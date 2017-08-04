init python:
	impery_name = 'Some Impery Name'
	turn = 1
	
	
	selected_star_group = None
	selected_star = None
	
	insided_star_group = None
	insided_star = None
	
	
	moneys = 50
	technologies = random.randint(101, 140)
	
	state_money = 50
	state_science = 50
	state_luxury = 0
	
	
	def get_count_stars(star_system = None):
		if star_system is None:
			res = 0
			for star_group in star_groups:
				res += len(star_group.stars)
			return res
		return len(star_group.stars)
	def get_population(star_group = None):
		res = 0
		if star_group is None:
			for star_group in star_groups:
				res += get_population(star_group)
		else:
			for star in star_group.stars:
				res += star.population
		return res
	
	def get_moneys_changing():
		return '+0'
	def get_technologies_changing():
		return '+0'
	
	def get_spaceships():
		return 0
	def get_angry_population():
		return int(get_spaceships() * gov_form.modifications.angry)
	
	
	def state_money_up():
		global state_money, state_science, state_luxury
		
		if state_money == 100:
			return
		if state_science > 0:
			state_science -= 10
		else:
			state_luxury -= 10
		state_money += 10
	def state_money_down():
		global state_money, state_science
		
		if state_money == 0:
			return
		state_science += 10
		state_money -= 10
	
	def state_science_up():
		global state_money, state_science, state_luxury
		
		if state_science == 100:
			return
		if state_money > 0:
			state_money -= 10
		else:
			state_luxury -= 10
		state_science += 10
	def state_science_down():
		global state_science, state_money
		
		if state_science == 0:
			return
		state_money += 10
		state_science -= 10
	
	def state_luxury_up():
		global state_money, state_science, state_luxury
		
		if state_luxury == 100:
			return
		if state_money > 0:
			state_money -= 10
		else:
			state_science -= 10
		state_luxury += 10
	def state_luxury_down():
		global state_luxury, state_money
		
		if state_luxury == 0:
			return
		state_money += 10
		state_luxury -= 10
	
	
	impery_info = ''
	def update_impery_info():
		global impery_info
		
		impery_info = get_color_text(
			impery_name + '\n' +
			'Ход №' + str(turn) + '\n' +
			gov_form.name,                                                                         'FF0000',
			
			'',                                                                                    '000000',
			
			'Деньги: '     +    str(moneys)    + ' (' +    get_moneys_changing()    + ')',         'FFFF00',
			'Технологии: ' + str(technologies) + ' (' + get_technologies_changing() + ')',         '0080FF',
			
			'',                                                                                    '000000',
			
			'В империи:\n' +
			' Звёзд: ' + str(get_count_stars()) + '\n' +
			' Людей: ' + str(get_population())  + ' млрд.\n' +
			' Кораблей: ' + str(get_spaceships()),                                                 '00AA00',
			
			'',                                                                                    '000000',
			
			'Недовольных жителей: ' + str(get_angry_population()) + '%',                           'FFFFFF'
		)


screen info:
	python:
		update_impery_info()
		
		text_size = get_stage_width() / 50
	
	
	text impery_info:
		align (0.03, 0.03)
		size text_size
	
	vbox:
		align (0.03, 0.65)
		
		text (('Звёздное скопление <' + selected_star_group.name + '>') if selected_star_group else '') color '#FFFFFF'
		if selected_star:
			text ('Звезда <' + selected_star.name + '>') color '#FFFFFF'
			text ('Империя <' + selected_star.empire.name + '>') color ('#' + selected_star.empire.color)
	
	
	vbox:
		align (0.03, 0.97)
		
		hbox:
			spacing 5
			
			text ('Деньги:  ' + str(state_money).rjust(3)   + '%') color '#FFFF00' size text_size
			textbutton '↑' color '#FFFFFF' xysize (20, 20) action state_money_up
			textbutton '↓' color '#FFFFFF' xysize (20, 20) action state_money_down
		hbox:
			spacing 5
			
			text ('Наука:   ' + str(state_science).rjust(3) + '%') color '#0080FF' size text_size
			textbutton '↑' color '#FFFFFF' xysize (20, 20) action state_science_up
			textbutton '↓' color '#FFFFFF' xysize (20, 20) action state_science_down
		hbox:
			spacing 5
			
			text ('Роскошь: ' + str(state_luxury).rjust(3)  + '%') color '#FF8000' size text_size
			textbutton '↑' color '#FFFFFF' xysize (20, 20) action state_luxury_up
			textbutton '↓' color '#FFFFFF' xysize (20, 20) action state_luxury_down
		
		null ysize 15
		textbutton 'Завершить ход' xalign 0.5 action next_turn
	
	
