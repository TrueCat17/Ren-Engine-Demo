init python:
	
	# params:
	
	# count
	MIN_STAR_GROUPS = 10
	MAX_STAR_GROUPS = 30
	
	# pixels
	MIN_STAR_GROUP_SIZE = 10
	MAX_STAR_GROUP_SIZE = 20
	
	
	# count
	MIN_STAR_IN_GROUP = 4
	MAX_STAR_IN_GROUP = 10
	
	# pixels
	MIN_STAR_SIZE = 14
	MAX_STAR_SIZE = 20
	
	
	# max star properties
	MAX_STAR_FOOD = 4
	MAX_STAR_PRODUCTION = 10
	MAX_STAR_TRADING = 10
	
	
	COUNT_NEARS = 6
	SECTOR_ANGLE = 2 * math.pi / COUNT_NEARS
	
	
	def get_nears(obj, array):
		tmp = [None] * COUNT_NEARS
		
		for i in array:
			if i is not obj:
				dx = obj.pos[0] - i.pos[0]
				dy = obj.pos[1] - i.pos[1]
				
				dist2 = dx*dx + dy*dy
				angle = math.atan2(dy, dx) % (2 * math.pi)
				
				n = in_bounds(int(angle / SECTOR_ANGLE), 0, COUNT_NEARS - 1)
				if tmp[n] is None or dist2 < tmp[n][0]:
					tmp[n] = (dist2, i)
		
		res = []
		for i in tmp:
			if i is not None:
				res.append(i[1])
		
		return res
				
	
	
	
	
	def generate_star_groups():
		global star_groups
		
		star_groups = []
		for i in xrange(random.randint(MIN_STAR_GROUPS, MAX_STAR_GROUPS)):
			star_groups.append(get_new_star_group())
		
		for i in star_groups:
			i.nears = get_nears(i, star_groups)
	
	def get_new_star_group():
		res = Object()
		res.name = str(len(star_groups))
		
		res.size = random.randint(MIN_STAR_GROUP_SIZE, MAX_STAR_GROUP_SIZE)
		res.half_size = int(res.size / 2)
		
		r, g, b = random.randint(170, 255), random.randint(170, 255), random.randint(170, 255)
		color = (r << 16) + (g << 8) + b
		color_str = hex(color)[2:]
		color_str = '0' * (6 - len(color_str)) + color_str
		res.image = im.Circle(color_str, res.size, res.size)
		res.selected_image = im.Circle('00AA00', res.size, res.size)
		res.mouse_over_image = im.Circle('0080FF', res.size, res.size)
		
		ok = False
		while not ok:
			ok = True
			
			x, y = random.randint(10, 60) / 100.0, random.randint(10, 90) / 100.0
			for star_group in star_groups:
				dx = abs(x - star_group.pos[0])
				dy = abs(y - star_group.pos[1])
				
				if dx < 0.05 and dy < 0.05:
					ok = False
					break
		
		res.pos = (x, y)
		
		res.stars = []
		for i in xrange(random.randint(MIN_STAR_IN_GROUP, MAX_STAR_IN_GROUP)):
			res.stars.append(get_new_star(res))
		for i in res.stars:
			i.nears = get_nears(i, res.stars)
		
		return res
	
	def get_new_star(star_group):
		res = Object()
		res.name = str(len(star_group.stars))
		
		res.size = random.randint(MIN_STAR_SIZE, MAX_STAR_SIZE)
		res.half_size = int(res.size / 2)
		
		res.selected_image = im.Circle('00AA00', res.size, res.size)
		res.mouse_over_image = im.Circle('0080FF', res.size, res.size)
		
		ok = False
		while not ok:
			ok = True
			
			x, y = random.randint(10, 60) / 100.0, random.randint(10, 90) / 100.0
			for star in star_group.stars:
				dx = abs(x - star.pos[0])
				dy = abs(y - star.pos[1])
				
				if dx < 0.05 and dy < 0.05:
					ok = False
					break
		
		res.pos = (x, y)
		
		res.food       = random.randint(1, MAX_STAR_FOOD)
		res.production = random.randint(1, MAX_STAR_PRODUCTION)
		res.trading    = random.randint(1, MAX_STAR_TRADING)
		
		res.x_food, res.x_production, res.x_trading = 1, 1, 1
		
		res.population = res.food * res.x_food
		
		return res
	
