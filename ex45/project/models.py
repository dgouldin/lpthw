import data_store

class Room(object):

	#properties = state (state is about data)
	def __init__(self, character, title, description, items, doors, enemies):
		self.title = title
		self.items = items
		self.description = description
		self.doors = doors
		self.enemies = enemies
		self.character = character
	
	#behaviors = functions, instance method
	def enter(self):
		return self.description
	
	def get_item(self, item):
		if item in self.items:
			if len(self.character['stuff']) <= 5
				self.items.remove(item)
				self.character['stuff'].append(item)
				return 'get %s' % item
			else:
				raise ValueError("You are carrying too much stuff! Drop or use something first.")
		else:
			raise ValueError('There is no %r that you can get.' % item)
			
	def use_item(self, item):	
		if item in self.character['stuff']:
			return 'use %s' % item
		else:
			raise ValueError('You do not have any %r!' % item)
			
	def drop_item(self, item):	
		if item in self.character['stuff']:
			self.character['stuff'].remove(item)
			self.items.append(item)
			return 'drop %s' % item
		else:
			raise ValueError('You do not have any %r!' % item)
	
	def next_room(self, door):
		if door in self.doors:
			if door == 'stairs':
				if 'key' in self.character['stuff']:
					return 'go %s' % door
				else:
					raise ValueError('The door appears to be locked.')
			if len(self.enemies) == 0:
				return 'go %s' % door
			else:
				raise ValueError('The %s blocks your escape.' % self.enemies[0])
		else:
			raise ValueError('There is no %r door.' % door)
					
	def search_room(self, searched):
		if len(self.items) == 0:
			return "There isn't anything useful for your quest in this room."
		else:
			if searched == False:
				random_response = [
					'Hmm. It looks like there is a %s under a table...' % self.items[0],
					'Wow. There is a %s hanging on the wall!' % self.items[0],
					'Interesting. You find a hidden trap door. Inside is a %s.' % self.items[0],
					'Nothing... Nothing... Oh! Look! A %s!' % self.items[0],
					'Someone left a %s right in the middle of the room.' % self.items[0],
					'You pull back a dusty cloth. Beneath it is a %s.' % self.items[0],
					'There is a massive clay pot. Inside is a %s.' % self.items[0],
					'Someone dressed in a %s costume runs in, sees you, screams,\ndrops a %s and vanishes.' % (random.choice(['gorilla', 'panda', 'ninja', 'bear', 'tiger', 'apricot', 'dorothy', 'lion']), self.items[0]),
				]
				return random_response[random.randint(0, len(random_response) - 1)]
			else:
				if len(self.enemies) >= 1:
					return 'There is a %s here.' % self.enemies[0]
				else:	
					return "You already searched. There is a %s here." % self.items[0]
	
	valid_actions = ['go', 'search room', 'get', 'use', 'check me', 'leave game',]
	
	def verify_action(self, action):
		action = action.strip()
		try:
			verb, obj = action.split(' ', 1)
		except ValueError:
			verb = action
			obj = None
		if verb in VALID_ACTIONS:
			try:
				getattr(self, 'action_%s' % verb)(obj)
			except AttributeError:
				raise ValueError("Invalid action")
		else:
			raise ValueError("Invalid action")

		#action_as_list = action.strip(' ').split(' ')
		#if len(action_as_list) == 1:
		#	if action_as_list[0] == 'go':
		#		raise ValueError("'go'? Um... go where, genius?")
		#	elif action_as_list[0] == 'get' or action_as_list[0] == 'use':
		#		raise ValueError("%r? You have to '%s something'." % (action_as_list[0], action_as_list[0]))
		#	else:
		#		raise ValueError('You cannot %r.' % action)
		#elif len(action_as_list) == 2:
		#	if action_as_list[0] == 'go':
		#		return self.next_room(action_as_list[1])
		#	elif action_as_list[0] == 'get':
		#		return self.get_item(action_as_list[1])
		#		# will return 'get item'
		#	elif action_as_list[0] == 'use':
		#		return self.use_item(action_as_list[1])
		#		# will return 'use item'
		#	elif action_as_list[0] == 'search' and action_as_list[1] == 'room':
		#		return 'search room'
		#	elif action_as_list[0] == 'check' and action_as_list[1] == 'me':
		#		return 'check me'
		#	elif action_as_list[0] == 'leave' and action_as_list[1] == 'game':
		#		return 'leave game'
		#	else:
		#		raise ValueError('You cannot %r.' % action)
		#else:
		#	raise ValueError('You cannot %r.' % action)

Battle(object):
	
	def __init__(self, character, enemy):
		self.character = character
		self.enemy = enemy
		
	enemy_difficulty = DataStore().enemy_difficulty
	
	def enemy_life(self):
		for key, value in enemy_difficulty:
			if self.enemies[0] in value:
				return enemy_difficulty['attack'][value]
			else:
				raise ValueError('Enemy attack value not found!')
				
		self.enemies[0] in enemy_difficulty['easy']:
			return 2
		elif self.enemies[0] in self.medium_enemies:
			return 4
		elif self.enemies[0] in self.hard_enemies:
			return 8
		elif self.enemies[0].lower() == 'gorilla':
			return 12
			
	def enemy_attack(self):
		defense = 0
		if 'shield' in self.character['stuff']:
			defense += 1
		if 'armor' in self.character['stuff']:
			defense += 1
		if self.enemies[0] in self.easy_enemies:
			attack = 2 - defense
		elif self.enemies[0] in self.medium_enemies:
			attack = 3 - defense
		elif self.enemies[0] in self.hard_enemies:
			attack = 4 - defense
		elif self.enemies[0].lower() == 'gorilla':
			attack = 4 - defense
		else:
			raise ValueError('No attack for that enemy was found')
		if attack <= 0:
			return 0
		else:
			return attack
	
	def enemy_stren

	def battle(self, action, prev_hit):
		character_attack = 0
		character_defense = 0
		
		
		enemy_life = self.enemy_life()
		exp_bonus = self.character['experience'] / 3
		if action == 'use fists' or action == 'use lantern':
			hit = (1 + exp_bonus) + prev_hit
		elif action == 'use shield':
			hit = (2 + exp_bonus) + prev_hit
		elif action == 'use sword':
			hit = (3 + exp_bonus) + prev_hit
		else:
			raise ValueError('You cannot %s' % action)
		if enemy_life - hit <= 0:
			return 'enemy dead'
		else:
			return hit


class FunStuff(object):
	
	def names(self, name):
		self.name = name
		if len(name) + 1 == len(name.split(' ')):
			random_names = ['Triage Patient', 'Unbathed Vagrant',
				'Wart', 'Deaf Pigeon', 'Turd', 'Fish Monocle',
				"Hampster's Child", 'Used Hygiene Product',
				'Sleeping Weirdo', 'Obnoxious Tool', 'Too Lazy To Fish', 
				'Derisive Sobriquet', 'Pavid Vermin', 'Coffee Breath', 
				'Dug the Dog', "Gollum's Loin Cloth", 'Barf', 'Pudge', 
				'Urban Poptart', 'Dirty Laundry', 'Colon', 'Scab Eater', 
				'Forever Alone', 'Broken Tail Light', 'Muffin Top', 
			]
			return random_names[random.randint(0, len(random_names) - 1)]
		elif name.lower().replace(' ', '') == 'charliesheen':
			return 'Tiger Blood'
		elif 'dreadpirateroberts' in name.lower().replace(' ', ''):
			print "Holy crap! That's an awesome name!"
			return name
		elif name.lower().replace(' ', '') == 'davidgouldin':
			print 'I would find it a challenge to recall a more generous friend.'
			return name
		else:
			return self.name


