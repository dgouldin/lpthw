import models

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
	
	def save_character(self, character_state):
		for key, value in character.items():
			self.character[key] = character_state[key]
	
	character = {'name' : '', 'experience' : 1, 'life' : 7, 'stuff' : ['fists',]}
	
	enemy_difficulty = {
		'easy' : ['walking skeleton', 'angry bush',],
		'medium' : ['evil monkey', 'drunk giant toad',],
		'hard' : ['armed guard', 'sober giant toad',],
		'boss' : ['gorilla',],
		'defense' : {'easy' = 2, 'medium' = 4, 'hard' = 8, 'boss' = 12}
		'attack' : {'easy' = 2, 'medium' = 3, 'hard' = 4, 'boss' = 4}
	}
	
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
			'enemies' : [self.enemy_difficulty['easy_enemies'][0]], 
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
			'enemies' : [self.enemy_difficulty['easy_enemies'][1]], 
			'doors' : ['toast'], 
		},
		'ice' : { 
			'description' : ["Your ice room is nothing more that a giant refrigerator.", 
				"Nothing more? Psh. It's an ENTIRE room that is a", 
				"refrigerator! It's full of all kinds of frozen meats",
				"and liquors you have collected in your world travels.", 
			], 
			'items' : ['shield'], 
			'enemies' : [self.enemy_difficulty['easy_enemies'][0]], 
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
			'enemies' : [self.enemy_difficulty['easy_enemies'][1]], 
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
			'enemies' : [self.enemy_difficulty['medium_enemies'][1]], 
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
			'enemies' : [self.enemy_difficulty['hard_enemies'][1]], 
			'doors' : ['mire', 'morgue', 'cigar'], 
		},
		'morgue' : { 
			'description' : ["You keep dead bodies in the morgue... Psychopath.", 
				"", 
				"Didn't you hire someone to keep people out of this",
				"place?\n", 
			], 
			'items' : [], 
			'enemies' : [self.enemy_difficulty['hard_enemies'][0]], 
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
			'enemies' : [self.enemy_difficulty['boss']], 
			'doors' : ['stairs'], 
		},
	}

