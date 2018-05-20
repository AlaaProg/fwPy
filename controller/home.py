
class home(object):

	# Route home/
	def index(self,arg):

		return "Hello To Home Page"
		
	#Route home/vtest
	def vtest(self,argv):
		# Test VIEW 
		self.view.title = 'Title Page '
		self.view.name  = 'alaa aqgell'
		self.view.names = ['alaa','ali','muhammed']

		return self.view.render('home.html')

	#Route home/mtest
	def mtest(self,argv):
		# Test MODEL  
		mtest = self.model.test()
		return mtest
