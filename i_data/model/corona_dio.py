
import logging
import pandas as pd
import numpy as np
from i_data.configs.constants import CVD_HEADERS, CVD_COL_TYPES
from i_data.modules.functions import get_wc_lookup_id
from i_data.modules.clickhouse_client import ClickHouseClient

log = logging.getLogger(__name__)


class CoronaDIO:

	def __init__(self, dataframe):
		self.df = dataframe

	@classmethod
	def read_csv(cls, file_path):
		return cls(pd.read_csv(file_path))

	def describe(self):
		def format_series(series):
			desc = """\n"""
			for c, t in zip(self.df, series):
				desc += f'\t\t\t\t\t\t\t\t\t{c} -> {t}\n'
			return desc

		desc = f"""
				shape:				{self.df.shape}
				columns with nan:	{self.df.columns[self.df.isna().any()].tolist()}
				dtypes:				{format_series(self.df.dtypes)}
				"""
		log.info(desc)

	def transform(self):
		log.info('Transforming Data')
		self.df = self.df[CVD_HEADERS.keys()]
		self.df.rename(columns=CVD_HEADERS, inplace=True)
		self.df.dropna(subset=['event_time'], inplace=True)
		self.df.last_update.fillna(self.df.event_time, inplace=True)
		self.df.province_state.fillna(self.df.country, inplace=True)
		self.df.country.replace(to_replace='China', value='Mainland China', inplace=True)
		self.df['id'] = get_wc_lookup_id(self.df['province_state'])
		self.df[['confirmed', 'deaths', 'recovered']] = self.df[['confirmed', 'deaths', 'recovered']].astype(np.int64)
		self.df[['event_time', 'last_update']] = self.df[['event_time', 'last_update']].apply(
			lambda x: pd.to_datetime(x)
		)
		self.df['event_date'] = self.df['event_time'].apply(lambda x: pd.to_datetime(x).date())
		return self.df

	def ingest_data(self, data=None):
		log.info('Ingesting Data to CH database!')
		data = data or self.df
		client = ClickHouseClient()
		table = 'incidents'
		client.create_database('nCONOV')
		client.drop_table(table_name=table)
		client.create_table(table_name=table, columns=CVD_COL_TYPES)
		client.insert_bulk_data(data)



