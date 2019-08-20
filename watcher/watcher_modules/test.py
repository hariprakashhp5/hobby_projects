
class Test:

	def __init__(self, message):
		self._message = message.decode('utf-8')

	def execute(self):
		print(self._message)
