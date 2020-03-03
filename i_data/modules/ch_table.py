

MergeTree = """
				ENGINE = MergeTree()
				PARTITION BY toYYYYMM({0})
				ORDER BY ({0})
				SETTINGS index_granularity = 8192
			"""

engines = dict(mergetree=MergeTree)


class CHTable:

	def __init__(
			self,
			table_name: str,
			columns: list,
			engine: str='mergetree',
			db_name: str=''
	):
		self.table = f'{db_name}.{table_name}' if db_name else table_name
		self.columns = columns
		self.engine = engine

	def get_query(self):
		query_tmplt = "CREATE TABLE IF NOT EXISTS {0}	({1})	{2}"
		engine_tmplt = engines.get(self.engine)
		column, engine = str(), str()
		for idx, item in enumerate(self.columns):
			column_tmplt = "`{0}`	{1}"
			column += column_tmplt.format(item[0], item[1])
			if idx != len(self.columns) - 1:
				column += ', '
			if len(item) > 2 and item[2]:
				engine = engine_tmplt.format(item[0])
		query = query_tmplt.format(self.table, column, engine)
		return query
