#crazy story 

name = input("hello what is your name?: ")

favorite_animal = input(f"Interesting...{name.title()} what is your favorite animal?: ")
favorite_animal = favorite_animal.replace("my","your")
if "or" in favorite_animal:
    favorite_animal = input("pick one...")
    favorite_animal = favorite_animal.replace("my","your")
else:
    pass
 
place = input(f'If you and a {favorite_animal.title()} were to go on an adventure where would you like to go?: ')
place = place.replace("my","your")
if " or " in place:
    place = input("pick one plz")
else:
    pass

print(f"{name.title()} and {favorite_animal.title()} find a mysterious portal...")

portal_action = input("Do you enter or do you walk away? ")

if portal_action == "enter":
    print(f"You enter {place.upper()}")
elif portal_action == "walk away":
    print(f"the portal dissapears and you live you noramal every day life never to experience adventure")

three_portals = input(f"upon arriving at {place.upper()} three more portals appear...which one do you enter? ")
if three_portals == "one":
    print(f"{name.title()} and {favorite_animal.title()} fell to their doom")
elif three_portals == "1":
    print(f"{name.title()} and {favorite_animal.title()} fell to their doom")
elif three_portals == "portal one":
    print(f"{name.title()} and {favorite_animal.title()} fell to their doom")
elif three_portals == "portal two":
    print(f"{name.title()} and {favorite_animal.title()} arive back home")
elif three_portals == "2":
    print(f"{name.title()} and {favorite_animal.title()} arive back home")
elif three_portals == "two":
    print(f"{name.title()} and {favorite_animal.title()} arive back home")
elif three_portals == "three":
    lamp_action =input(f"{name.title()} and {favorite_animal.title()} you reappear at {place.title()} but with a mysterious lamp...what do you do? ")
elif three_portals == "3":
    lamp_action =input(f"{name.title()} and {favorite_animal.title()} you reappear at {place.title()} but with a mysterious lamp...what do you do? ")
elif three_portals == "portal three":
    lamp_action =input(f"{name.title()} and {favorite_animal.title()} you reappear at {place.title()} but with a mysterious lamp...what do you do? ")
else:
    print("nothing happens...")



