from django.http import Http404


class ResponseHandler(object):
	def __init__(self,fn):
		self._func = fn

	def __call__(self, *args, **kw):
		print("ResponseHandler====================>args:",args)
		print("ResponseHandler====================>kw:",kw)
		try:
			r =  self._func(*args, **kw)
			return r
		except :
			raise



class Pager(object):
	def __init__(self,item_count, page_index = 1,page_size = 3):
		self.item_count = item_count
		self.page_size = page_size
		self.page_count = item_count //page_size +(1 if item_count % page_size >0 else 0)
		self.start_index = 1
		self.end_index = self.page_count
		self.page_range = range(1,self.page_count+1)
		print("page_index > self.page_count=============>",page_index > self.page_count)
		if item_count == 0:
			self.offset = 0
			self.limit = 0
			self.page_index = 1
		elif (page_index > self.page_count) or page_index < 1:
			self.page_index = 1
			self.offset = (self.page_index - 1 )* self.page_size
			self.limit = self.page_index * self.page_size
		else:
			self.page_index = page_index
			# self.offset = (page_index - 1 )* self.page_size
			# self.limit = (page_index - 1 )* self.page_size + page_size
			self.offset = (self.page_index - 1 )* self.page_size
			self.limit = self.page_index * self.page_size
		print("self.offset=================>",self.offset)
		print("self.limit=================>",self.limit)
		print("self.page_index < self.page_count===============>",self.page_index < self.page_count)
		self.has_next = self.page_index < self.page_count
		print("self.page_index > 1=============================>",self.page_index > 1)
		self.has_prevoius = self.page_index > 1
		if self.has_next:
			self.next_page = self.page_index +1
		if self.has_prevoius:
			self.prev_page = self.page_index -1
	def __str__(self):
		return 'item_count: %s, page_count: %s, page_index: %s, page_size: %s, offset: %s, limit: %s' % (self.item_count, self.page_count, self.page_index, self.page_size, self.offset, self.limit)
	__repr__ = __str__
