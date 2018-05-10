import os

from .server_mvc import server

class FwPy(server):
	def __init__(self):

		if not ( os.path.exists("./controller") or os.path.exists("./controler") or os.path.exists("./ctrl") ):
			os.mkdir("./controller")

		if not os.path.exists("./models") :
			os.mkdir("./models")

		if not os.path.exists("./view") :
			os.mkdir("./view")

		# if not os.path.exists("./public") :
		# 	os.mkdir("./public")
		
		
