# To mgive the user a fun experience hearing music and creating playlists
import random
def greet(name):
    print(f"hello",name)
greet("user")


music = input("Would you like to hear music? : ") # Will be asking the user if they want to hear music
if music == "yes":
    print("Great, Let's listen to music") 
elif music == "no":
    print("Come next time :)")
else:
    print("Please respond with 'yes' or 'no' ")

genre = ['Pop','Rap','Hiphop','R&B','Kpop','Mexican','Country','Jazz','Classical Music','Rock']
print(f"Pick from these 10 genres -> ")

for p in genre:
    print( p)

print(f"Anwer with Capital case, For Example -> Rap or R&B")

for genre in genre:
    print(input(f"Which genre would you like to listen to? :"))
    break

def genre():
    if genre == 'Pop':
        print("What artist/ song would you like to listen to?: ")
    elif genre == 'Rap': 
        print("What artist/ song would you like to listen to?: ")
    elif genre == 'Hiphop':
        print("What artist/ song would you like to listen to?: ")
    elif genre == 'R&B':
        print("What artist/ song would you like to listen to?: ")
    elif genre == 'Kpop':
        print("What artist/ song would you like to listen to?: ")
    elif genre == 'Mexican': 
        print("What artist/ song would you like to listen to?: ")
    elif genre == 'Country':
        print("What artist/ song would you like to listen to?: ")
    elif genre == 'Jazz': 
        print("What artist/ song would you like to listen to?: ")
    elif genre == 'Classical Music':
        print("What artist/ song would you like to listen to?: ")
    elif genre == 'Rock':
        print("What artist/ song would you like to listen to?: ")
    else:
        print("please pick from one of the 10 genres given")

    genre()
    