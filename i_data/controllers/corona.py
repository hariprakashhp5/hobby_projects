
import logging
from common import ROOT
from common.functions import FileSystem as fs
from i_data.model.corona_dio import CoronaDIO
from kaggle.api.kaggle_api_extended import KaggleApi

log = logging.getLogger(__name__)

DATA_SET_PATH = fs.join(ROOT, 'i_data', 'data', 'coronavirus')


def execute_process(trigger_args):
	kaggle = KaggleApi()
	kaggle.authenticate()
	log.info('Downloading Corono Virus Dataset from Kaggle')
	kaggle.dataset_download_files(dataset='sudalairajkumar/novel-corona-virus-2019-dataset',
										 path=DATA_SET_PATH, unzip=True, force=True)
	dio = CoronaDIO.read_csv(fs.join(DATA_SET_PATH, 'covid_19_data.csv'))
	dio.describe()
	dio.transform()
	dio.describe()
	dio.ingest_data()
	log.info('Done!')
