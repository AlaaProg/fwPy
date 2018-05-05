from jinja2 import BaseLoader, TemplateNotFound, Template, Environment, select_autoescape

# template = Template('Hello {{ name }}!')

# template.render(name='John Doe')

class MyLoader(BaseLoader):
	def __init__(self, path):
		self.path = path
	def get_source(self, environment, template):
		path = join(self.path, template)
		if not exists(path):
			raise TemplateNotFound(template)
			mtime = getmtime(path)
			with file(path) as f:
				source = f.read().decode('utf-8')
		return source, path, lambda: mtime == getmtime(path