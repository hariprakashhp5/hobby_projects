
class Email:

	def __init__(self, message):
		self._message = message

	def execute(self):
		print(self._message)
