from jinja2 import (Environment, select_autoescape,FileSystemLoader)

class Argv:
	def __init__(self,kw):self.Argvs = {**kw}
	def __setitem__(self,key,value):self.Argvs.update({key:value})
	def __getattr__(self,key):return self.Argvs.get(key)



class View:
	GLOBALS = {}
	def __init__(self):
		self.env = Environment(
			autoescape = select_autoescape(['html', 'htm']),
			loader =  FileSystemLoader("view/")
		)

	def __setattr__(self,key,value):self.GLOBALS.update({key:value})
	def __getattr__(self,key):return self.GLOBALS.get(key)

	def render(self,path):
		template = self.env.get_template(path)
		return template.render( this= Argv( self.GLOBALS ) )

