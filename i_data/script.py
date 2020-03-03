
import logging
import argparse
import importlib
from i_data.modules.functions import get_configs
from common.functions import init_logger, FileSystem as fs

init_logger()
log = logging.getLogger(__name__)
config = get_configs()


def validate_inputs(ip):
	""" Method to validate if the received cli inputs are valid"""
	is_valid = True
	if ip.trigger not in config['triggers']:
		log.error(f'trigger [{ip.trigger}] is not available in the config file. terminating execution!')
		is_valid = False
	if ip.path and not fs.exists(ip.path):
		log.error(f'specified directory or file does not exists!')
		is_valid = False
	if not is_valid:
		exit(1)


def init_args():
	parser = argparse.ArgumentParser()
	ip_arguments = parser.add_argument_group('input arguments for the script')
	ip_arguments.add_argument("-t", "--trigger", dest="trigger", default="", required=True,
							  help="Provide appropriate trigger, refer config for list of available triggers")
	ip_arguments.add_argument("-p", "--path", dest="path", default=None, required=False,
							  help="Specify the directory or file from which data can be obtained")
	args = parser.parse_args()
	validate_inputs(args)
	return args


def main(args):
	try:
		trigger_obj = config['triggers'][args.trigger]
		trigger_obj['path'] = args.path
		module = importlib.import_module(f"i_data.controllers.{trigger_obj['controller']}")
		module.execute_process(trigger_obj)
	except Exception as ex:
		log.exception(ex)


if __name__ == '__main__':
	cli_args = init_args()
	main(cli_args)
