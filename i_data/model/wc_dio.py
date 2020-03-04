
import datetime
import logging
import pandas as pd
from i_data.modules.clickhouse_client import ClickHouseClient
from i_data.configs.constants import WC_COL_TYPES

log = logging.getLogger(__name__)


class WCDIO:

	def __init__(self, data, db: str='', table: str=''):
		self.df = data
		self.db = db
		self.table = table

	def ingest_to(self, db_table):
		self.db, self.table = db_table.split('.')

	@classmethod
	def read_csv(cls, file_path):
		return cls(pd.read_csv(file_path))

	def transform(self):
		self.df.fillna(dict(iso2='XX', admin_name='unknown', capital='unknown', population=0), inplace=True)
		self.df['event_date'] = datetime.date.today()
		return self.df

	def ingest_data(self, data=None):
		log.info('Ingesting Data to CH database!')
		data = data or self.df
		client = ClickHouseClient()
		client.create_database(self.db)
		client.drop_table(table_name=self.table)
		client.create_table(table_name=self.table, engine='join', columns=WC_COL_TYPES)
		client.insert_bulk_data(data)
