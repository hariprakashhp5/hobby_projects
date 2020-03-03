
import yaml
import logging
from os.path import exists, join


def read_config(path):
	with open(path, 'r') as config_file:
		config = yaml.safe_load(config_file.read())
	return config


def init_logger(level=logging.DEBUG):
	handler = logging.StreamHandler()
	formatter = logging.Formatter(
		'%(asctime)s [%(name)-12s] %(levelname)-8s %(message)s')
	handler.setFormatter(formatter)
	logging.basicConfig(level=level, handlers=[handler])


class FileSystem:

	@staticmethod
	def exists(path):
		return exists(path)

	@staticmethod
	def join(*args):
		return join(*args)


if __name__ == '__main__':
	conf = read_config('D:\Scripts\in-dev\hobby_projects\i_data\configs\config.yml')
	print(conf)