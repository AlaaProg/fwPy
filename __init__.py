import os

from .server_mvc import server

class MVC(server):
	def __init__(this):

		if not ( os.path.exists("./controller") or os.path.exists("./controler") or os.path.exists("./ctrl") ):
			os.mkdir("./controller")

		# if not os.path.exists("./models") :
		# 	os.mkdir("./models")

		# if not os.path.exists("./view") :
		# 	os.mkdir("./view")

		# if not os.path.exists("./public") :
		# 	os.mkdir("./public")
		
		