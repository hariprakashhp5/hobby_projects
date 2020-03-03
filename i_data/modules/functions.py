
import pandas as pd
from common import ROOT
from os.path import join
from common.functions import read_config
CONFIG_DIR = join(ROOT, 'i_data', 'configs')


def get_configs():
	return read_config(join(CONFIG_DIR, 'config.yml'))


def get_wc_lookup_id(city_series):
	wc_file = join(ROOT, 'i_data', 'data', 'worldcities.csv')
	wc_df = pd.read_csv(wc_file)
	cache, lookup_ids = dict(), list()
	for city in city_series:
		city = city.split(',')[0]
		if city not in cache:
			lookup_row = wc_df.query(f'city == "{city}" or city_ascii == "{city}" or admin_name == "{city}" or country == "{city}"').head(1)
			lookup_id = lookup_row.id.item() if not lookup_row.id.empty else 0
			cache[city] = lookup_id
		lookup_ids.append(cache.get(city))
	return lookup_ids
