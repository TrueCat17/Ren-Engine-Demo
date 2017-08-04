init python:
	mods['start_main_menu'] = 'main_menu'
	start_screens = 'main_menu'


screen main_menu:
	image "images/bg/menu.jpg":
		xysize (1.0, 1.0)
	
	vbox:
		align (0.5, 0.5)
		spacing 5
		
		textbutton "Начать" size 20 xysize (300, 35) action Function(start_mod, "main_game")
		textbutton "Выход"  size 20 xysize (300, 35) action exit_from_game


label start_main_menu:
	while True:
		pause 1

