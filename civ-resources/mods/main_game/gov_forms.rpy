init python:
	class GovForm(Object):
		def __init__(self, name):
			Object.__init__(self)
			
			self.name = name
			self.modifications = Object()
			self.game_over = Object()
	
	
	anarchy = GovForm('Анархия')
	anarchy.modifications.angry = 0.5
	anarchy.modifications.science_and_trade = 0.1
	anarchy.modifications.production = 0.7
	anarchy.modifications.food = 0.8
	
	anarchy.game_over.angry_population = 0
	anarchy.game_over.count_turns = -1
	
	anarchy.max_count_turns = 10
	anarchy.min_authority = 0
	
	
	monarchy = GovForm('Монархия')
	monarchy.modifications.angry = 0.7
	monarchy.modifications.science_and_trade = 0.7
	monarchy.modifications.production = 1.0
	monarchy.modifications.food = 1.1
	
	monarchy.game_over.angry_population = 0.5
	monarchy.game_over.count_turns = 0
	
	monarchy.max_count_turns = -1
	monarchy.min_authority = 0
	
	
	republic = GovForm('Республика')
	republic.modifications.angry = 1.0
	republic.modifications.science_and_trade = 1.1
	republic.modifications.production = 0.9
	republic.modifications.food = 1.0
	
	republic.game_over.angry_population = 0.3
	republic.game_over.count_turns = 10
	
	republic.max_count_turns = -1
	republic.min_authority = 0
	
	
	communism = GovForm('Коммунизм')
	communism.modifications.angry = 0.9
	communism.modifications.science_and_trade = 0.9
	communism.modifications.production = 1.4
	communism.modifications.food = 1.1
	
	communism.game_over.angry_population = 0
	communism.game_over.count_turns = -1
	
	communism.max_count_turns = -1
	communism.min_authority = 0.05
	
	
	democracy = GovForm('Демократия')
	democracy.modifications.angry = 1.1
	democracy.modifications.science_and_trade = 1.3
	democracy.modifications.production = 0.7
	democracy.modifications.food = 0.9
	
	democracy.game_over.angry_population = 0.3
	democracy.game_over.count_turns = 2
	
	democracy.max_count_turns = -1
	democracy.min_authority = 0
	
	
	
	
	gov_forms = (anarchy, monarchy, republic, communism, democracy)
	gov_form = random.choice(gov_forms)
	
