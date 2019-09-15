import re
from watcher.generic_modules.helpers import type_cast
from watcher.generic_modules.file_utils import load_config


class SMS:

	config = load_config('sms_template_config.yml')

	def __init__(self, message):
		self._message = message.decode('utf-8')

	def __get_matching_regex(self):
		patterns = SMS.config.patterns
		for idx, pattern_conf in enumerate(patterns):
			regex = re.compile(pattern_conf.pattern, re.IGNORECASE)
			if regex.match(self._message):
				return {'regex_id': idx, 'regex': regex, 'schema': pattern_conf.schema}
		return None

	def __get_data_type(self, field):
		data_types_map = SMS.config.data_type
		return eval(getattr(data_types_map, field, 'str'))

	def __extract_valuables(self):
		matching_pattern = self.__get_matching_regex()
		resp_dict = {'message': self._message}
		if matching_pattern:
			resp_dict['regex_used'] = matching_pattern['regex_id']
			matches = matching_pattern['regex'].findall(self._message)
			match = matches[0] if isinstance(matches[0], tuple) else matches
			for key, value in matching_pattern['schema']:
				data_type = self.__get_data_type(value)
				resp_dict[value] = type_cast(match[int(key)], data_type)
		return resp_dict

	def execute(self):
		vals = self.__extract_valuables()
		print(vals)
