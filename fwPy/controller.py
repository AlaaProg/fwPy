import os,importlib as lib
from .view import View

class Controller():
	path_ctrl  = "controller."
	path_model = "models."
	index      = "index"

	def __init__(self,request):
		self.req = request
		self.view = View()

	def loader(self,path):
		return self.loadCtrl(path.strip("/").split("/"))


	def loadCtrl(self,pkg):
		
		clas      = pkg[0] 
		function  = pkg[1] if len(pkg) > 1 else self.index
		# print(function)

		if os.path.exists("controller/"+clas+".py"):
			# import  file.py from controller
			load_ctrl  = lib.import_module(self.path_ctrl+clas)
			# loader Class 
			load_class  = getattr(load_ctrl,clas)
			self.loadModel(load_class)
			
			# isinclass
			if load_class.__dict__.get(function):
				# Loader function 'def'
				function  = getattr(load_class(),function)
				
				return function(pkg[2:])

		
			function  = getattr(load_class(),self.index)
			return function(pkg[1:])

			



	def loadModel(self,clas):
		try:
			load_model  = lib.import_module(self.path_model+clas.__name__)
			load_model  = getattr(load_model,clas.__name__)
			setattr(clas,"model",load_model())
		except Exception as error:
			setattr(clas,"model",self.ErrorModel)


		setattr(clas,"request",self.req )
		setattr(clas,"view",self.view   )

	def loadDefaultCtrl(self):
		return self.loadCtrl(["index"])

	def ErrorModel(self):
		return "Error Model"
