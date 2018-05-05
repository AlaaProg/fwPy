from werkzeug.wrappers import Response as resp,Request as req
from .controller import Controller

class Response(resp):

	default_mimetype = 'text/html'

	def setHeader(self,headers):
		for k,v in headers.items():
			self.headers.set(k,v)

	# def setCookies(self,key,value):
	# 	pass


class Request(req):
	# request = {}

	def resp_ctx(self):
		# self.request.update({'path':self.path})
		self.ctrl = Controller(self)

		if self.path == "/":
			return self.ctrl.loadDefaultCtrl()

		return self.ctrl.loader(self.path)
		