init python:
	def get_star_group_color(star_group, mouse_over):
		nears = selected_star_group.nears if selected_star_group else []
		for i in nears:
			if i is star_group:
				return star_group.selected_image
		if mouse_over:
			return star_group.mouse_over_image
		return star_group.image
	
	def get_star_color(star, mouse_over):
		nears = selected_star.nears if selected_star else []
		for i in nears:
			if i is star:
				return star.selected_image
		if mouse_over:
			return star.mouse_over_image
		return star.image
	
	
	def select_star_group(star_group):
		global selected_star_group
		selected_star_group = star_group
	def inside_star_group(star_group):
		global insided_star_group
		insided_star_group = star_group
	
	def select_star(star):
		global selected_star
		selected_star = star
	def inside_star(star):
		global insided_star
		insided_star = star
	
	
	def click_on_field():
		sw, sh = get_stage_width(), get_stage_height()
		
		mouse_x, mouse_y = get_mouse()
		mouse_x -= field_x
		
		if insided_star_group:
			for star in insided_star_group.stars:
				x = int(star.pos[0] * sw)
				y = int(star.pos[1] * sh)
			
				mouse_over = get_dist(x, y, mouse_x, mouse_y) <= star.half_size
				if mouse_over:
					inside_star(star)
					break
		else:
			for star_group in star_groups:
				x = int(star_group.pos[0] * sw)
				y = int(star_group.pos[1] * sh)
			
				mouse_over = get_dist(x, y, mouse_x, mouse_y) <= star_group.half_size
				if mouse_over:
					inside_star_group(star_group)
					break
	
	def exit_from_star_group():
		inside_star_group(None)

screen galaxy:
	key 'Escape' action exit_from_star_group
	
	python:
		sw, sh = get_stage_width(), get_stage_height()
		field_width = int(sw * 0.7)
		field_x = sw - field_width
		
		mouse_x, mouse_y = get_mouse()
		mouse_x -= field_x
		
		tmp = [(field_width, sh), (0, 0), im.Rect("#101040", field_width, sh)]
		
		if insided_star_group:
			select_star(None)
			
			for star in insided_star_group.stars:
				x = int(star.pos[0] * sw)
				y = int(star.pos[1] * sh)
				
				mouse_over = get_dist(x, y, mouse_x, mouse_y) <= star.half_size
				if mouse_over:
					select_star(star)
					break
			
			for star in insided_star_group.stars:
				x = int(star.pos[0] * sw)
				y = int(star.pos[1] * sh)
				
				mouse_over = get_dist(x, y, mouse_x, mouse_y) <= star.half_size
				if mouse_over:
					select_star(star)
				
				tmp += [(x - star.half_size, y - star.half_size), get_star_color(star, mouse_over)]
		else:
			select_star_group(None)
			
			for star_group in star_groups:
				x = int(star_group.pos[0] * sw)
				y = int(star_group.pos[1] * sh)
				
				mouse_over = get_dist(x, y, mouse_x, mouse_y) <= star_group.half_size
				if mouse_over:
					select_star_group(star_group)
					break
			
			for star_group in star_groups:
				x = int(star_group.pos[0] * sw)
				y = int(star_group.pos[1] * sh)
				
				mouse_over = get_dist(x, y, mouse_x, mouse_y) <= star_group.half_size
				if mouse_over:
					select_star_group(star_group)
				
				tmp += [(x - star_group.half_size, y - star_group.half_size), get_star_group_color(star_group, mouse_over)]
		field = im.Composite(*tmp)
	
	
	button:
		xpos field_x
		xysize (field_width, get_stage_height())
		
		action click_on_field
		
		ground field
		hover field

