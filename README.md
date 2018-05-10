# test_fwPy

### A very simple framework you designed using the werkzeug and jinja2 library on MVC technology

### Controller
```
# not need import anything
# Controller/index.py

# class run With "/" 
class index():
  
  #Func Index run whene call index with "/"
	def index(self,argv):
		return self.view.render("index.html")
    
 #          class  def 
 # path == "index/page" 
 def page(self,argv):
   return sefl.view.render('page.html')

# view att with Controller and requests 
# can add any var or func our dict or list to view like this : 
  def v(self,argv):
      self.view.title = 'Title Page '
      self.view.name  = 'alaa aqgell'
      self.view.names = ['alaa','ali','muhammed']
      
      return self.view.render('viewTest.html')

#MODEL 
#model/index.py
    def m(self,argv):
        self.model.login(username='',password='')
        return self.view.render('modelTest.html')

```
### view 
```
<!-- view/viewTest.html -->
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
class index:
    def login(self,username='',password=''):
        return 'do samething'
    def logout(self,username='')
```
