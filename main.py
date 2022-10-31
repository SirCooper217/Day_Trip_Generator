import random
greeting = "Hello! Welcome to your Day Trip Generator! Your current Day trip itenerary entails:"
print("")
print(greeting)

def run_day_trip_generator():
    print_full_trip()
    confirm_trip_details()

def print_full_trip():
    print("")
    print("Destination: " + random_dest)
    print("Restaurant: " + random_rest)
    print("Transportation: " + random_trans)
    print("Entertainment: " + random_ent) 
    

dest_list = ['Kakariko Village', 'Besaid Village', 'Clock Town', 'Twilight Town']
rest_list = ['Stardop Saloon', 'Le Grand Bistrot', 'Mos Eisely Cantina', 'Alola Battle Buffet']
trans_list = ['Minecart', 'Teleporter', 'Horseback', "Paraglider"]
ent_list = ['The Drive-In', 'Disneyland', 'The Opera', 'The Fishing Minigame']

random_dest = random.choice(dest_list)
random_rest = random.choice(rest_list)
random_trans = random.choice(trans_list)
random_ent = random.choice(ent_list)

def confirm_trip_details():
    user_choice = input("Are you satisfied with your itenerary? Y or N - ")
    if user_choice == "Y":
        print("Great! You're going to " + random_dest + ", eating at " + random_rest + ", and you'll be arriving by " + random_trans + ". Enjoy your time with " + random_ent +"!")
    elif user_choice == "N":
        reselect_option()
    else:
        print("Input invalid.")
        confirm_trip_details()

def reselect_option():
    to_change = input("What would you like to change? ")
    if to_change.lower() == "destination":
       global random_dest
       dest_list.remove(random_dest)
       random_dest = random.choice(dest_list)
    elif to_change.lower() == "restaurant":
        global random_rest
        rest_list.remove(random_rest)
        random_rest = random.choice(rest_list)
    elif to_change.lower() == "transportation":
        global random_trans
        trans_list.remove(random_trans)
        random_trans = random.choice(trans_list)
    elif to_change.lower() == "entertainment":
        global random_ent
        ent_list.remove(random_ent)
        random_ent = random.choice(ent_list)
    else:
        print("Input invalid")
        reselect_option()
    print_full_trip()
    confirm_trip_details()

run_day_trip_generator()
