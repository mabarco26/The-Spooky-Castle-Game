from character import Enemy

dave = Enemy("Dave", "A smelly zombie!")
dave.describe()

dave.set_conversation("How you doin' dude? ")
dave.talk()

print("What will you fight with?")
dave.set_weakness("cheese")
fight_with = input()
dave.fight(fight_with)

# action = input("Do you want to talk with Dave? 1.Yes or 2.No: ")

# if action == "1":
#     talking = input("what do you wanna say?: ")
#     dave.set_conversation(talking)
#     dave.talk()
# else:
#     action == "2"
#     print("...braaaaaiiiinnnnnnsss....")



