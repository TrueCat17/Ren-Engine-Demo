init python:
    narrator = Character('')
    extend = Character(None)
    
    snd = Character('Звук', color='#808080')
    
	me = Character('Сэм', color='#DDDDAA')
	rn = Character('Рен', color='#FFFFFF')
	
	mr = Character('Маширо', color='#DD5566')
	mr_ship = Character('|> ! Я 4 7 |< 4', color='#FF0000')
	
	ar = Character('Эйрис', color='#B09080')
	
	
	traders_names = ['Нелли', 'Мира', 'Алиса', 'Юки', 'Кристина', 'Мария', 'Джек', 'Виктор', 'Лео']
	pirates_names = ['Гарри', 'Алекс', 'Нео', 'Анна', 'Ями']
	
	trader = Character('Торговец', color='#FFFF00')
	pirate = Character('Пират', color='#BB0000')
	
	def set_random_trader():
		global trader_num
		trader_num = random.randint(0, len(traders_names) - 1)
		set_name('trader', traders_names[trader_num])
	def set_random_pirate():
		global pirate_num
		pirate_num = random.randint(0, len(pirates_names) - 1)
		set_name('pirate', pirates_names[pirate_num])
	
	set_random_trader()
	set_random_pirate()
	
