def create_plugin(name, version, author, description):
	import qiime.core.registry as registry
	plugin = Plugin(name, version, author, description)
	registry.add_plugin(plugin)
	return plugin

class Plugin(object):
	def __init__(self, name, version, author, description):
		self._name = name
		self._version = version
		self._author = author
		self._description = description
		self._methods = {}

	def register_method(self, name):
		if self.has_method(name):
			raise Exception()

		def decorator(function):
			self._methods[name] = Method(name, function,
										 function.__annotations__,
										 function.__doc__)
		return decorator

	def has_method(self, name):
		return name in self._methods

	def get_method(self, name):
		if self.has_method(name):
			return self._methods[name]
		else:
			raise Exception()

	def get_methods(self):
		return self._methods.copy()

class Method(object):
	def __init__(self, name, function, annotations, docstring):
		self._function = function
		self.name = name
		self.annotations = annotations
		self.docstring = docstring

	def __call__(self, *args, **kwargs):
		return self._function(*args, **kwargs)
