

class ResponseHandler(object):
	def __init__(self,fn):
		self._func = fn

	def __call__(self, *args, **kw):
		print("ResponseHandler====================>args:",args)
		print("ResponseHandler====================>kw:",kw)
		try:
			r =  self._func(*args, **kw)
			return r
		except:
			print("404")
			pass