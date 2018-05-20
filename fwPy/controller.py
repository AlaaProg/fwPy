import os,importlib as lib
from .view import View

class Controller:
	PathCtrl   = "controller."
	PathModels = "models."
	Index      = "index"

	def __init__(self,request):
		self.req = request
		self.view = View()

	def loader(self,path):
		self.url = path.strip("/").split("/")

		if os.path.exists("controller/"+self.url[0]+".py"):
			return self.loaderClass()

		return self.errorCtrl()


	def loaderClass(self):

		cl = self.PathCtrl+self.url[0]

		load_ctrl  = lib.import_module(cl)

		load_class  = getattr(load_ctrl,self.url[0])
		
		self.loaderModel(load_class)

		if len(self.url) > 1 and load_class.__dict__.get(self.url[1]):
			return self.loaderFunc(load_class,self.url[1])

		elif load_class.__dict__.get("index"):
			return self.loaderFunc(load_class,self.Index)

		elif load_class.__dict__.get("error"):
			return self.loaderFunc(load_class,'error')

		return self.errorFunc(cl+"."+self.url[1] if len(self.url) > 1 else cl+"."+self.Index)


	def loaderModel(self,_class):
		try:

			load_model  = lib.import_module(self.PathModels+_class.__name__)
			load_model  = getattr(load_model,_class.__name__)
			setattr(_class,"model",load_model())

		except Exception as error:
			setattr(_class,"model",lambda:"No Model: %s"%_class.__name__)

		# set attr to _class Controller 
		setattr(_class,"request",self.req )
		setattr(_class,"view",self.view   )

	def loaderFunc(self,clas,func):
		function  = getattr(clas(),func)
		return function(self.url[2:] if len(self.url) > 2 else [])



	def errorFunc(self,_cf):
		raise Exception("No Function named: '%s' "%_cf)

	def errorCtrl(self):
		raise Exception('No Controller named:  "%s" '%self.url[0])
