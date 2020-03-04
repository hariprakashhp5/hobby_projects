
CVD_HEADERS = {
			'SNo': 'sno', 'ObservationDate': 'event_time',
			'Province/State': 'province_state', 'Last Update': 'last_update',
			'Country/Region': 'country', 'Confirmed': 'confirmed',
			'Deaths': 'deaths', 'Recovered': 'recovered'
			}

CVD_COL_TYPES = [('sno', 'UInt16'), ('id', 'UInt64'), ('event_date', 'Date', True), ('event_time', 'DateTime'),
				 ('province_state', 'String'), ('country', 'String'), ('last_update', 'DateTime'),
				 ('confirmed', 'UInt16'), ('deaths', 'UInt16'), ('recovered', 'UInt16')]

WC_COL_TYPES = [('event_date', 'Date'), ('city', 'String'), ('city_ascii', 'String'), ('lat', 'Float64'),
				('lng', 'Float64'), ('country', 'String'), ('iso2', 'String'), ('iso3', 'String'), ('admin_name', 'String'),
				('capital', 'String'), ('population', 'Float64'), ('id', 'UInt64', True)]
