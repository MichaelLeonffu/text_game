

# EDL

meows_world = {
	'rooms': [
		{
			'id': 0,
			'name': "Diego's house",
			'des': "Diego lives here. You smell pizza that is baking in the oven."
		},
		{
			'id': 1,
			'name': "Anna's house",
			'des': "Anna lives here with Baba. Baba is outside watching birds and thinking about optics."
		},
		{
			'id': 2,
			'name': "Meow's house",
			'des': "Meow lives here. Meow is designing a text game..."
		}
	],
	'items': [
		{
			'id': 0,
			'name': "Pizza",
			'des': "It's a pretty Pizza... what ever that means..."
		}
	],
	'actions': [

	],
	'doors': [
		{
			'id': 0,
			'origin': 0,	# Diego's house
			'dest': 1,		# Anna's house
			'name': "Go to",
			'append_dest_to_name': True,
			'des': "You take the red prius and drive to",
			'append_dest_to_des': True
		},
		{
			'id': 1,
			'origin': 1,	# Anna's house
			'dest': 0,		# Diego's house
			'name': "Go to",
			'append_dest_to_name': True,
			'des': "You take the blue crv and drive to",
			'append_dest_to_des': True
		},
		{
			'id': 2,
			'origin': 1,	# Anna's house
			'dest': 2,		# Meow's house
			'name': "Go to",
			'append_dest_to_name': True,
			'des': "You take the blue crv and drive to",
			'append_dest_to_des': True
		},
		{
			'id': 3,
			'origin': 2,	# Meow's house
			'dest': 1,		# Anna's house
			'name': "Go to",
			'append_dest_to_name': True,
			'des': "You take the red rav4 and drive to",
			'append_dest_to_des': True
		}
	]
}