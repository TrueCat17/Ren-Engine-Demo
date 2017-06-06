init:
	$ mods['main'] = 'main_game'

label main:
	$ days = 0
	scene bg menu with dspr
	
	menu:
		'Начало':
			jump start
		'Перед звёздами':
			jump before_stars
		''
		'Рут Маширо':
			menu:
				'Встреча':
					jump mr_meet
				'Проблема (без конкурса)':
					$ install_filter = False
					$ root_name = 'mr'
					jump mr_problem
				'Проблема (конкурс)':
					$ install_filter = True
					$ root_name = 'mr'
					jump mr_problem
				'Назад':
					jump main
		'Рут Эйрис':
			menu:
				'Встреча':
					jump ar_meet
				'q':
					jump ar_
				'Назад':
					jump main
		''
		'Выход':
			$ exit_from_game()

