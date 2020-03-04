
import logging
from common import ROOT
from i_data.model.wc_dio import WCDIO
from common.functions import FileSystem as fs

log = logging.getLogger(__name__)

DATA_SET_PATH = fs.join(ROOT, 'i_data', 'data', 'worldcities.csv')


def execute_process(trigger_args):
	dio = WCDIO.read_csv(DATA_SET_PATH)
	dio.transform()
	dio.ingest_to(f'{trigger_args.get("db_name")}.{trigger_args.get("table_name")}')
	dio.ingest_data()
	log.info('Done')
