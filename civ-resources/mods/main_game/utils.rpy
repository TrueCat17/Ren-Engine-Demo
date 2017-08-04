init -10000 python:
	
	def get_color_text(*args):
		res = ''
		
		for i in xrange(len(args) / 2):
			res += '{color=' + args[i*2 + 1] + '}' + args[i*2] + '{/color}' + '\n'
		
		return res[:-1]
