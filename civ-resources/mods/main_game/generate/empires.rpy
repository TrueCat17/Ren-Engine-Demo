init python:
	
	def set_star_empire(star, empire):
		star.image = im.Circle(empire.color, star.size, star.size)
		
		old_empire = star.empire
		if old_empire:
			for i in xrange(len(old_empire.stars)):
				if old_empire.stars[i] is star:
					old_empire.stars = old_empire.stars[0:i] + old_empire.stars[i+1:]
					break
		star.empire = empire
		empire.stars.append(star)
	
	def generate_empires():
		global empires
		
		empires = []
		for i in xrange(len(star_groups)):
			count_stars = len(star_groups[i].stars)
			count = random.randint(MIN_STAR_IN_GROUP / 3, count_stars * 2/3)
			
			cur_empires = []
			stars = star_groups[i].stars
			
			for j in xrange(count):
				empire = get_new_empire()
				empire.name = str(len(empires) + j)
				
				set_star_empire(stars[j], empire)
				cur_empires.append(empire)
			
			free_stars = stars[count:]
			while free_stars:
				n = random.randint(0, len(free_stars) - 1)
				star = free_stars[n]
				
				near_empires = []
				for i in star.nears:
					if i.empire:
						near_empires.append(i.empire)
				if near_empires:
					free_stars = free_stars[0:n] + free_stars[n+1:]
					
					empire = random.choice(near_empires)
					set_star_empire(star, empire)
			
			empires += cur_empires
	
	
	def get_new_empire():
		res = Object()
		
		r, g, b = random.randint(5, 12) * 20, random.randint(5, 12) * 20, random.randint(5, 12) * 20
		color = (r << 16) + (g << 8) + b
		color_str = hex(color)[2:]
		color_str = '0' * (6 - len(color_str)) + color_str
		res.color = color_str
		
		res.gov_form = random.choice(gov_forms)
		
		res.moneys = random.randint(400, 1000)
		res.technologies = random.randint(200, 350)
		
		res.stars = []
		res.spaceships = []
		
		res.ai = None
		
		return res
	
	
