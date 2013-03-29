import random

# You create a class because it has a common behavior.

class DataStore(object):

	def get_room(self, room_name):
		# room name is the identifier---a primary key or id
		room_data = self.the_map[room_name]
		# ** expects a dictionary, which it turns into keyword arguments
		room_data['title'] = room_name
		return Room(self.character, **room_data)

	def save_room(self, room):
		# takes an instance of Rooms
		for key in self.the_map[room.title].keys():
			# try to do this using getattr()
			self.the_map[room.title][key] = getattr(room, key)
		for key, value in room.character.items():
			self.character[key] = room.character[key]
	
	character = {'name' : '', 'experience' : 1, 'life' : 7, 'stuff' : ['fists',]}
	
	the_map = {
		'room' : { 
			'description' : ["line1", 
				"line2", 
				"line3", 
			], 
			'items' : [], 
			'enemies' : [], 
			'doors' : [], 
		},
		'main' : {
			'description' : ["It's Tuesday morning, and you are standing in the MAIN",
				"room of your apartment. Your bride is missing.",
				"That damned gorilla must have taken her again.",
			],
			'items' : ['lantern'],
			'enemies' : [],
			'doors' : ['toast', 'armory', 'hallway'],
		},
		'toast' : {
			'description' : ["Ah, the toast room! The only place to get", 
				"toast. The couters are covered with all manner of", 
				"toasters and toaster ovens. In the cabinets are",
				"dozens of different types of bread: white, wheat,",
				"pumpernickel, cinnamon, banana, zucchini... the list",
				"goes on and on. There is a covered dish with soft butter",
				"and the refrigerator is full of all manner of jams and",
				"jellies.",
			], 
			'items' : [], 
			'enemies' : [], 
			'doors' : ['main', 'fire', 'ice'], 
		},
		'hallway' : { 
			'description' : ["You're in your boring hallway.", 
				"It dog-legs to the right at the end where there is a", 
				"door leading to the stairwell.",
			], 
			'items' : [], 
			'enemies' : [], 
			'doors' : ['main', 'stairs'], 
		},
		'armory' : { 
			'description' : ["This is the Armory. You keep all your badass suits", 
				"of armor in here. Your bride hates this room but ", 
				"you don't care because it's awesome.",
			], 
			'items' : ['armor'], 
			'enemies' : ['walking skeleton'], 
			'doors' : ['main', 'treehouse', 'mire'], 
		},
		'fire' : { 
			'description' : ["This is your fire room. You have an entire room dedicated", 
				"to fire. There are fireplaces along every wall. There are", 
				"fireplaces within fireplaces. Manly torches adorn the", 
				"resplendent mantle above each roaring fire.",
				"",
				"It's so f#%*ing hot in here...",
				"",
			], 
			'items' : ['potion'], 
			'enemies' : ['angry bush'], 
			'doors' : ['toast'], 
		},
		'ice' : { 
			'description' : ["Your ice room is nothing more that a giant refrigerator.", 
				"Nothing more? Psh. It's an ENTIRE room that is a", 
				"refrigerator! It's full of all kinds of frozen meats",
				"and liquors you have collected in your world travels.", 
			], 
			'items' : ['shield'], 
			'enemies' : ['walking skeleton'], 
			'doors' : ['toast'],
		},
		'treehouse' : { 
			'description' : ["This is your treehouse room. The room literally opens", 
				"into a single-room treehouse. It's similar to one you", 
				"built when you were a kid but also has all of the ",
				"amazing ameneties you could not bestow on it in the ",
				"days of your youth. You can see your well-kept yard ",
				"outside through the treehouse window.", 
			], 
			'items' : [], 
			'enemies' : ['angry bush'], 
			'doors' : ['armory'], 
		},
		'mire' : { 
			'description' : ["You're in the Mire room. Gross.", 
			], 
			'items' : [], 
			'enemies' : [], 
			'doors' : ['armory', 'labrynth', 'cave'], 
		},
		'labrynth' : { 
			'description' : ["Even though you call this room your 'Labrynth', it is a", 
				"bit of a misnomer. The room does have a hedge maze built", 
				"in it, but it could be solved by a drunk eight year-old.", 
			], 
			'items' : ['sword'], 
			'enemies' : ['drunk giant toad'], 
			'doors' : ['mire'], 
		},
		'cave' : { 
			'description' : ["The cave has one, massive cavern at its center and", 
				"three narrow cave passageways leading out from the", 
				"center. The ground and the walls are all sold granite.",
				"You can't help shouting 'Echo!' and listening to your",
				"voice bounce off the walls around you."
			], 
			'items' : ['potion'], 
			'enemies' : ['sober giant toad'], 
			'doors' : ['mire', 'morgue', 'cigar'], 
		},
		'morgue' : { 
			'description' : ["You keep dead bodies in the morgue... Psychopath.", 
				"", 
				"Didn't you hire someone to keep people out of this",
				"place?\n", 
			], 
			'items' : [], 
			'enemies' : ['armed guard'], 
			'doors' : ['cave'], 
		},
		'cigar' : { 
			'description' : ["Some might call it an unnecessarily-large humidifier,", 
				"but you prefer to call it simply your 'cigar'. The", 
				"sweet smell of tobacco dances across your nostrils", 
				"as you consider its blissful taste and the unavoidable",
				"fact that you'll die of cancer."
			], 
			'items' : ['key'], 
			'enemies' : [], 
			'doors' : ['cave'], 
		},
		'stairs' : { 
			'description' : ["The stairs go up... or down... depending on your", 
				"perspective.", 
			], 
			'items' : [], 
			'enemies' : [], 
			'doors' : ['hallway', 'tower'], 
		},
		'tower' : { 
			'description' : ["Ah! The tower to your magnificent abode. And, sure enough,", 
				"there's that idiot gorillia at the top of it dancing", 
				"like a freakshow in front of your bride and getting",
				"ready to throw barrels at you." 
			], 
			'items' : ['bride'], 
			'enemies' : ['gorilla'], 
			'doors' : ['stairs'], 
		},
	}


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
			self.items.remove(item)
			self.character['stuff'].append(item)
			return 'get %s' % item
		else:
			raise ValueError('There is no %r that you can get.' % item)
			
	def use_item(self, item):	
		if item in self.character['stuff']:
			return 'use %s' % item
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
					return 'There is a %s here. There is a %s here.' % self.enemies[0]
				else:	
					return "You just searched. There is a %s here." % self.items[0]

	VALID_ACTIONS = ['go', ]

	def action_go(self, object=None):
		

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

		action_as_list = action.strip(' ').split(' ')
		if len(action_as_list) == 1:
			if action_as_list[0] == 'go':
				raise ValueError("'go'? Um... go where, genius?")
			elif action_as_list[0] == 'get' or action_as_list[0] == 'use':
				raise ValueError("%r? You have to '%s something'." % (action_as_list[0], action_as_list[0]))
			else:
				raise ValueError('You cannot %r.' % action)
		elif len(action_as_list) == 2:
			if action_as_list[0] == 'go':
				return self.next_room(action_as_list[1])
			elif action_as_list[0] == 'get':
				return self.get_item(action_as_list[1])
				# will return 'get item'
			elif action_as_list[0] == 'use':
				return self.use_item(action_as_list[1])
				# will return 'use item'
			elif action_as_list[0] == 'search' and action_as_list[1] == 'room':
				return 'search room'
			elif action_as_list[0] == 'check' and action_as_list[1] == 'me':
				return 'check me'
			elif action_as_list[0] == 'leave' and action_as_list[1] == 'game':
				return 'leave game'
			else:
				raise ValueError('You cannot %r.' % action)
		else:
			raise ValueError('You cannot %r.' % action)
	
	easy_enemies = ['walking skeleton', 'angry bush',]
	medium_enemies = ['evil monkey', 'drunk giant toad',]
	hard_enemies = ['armed guard', 'sober giant toad',]
	
	def enemy_life(self):
		if self.enemies[0] in self.easy_enemies:
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

	def battle(self, action, prev_hit):
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

def engine():
	
	avail_actions = ['go', 'search room', 'get', 'use', 'check me', 'leave game',]
	name = raw_input("Please enter a character name:\n> ")
	fun_inst = FunStuff()
	if name != fun_inst.names(name):
		name = fun_inst.names(name)
		print "*****\nA wise guy, eh? Your new name is %r.\n*****" % name
	print "Welcome to the game. Commands are: \n* '%s'" % "'\n* '".join(avail_actions)

	data_store = DataStore()
	current_room = 'main'
	data_store.character['name'] = name
	
	while True:
		room = data_store.get_room(current_room)
		# room = Room(**room_data)
		for line in room.enter():
			print line
		print "There are doors to the following rooms:\n%s." % ", ".join(room.doors)
		if len(room.enemies) >= 1:
			prev_hit = 0
			print "There is a %s in the room." % room.enemies[0]
		searched = False
		action = ''
		
		while action.split(' ')[0] != 'go':
			if room.character['life'] <= 0:
				print "\nYou're dead. :-(\n"
				exit(1)
			try:
				action = room.verify_action(raw_input("\nWhat do you want to do?\n> ").lower())
				if action == 'leave game':
					print "Thanks for playing!"
					exit(1)
				elif action == 'check me':
					print 'Your name is %s. Your remaining life is: %s.\nYou have the following items: %s.' % (data_store.character['name'], data_store.character['life'], ", ".join(data_store.character['stuff']))
				elif action == 'search room':
					print room.search_room(searched)
					print "The available doors are: %s" % (", ".join(room.doors))
					searched = True
				elif action.split(' ')[0] == 'get':
					print 'You got the %s!' % action.split(' ')[1]
				elif action.split(' ')[0] == 'use':
					if action.split(' ')[1] == 'potion':
						room.character['life'] += 5
						room.character['stuff'].remove('potion')
						print "You drink the potion. Life is now %s." % room.character['life']
					elif action.split(' ')[1] == 'bride':
						print "\n\nAre you serious? You just saved her from"
						print "a giant gorilla!!!\n\n"
						print "    ...she's gonna let you use her all night long...\n\n"
						exit(1)
					else:
						if len(room.enemies) == 0:
							print "There is nothing to use your %s on." % action.split(' ')[1]
						else:
							if room.battle(action, prev_hit) == 'enemy dead':
								print 'The %s is dead!' % room.enemies[0]
								if room.enemies[0] == 'gorilla':
									print "\n"
									print "*********************************************"
									print '*    You saved your bride and the world.    *'
									print '*         You win. Congratulations.         *'
									print "*********************************************"
									room.enemies.pop(0)
								else:
									room.enemies.pop(0)
									room.character['experience'] += 1
									if room.character['experience'] % 3 == 0:
										print "New experience level reached!"
							else:
								print 'You %s the %s with your %s!' % (random.choice(['pummel', 'hit', 'assail', 'thwomp', 'beat', 'attack', 'smack']),room.enemies[0], action.split(' ')[1])
								prev_hit = room.battle(action, prev_hit)
			except ValueError as e:
				print e
			if len(room.enemies) >= 1:
				room.character['life'] -= room.enemy_attack()
				print "The %s whacks you! Life is at %s." % (room.enemies[0], room.character['life'])
		data_store.save_room(room)
		current_room = action.split(' ')[1]

# instantiate all of the rooms at the beginning
engine()

# MVC - model view controller. Each layer of the program should  be sep
# from the others. Room here models 
