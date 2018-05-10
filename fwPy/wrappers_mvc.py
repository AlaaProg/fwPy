from werkzeug.wrappers import Response as resp,Request as req
from .controller import Controller

class Response(resp):

	default_mimetype = 'text/html'

	def setHeader(self,headers):
		for k,v in headers.items():
			self.headers.set(k,v)



	def setCookies(self,k):
		if k:
			self.set_cookie(*k)


class Request(req):
	req__cookie	= None


	def resp_ctx(self):
		req = {'path':self.path,
				"method":self.method,
				"form":self.form,
				"host":self.host,
				"headers":self.headers,
				"cookies":self.cookies,
				"args":self.args}

		self.ctrl = Controller(req)
		if self.path == "/":
			return self.ctrl.loadDefaultCtrl()
		return self.ctrl.loader(self.path)



	def setCookies(self,*v):
		self.req__cookie = tuple(v)
		
