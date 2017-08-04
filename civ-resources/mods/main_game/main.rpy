init 1 python:
	mods['main'] = 'main_game'
	start_screens = 'galaxy info'
	
	def init():
		set_fps(10)
		
		generate_star_groups()
		generate_empires()
	
	init()

label main:
	while True:
		pause 0.1
