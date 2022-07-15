from room import Room
from character import Enemy,Friend
from rpginfo import RPGInfo
from item import Item

spooky_castle = RPGInfo("The Spooky Castle")
spooky_castle.welcome()
RPGInfo.info()
RPGInfo.author = "Manuel"

kitchen = Room()
kitchen.set_name("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom = Room()
ballroom.set_name("Ballroom")
ballroom.set_description("An empty room with gym weights, mirrors around and wooden floor")
dining_hall = Room()
dining_hall.set_name("Dining hall")
dining_hall.set_description("A large room with ornate golden decorations on every wall")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(ballroom,"west")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Why hello there")
ballroom.set_character(catrina)

cheese = Item()
cheese.set_name("cheese")
cheese.set_description("A large and smelly block of cheese")
ballroom.set_item(cheese)

book = Item()
book.set_name("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

# kitchen.return_name()
# kitchen.describe()
# kitchen.get_details()

# ballroom.return_name()
# ballroom.describe()
# ballroom.get_details()

# dining_hall.return_name()
# dining_hall.describe()
# dining_hall.get_details()

current_room = kitchen
backpack = []

dead = False
while dead == False:
    print("\n")
    current_room.get_details()
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

# Check whether a direction was typed
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
       
    elif command == "fight":
        # You can check whether an object is an instance of a particular
        # class with isinstance() - useful! This code means
        # "If the character is an Enemy"
        if inhabitant is not None and isinstance(inhabitant, Enemy):
            # Fight with the inhabitant, if there is one
            print("What will you fight with?")
            fight_with = input()
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.set_character(None)
                    if Enemy.enemies_to_defeat == 0:
                        print("Congratulations, you have vanquished the enemy horde!")
                        dead = True
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost the fight.")
                    print("That's the end of the game")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to fight with")        

    elif command == "hug":
        if inhabitant is not None:
            if isinstance(inhabitant, Enemy):
                print("I wouldn't do that if I were you...")
            else:
                inhabitant.hug()
        else:
            print("There is no one here to hug :(")

    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
            
    RPGInfo.credits()
            

# from item import Item

# knife = Item()
# knife.set_name("Knife")
# knife.set_description("Old and rusty knife")
# mousepad = Item()
# mousepad.set_name("Mouse pad")
# mousepad.set_description("red and square mousepad")
# glasses = Item()
# glasses.set_name("Glasses")
# glasses.set_description("Scientist glasses with a brown frame")

# knife.return_name()
# knife.describe()

# mousepad.return_name()
# mousepad.describe()

# glasses.return_name()
# glasses.describe()

