import models
import data_store

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

