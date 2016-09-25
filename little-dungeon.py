from sys import exit

# --------------------------- VARS ---------------------------

beast_alive = True
dragon_alive = True
sword = False

# ------------------------- ROUTINES -------------------------

# ROOM 1

def room_1():
    print "You are in a big room with blood covered walls."
    print "It's really dark and all you can see is three doors."
    print "They lead east, north and west. What do you do?"

    choice = raw_input("> ");

    if "west" in choice:
        room_2()
    elif "north" in choice:
        room_4()
    elif "east" in choice:
        game_over("""You carefully go through the narrow passage heading
east. After walking for three minutes, you see that
it ends with a solid wall. You turn around to get back
but you find yourself facing another wall. Somewhat,
you have trapped youself. Without water nor food, you
die some days later.""")
    else:
        room_1()

# ROOM 2

def room_2():
    print "This room has a really low ceiling and you must crouch to walk."
    print "You see a passage leading west and a passage leading north."
    print "On the far end of the first one, you can see a bright light."
    print "From the second one, a really bad smell emanates."
    print "The passage to the east leads to the first room."
    print "What do you do?"

    choice = raw_input("> ");

    if "west" in choice:
        game_over("""You follow the bright path. As you walk, the light
gets brighter and brighter, until you can't see anything.
Suddenly you can no longer feel the floor under your
feet and, as you fall in a pit of flames, you understand
where the light came from. You die screaming in pain.""")
    elif "north" in choice:
        room_3()
    elif "east" in choice:
        room_1()
    else:
        room_2()

# ROOM 3

def room_3():

    global beast_alive
    global sword

    if beast_alive:
        print "As you walk into the room, you understand where the smell came from."
        print "The floor is littered with rotting corpses."
        print "Suddenly you hear a growl and a huge beast appears in front of you."
        print "You see a passage to the east, a flaming torch on the ground,"
        print "a skeleton holding a sword and a hole on the far side of the room."
        print "The passage to the south leads to the second room."
        print "What do you do?"

        choice = raw_input("> ")

        if "east" in choice:
            game_over("""As you run towards the east passage, the beast leaps
in front of you. You don't have the time to do anything,
because the beast opens its jaws and rips of your head.""")
        elif "torch" in choice:
            print """You take the flaming torch and wave it in front of the
beast. It leaps back in fear, stumbles and falls in the
hole, disappearing from the room."""
            beast_alive = False
            room_3()
        elif "sword" in choice:
            print """You take the sword. Suddenly, it starts emanating a faint
glow and you feel invincible. Without knowing how, you
jump forward and kill the beast."""
            beast_alive = False
            sword = True
            room_3()
        elif "hole" in choice:
            game_over("""You jump in the dark. It wasn't
such a good idea, though. You start falling in the void,
never again hitting a floor. You die days later, still
falling.""")
        elif "south" in choice:
            room_2()
        else:
            room_3()

    else:
        print "The floor is littered with rotting corpses."
        print "You see a passage to the east, a flaming torch on the ground,"
        print "a skeleton holding a sword and a hole on the far side of the room."
        print "The passage to the south leads to the second room."
        print "What do you do?"

        choice = raw_input("> ")

        if "east" in choice:
            room_4()
        elif "torch" in choice:
            print """You take the flaming torch and wave it in the air.
You feel stupid and put it down."""
            room_3()
        elif "sword" in choice:
            print """You take the sword."""
            sword = True
            room_3()
        elif "hole" in choice:
            game_over("""You jump in the dark. It wasn't
such a good idea, though. You start falling in the void,
never again hitting a floor. You die days later, still
falling.""")
        elif "south" in choice:
            room_2()
        else:
            room_3()

# ROOM 4

def room_4():

    global dragon_alive

    if dragon_alive:

        print "The room is huge, and for a good reasons. It is the home of a dragon."

        if sword:
            print """Suddenly your sword starts to glow. Un uknown force urges you to
leap forward and drive the sword in the heart of the dragons.
It dies with horrible screams."""
            dragon_alive = False
            room_4()
        else:
            print "There is a passage to the north, one to the east, one to the"
            print "south and one to the west. What do you do?"

        choice = raw_input("> ")

        game_over("The dragon leaps in front of you and roasts you alive.")

    else:

        print "There is a passage to the north, one to the east, one to the"
        print "south and one to the west. What do you do?"

        choice = raw_input("> ")

        if "east" in choice:
            game_over("""You follow the east passage until you end up in a little
room with a desk and a PC on it. A little fellow is typing
on the PC and suddenly he notices your presence. 'You should
not have found me, the coder of this game!' he says. 'Now
you have to die.' He types something on the PC, and you die.""")
        elif "south" in choice:
            room_1()
        elif "west" in choice:
            room_3()
        elif "north" in choice:
            game_over("""The passage leads to the surface. You are free! You have
won the game!""")
        else:
            room_4()

# START

def start():
    room_1()

# GAME OVER

def game_over(s):

    global beast_alive
    global dragon_alive
    global sword

    beast_alive = True
    dragon_alive = True
    sword = False

    print s
    print "Do you want to play again? (y / n)"

    choice = ""
    while choice != "y" and choice != "n":
        choice = raw_input("> ")
        if choice == "y":

            start()
        elif choice == "n":
            exit(0)


# --------------------------- MAIN ---------------------------

start()
