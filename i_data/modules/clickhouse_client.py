
import logging
from os import environ
from i_data.modules.ch_table import CHTable
from clickhouse_driver import Client

log = logging.getLogger(__name__)


class ClickHouseClient(Client):

	def __init__(self, *args, **kwargs):
		self.database = kwargs.get('database', '')
		self.table_name = None
		super(ClickHouseClient, self).__init__(host=environ.get('CH_HOST'), *args, **kwargs)

	def show_databases(self):
		return self.execute('SHOW DATABASES')

	def create_database(self, db_name):
		self.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')
		self.execute(f'USE {db_name}')

	def create_table(self, table_name: str, columns: list, engine: str='mergetree', db_name: str=''):
		table = CHTable(table_name, columns=columns, engine=engine, db_name=db_name or self.database)
		self.execute(table.get_query())
		self.table_name = table.table

	def show_tables(self, db_name: str=''):
		db_name = db_name or self.database
		self.execute(f'USE {db_name}')
		return self.execute('SHOW TABLES')

	def __get_db_table(self, table_name: str='', db_name: str=''):
		db_name = db_name or self.database
		table_name = table_name or self.table_name
		return f'{db_name}.{table_name}' if db_name else table_name

	def insert_bulk_data(self, dataframe, table_name: str='', db_name: str=''):
		db_table = self.__get_db_table(table_name, db_name)
		self.execute(f'INSERT INTO {db_table} VALUES', dataframe.to_dict('records'), types_check=True)
		log.info(f'Inserted {self.count_recs()} Records!')

	def drop_table(self, table_name: str='', db_name: str=''):
		db_table = self.__get_db_table(table_name, db_name)
		self.execute(f'DROP TABLE IF EXISTS {db_table}')

	def count_recs(self, table_name: str='', db_name: str=''):
		db_table = self.__get_db_table(table_name, db_name)
		return self.execute(f"SELECT COUNT(*) FROM {db_table}")[0]


# if __name__ == '__main__':
# 	client = ClickHouseClient()
# 	client.create_database(db_name='temps')
# 	print(client.show_databases())
# 	print(client.create_table('tst', columns=[('A', 'UInt16'), ('B', 'Date', True), ('C', 'UInt16')]))
# 	print(client.show_tables(db_name='default'))
# 	print(client.count_recs(table_name='tst'))
# 	client.drop_table(table_name='tst')
