#define some excepts

class DownloadException(Exception):
	def __init__(self,message):
		Exception.__init__(self)
		self.message = message

class BuildkernelException(Exception):
	def __init__(self,message):
		Exception.__init__(self)
		slef.message = message
