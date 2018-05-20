# [fwPy](https://alaaprog.github.io/fwPy/)
### A very simple framework you designed using the werkzeug and jinja2 library on MVC technology

### Controller
controller/index.py
-------------------

```
class index:

  #Route /
  def index(self,argv):
	return self.view.render("index.html")
```

controller/home.py
------------------
```
	class home:

	  # Route home/
	  def index(self,arg):
	      return "Hello To Home Page "

	  #Route home/vtest
	  def vtest(self,argv):
	      self.view.title = 'Title Page '
	      self.view.name  = 'alaa aqgell'
	      self.view.names = ['alaa','ali','muhammed']

	      return self.view.render('home.html')

	  #Route home/mtest
	  def mtest(self,argv):
	      self.model.login(username='',password='')
	      return self.view.render('modelTest.html')
```

### view 
```
	<html>
	<head>
		<title> {{ this.title }} </title>
	</head>
	<body>

		   {{ this.name }} 

		  {% for i in this.names %}
		    {{ i }}

		  {% endfor %}

	</body>
	</html>
```
### MODEL
```
	class home:
	    def login(self,username='',password=''):
		return 'do samething'
	    def logout(self,username=''):
		# some code 
```
