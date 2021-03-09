

"""
Everything: Like a HDL except for everything

Everything is composed of Thing, State, and Action. These are
the fundamental building blocks. Things (subclasses) that are
made from these blocks are concepts/constructions.

Thing:
	Atomic, something that is tangable, may hold information (State),
	and may perform actions (Action).

Qualities: or Aspects/concepts?
	An inhearent quality of a Thing, similar to an interface.
	(I might remove this since Qualities can be things)
	Reasons for this would be:
		If something is burnable then it would have a "Burnable"
		If something can ignite then it would have "Ingiteable"
		We can then define that "Burnable" Things can be
		ignited by "Ingiteable" Things.

	Reasons to not have this:
		We can make a Burnable(Thing) and a Ignitable(Thing)
		then if we want something like Wood(Thing) it would be
		Wood(Burnable) and Matches(Ignitable)

	We might run into an inheratience issue if Igniteable needs
	to check if the other Thing is Burnable... but if it is
	an interface (a non-thing) then perhaps it would be easier

State:
	State of a Thing. States can be enforced and stored by
	either Thing which the information is about. e.g a Position
	construct is enforced, maintained, stored by a World construct.
	Whereas a Hunger construct, which is enforced by a World
	construct can be stored in the Thing that exists in that World.

Action:
	Stuff a Thing can do that can manipulate State of a Thing.
	Actions can depend on which two or more Things are interacting.
	e.g given a Tree(Thing) it can define an Action which requires an
	Axe(Thing) in order to use it.


Basis? Constructed concepts:

*Note that these Constructions and concepts are all Thing

World(Thing):
	A set of rules/laws onto Things which define this World.

Entity(Thing): AKA Player
	The conscious Thing which drives all entropy in World(Thing)

Room(Thing):
	A metaphysical space construct which contains a collection
	of Things

Door(Thing):
	A metaphysical link between two spaces such as Rooms

Item(Thing):
	A metaphysical substance which exists in a container AKA a Room
	but can later be things like inventory/bags


Simulation: (more like implementation)

Setup:
	World will contain 1 thing and at least 1 room.
	For every room added it must somehow connect to the original
	room through the use of doors.

Runtime:
	While the simulation is running a Player can do Actions.
	These Actions are given by the World as a list of Actions
	that each Thing in the same Room is willing to provide.
	
	TODO: This will go on until the Player dies

Implementation:
	Making a Room:
		Make this yourself.
		
		TODO: Do not add Doors yourself, use the World to do this

	Connecting two Rooms with a Door:
		The World will have a helper function to do this.

	Moving between Rooms with Door:
		The World will give the Player a list of "Actions"
		which the Player can execute in order to change Rooms.


"""


class State:
	"""State are managed by other ojects to hold information on a
	current object
	"""

	def __init__(self, manager: object):
		"""State is initalized by the calling object installing the
		State"""

		print("State")

class Action:
	"""Actions is the stuff that Thing can do to change State of Thing
	
	description: str
		What the action is called
	priori: str
		What is said before the action
	posteriori: str
		What is said after the action
	transition: Lambda?
		States that are changed
	"""

	def __init__(self, description: str, priori: str, posteriori: str, act_run):
		self.description = description
		self.priori = priori
		self.posteriori = posteriori

		self.__act_run = act_run

	# Override this
	def act(self):
		"""Change the state"""

		print(self.priori)
		self.__act_run()

	# These are transitions to change State with arg
	# FIXME: sometime
	def update(action, *arg):
		"""Update the value of key with val"""

		# Expect arg to have 2 arguments key and val
		action.__state[arg[0]] = arg[1]
		

class Thing:
	"""Things have States, actions, etc...

	States of a Thing can be owned and managed by other Thing objects
		e.g a World(Thing) can update a State of Player(Thing)
		in order to keep track of which Room(Thing) the Player(Thing)
		is currently in. The Player(Thing) cannot modify the
		State that the World(Thing) put onto Player(Thing)

	Actions 
	"""

	def __init__(self, name: str, des: str):
		self.__actions = list()
		self.name = name
		self.des = des

	def add_action(self, action: Action):
		"""Add an Action to this Thing"""

		self.__actions.append(action)

	def get_actions(self) -> list():
		"""Retrun the list of actions for this Thing"""

		return self.__actions

class Item(Thing):
	"""An Item... for lack of a better understanding"""

	def __init__(self, name: str, des: str):
		super().__init__(name, des)

	def clone(self):
		return Item(self.name, self.des)

	def __str__(self):
		return self.name + ": " + self.des

class Bag(Thing):
	"""A bag can hold items, it's a container for Items(Thing)"""

	def __init__(self, name: str, des: str):
		super().__init__(name, des)
		self.items = list()

	def add_item(self, item: Item):
		self.items.append(item)

	def print_contents(self):
		"""Prints contents of the bag"""
	
		if len(self.items) == 0:
			print("Bag is empty")
		else:
			for item in self.items:
				print(item)
		


class Room(Thing):
	"""Rooms contains Things: player, items, context, and doors"""

	def __init__(self, name: str, des: str, *things: Thing):
		super().__init__(name, des)

		# If things is not given then it defaults to () empty tuple
		self.container = list(things)

		# init the Doors
		self.doors = list()

	def add_thing(self, thing: Thing):
		"""Add a Thing to this room"""

		self.container.append(thing)

	def __str__(self):
		return "Room: %s" % self.name

	def make_door_to(self, room, name: str, des: str="", append_dest_to_name: bool=False, append_dest_to_des: bool=False):
		"""Make a door from self to `room`

		room: Room, The dest room this door will lead to.
		name: str, The name of this Door
		des: str, The description of Door
		append_dest_to_name: bool, (default) False, If True then append the " " + `room.name` to the end of `name`
		append_dest_to_des: bool, (default) False, If True then append the " " + `room.name` to the end of `des`
		"""

		if append_dest_to_name:
			name += " " + room.name

		if append_dest_to_des:
			des += " " + room.name

		self.doors.append(Door(name, des, room))

class Door(Thing):
	"""Connects rooms together"""

	def __init__(self):
		super().__init__("A Door", "A plain and normal looking door.")
		self.dest = None


	def __init__(self, name: str, des: str, dest: Room):
		"""Door

		name: str, name of this door
		des: str, description of this door
		dest: Room, room that this door leads to
		"""

		super().__init__(name, des)
		self.dest = dest

	def __str__(self):
		return "Door to %s" % self.dest.name

class Player(Thing):
	"""Has blocking calls and interface to a user, can take actions"""

	def __init__(self):
		super().__init__("The Entity", "The player")


		self.bag = Bag("Inventory", "Normal looking bag")

		def look_at_bag(bag: Bag):
			return lambda: bag.print_contents()

		self.add_action(Action(
			description="Look through bag",
			priori="You look into your bag",
			posteriori="",
			act_run=look_at_bag(self.bag)
		))

		self.last_command = ""

	def free_will(self, actions: Action):
		"""Player takes an Action of actions"""

		# FIXME: make it better
		num = 0
		for act in actions:
			print(num, ": ", act.description)
			num += 1
		
		print("> ", end="")

		user_input = input()

		# Pressed enter, loop last command
		if len(user_input) == 0:
			if len(self.last_command) == 0:
				return
			actions[int(self.last_command)].act()

		else:
			actions[int(user_input)].act()

			# Record this command
			self.last_command = user_input


class World(Thing):
	"""The world which contains things

	The world is big and has things in it

	player: Player(Entity)
		Is given actions to perform
	
	init_room: Room(Thing)
		The starting point for this world

	It's a specification on how things interact in World
	For example there is a Player(Entity) which can do actions,
	These actions are a list of Actions of Things that are in the
	same room as the Player(Entity).
	"""

	def __init__(self, player: Player):
		super().__init__("The World", "A construct")
		self.__player = player
		self.__rooms = list()

		self.__curr_room = None

	def add_room(self, room: Room, gen_door: bool=True):
		"""Add room to this world
		room: Room, The room to add
		gen_door: bool, (default) True: connect this to the previous room with
			a generic door. False: Do not connect.

		"""

		# If there are no rooms yet then add this as the first room
		if len(self.__rooms) <= 0:
			self.__rooms.append(room)
			self.__curr_room = room
			return

		# Generate a Door for this room to the previous one
		if gen_door:
			self.gen_door(self.__rooms[-1], room)

		# Add this new Room into the rooms
		self.__rooms.append(room)

	def start_world(self):
		"""Init player in the first room"""

		print("World starting...")

		# Check if there is any rooms
		if len(self.__rooms) <= 0:
			print("no rooms to start in! fails.")
			return None

		# Place Player(Thing) in first Room
		self.__rooms[0].add_thing(self.__player)

		print("world start!")

		# For all event entities (only player for now)

		# Generate a list of Actions from Things in the current Room
		while True:
			# Get all things in that Room
			print("\n" + self.__curr_room.name)
			print(self.__curr_room.des)

			# All actions that can be taken
			actions = list()

			# Navagation actions
			for door in self.__curr_room.doors:
				actions += door.get_actions()

			# Actions that this room has
			actions += self.__curr_room.get_actions()
			
			# Actions that Things in this room has
			for t in self.__curr_room.container:
				actions += t.get_actions()

			# Actions that the player has in it's bag
			for i in self.__player.bag.items:
				actions += i.get_actions()

			# Give the player all the Actions
			self.__player.free_will(actions)

	def mv_room(self, new_room: Room, priori: str=None):
		"""Moves room, prints priori if defined"""

		self.__curr_room = new_room

	def gen_door(self, room_a: Room, room_b: Room) -> Door:
		"""Generate a door that connects both rooms"""

		# a -> b and b -> a
		# Assumes that Player is in the priori room
		def move_room(world, new_room):
			return lambda: world.mv_room(new_room)

		room_a.add_action(Action("Move room to " + room_b.des, "You're moving", "You moved", move_room(self, room_b)))

		room_b.add_action(Action("Move room to " + room_a.des, "You're moving", "You moved", move_room(self, room_a)))

	def gen_door_actions(self):
		"""Generates Actions for Doors which are in this World"""

		def move_room(world, new_room, priori):
			return lambda: world.mv_room(new_room, priori)

		# For each of the Rooms
		for r in self.__rooms:
			for d in r.doors:
				d.add_action(Action(
					description=d.name,
					priori=d.des,
					posteriori="",
					act_run=move_room(self, d.dest, d.des)
				))

def main():
	
	# Make the player that will be in the rooms in the world
	my_player = Player()

	# Make the world first
	cbad_world = World(my_player)

	# Make some Rooms for the world
	diego_house = Room(
		name="Deigo's House",
		des="Diego lives here. You smell the pizza that is baking in the oven."
	)
	anna_house = Room(
		name="Anna's House",
		des="Anna lives here with Baba. Baba is outside watching birds and thinking about optics."	
	)
	meow_house = Room(
		name="Meow's House",
		des="Meow lives here. Meow is designing a text game..."
	)

	# Make some items that can exist in the world
	master_pizza = Item(
		name="Pizza",
		des="It's a pretty Pizza... what ever that means..."
	)

	# Make some features
	def make_pizza(player):
		return lambda: player.bag.add_item(master_pizza.clone())

	# Make some of these rooms have cool features
	cook_pizza = Action(
		description="Bake a pretty pizza",
		priori="You bake a pizza",
		posteriori="",
		act_run=make_pizza(my_player)
	)

	# Add the features to the Room
	diego_house.add_action(cook_pizza)

	# Add Doors to the Rooms
	diego_house.make_door_to(
		room=anna_house,
		name="Go to",
		append_dest_to_name=True,
		des="You take the red prius and drive to",
		append_dest_to_des=True
	)
	anna_house.make_door_to(
		room=diego_house,
		name="Go to",
		append_dest_to_name=True,
		des="You take the blue crv and drive to",
		append_dest_to_des=True
	)
	anna_house.make_door_to(
		room=meow_house,
		name="Go to",
		append_dest_to_name=True,
		des="You take the blue crv and drive to",
		append_dest_to_des=True
	)
	meow_house.make_door_to(
		room=anna_house,
		name="Go to",
		append_dest_to_name=True,
		des="You take the red rav4 and drive to",
		append_dest_to_des=True
	)

	# World will add a add these Rooms, but not add a Door
	cbad_world.add_room(diego_house, False)
	cbad_world.add_room(anna_house, False)
	cbad_world.add_room(meow_house, False)

	# We need to world to generate Actions for Doors
	cbad_world.gen_door_actions()

	# Explaination:
		# While Doors exist in Rooms, the world is what
		# determins which Room the Player is in, as such
		# the World must be the one that can cause a Player
		# to move between Rooms given Doors.

		# The World will automatically scan all Rooms for
		# Doors then update the Doors to have the correct
		# Actions which will "move" the Player from Room to Room

	# Start the simulation
	# cbad_world.start_world()

	# import meow_world as mworld

	import yaml
	stream = open('meow_world.yml', 'r')
	mworld = yaml.load(stream, yaml.SafeLoader)

	bplayer = Player()
	bworld = World(bplayer)

	rooms = {
		r['id']: Room(
			name=r['name'],
			des=r['des']
		) for r in mworld['rooms']
	}

	# Generate doors
	for d in  mworld['doors']:
		rooms[d['origin']].make_door_to(
			room=rooms[d['dest']],
			name=d['name'],
			append_dest_to_name=d['append_dest_to_name'],
			des=d['des'],
			append_dest_to_des=d['append_dest_to_des']
		)

	for r in rooms:
		bworld.add_room(rooms[r], False)

	bworld.gen_door_actions()

	bworld.start_world()

if __name__ == "__main__":
	main()
