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

genre = input("You can only pick from these 10 genres :")
g = ['Pop','Rap','Hiphop','R&B','Kpop','Mexican','Country','Jazz','Classical Music','Rock']
print(genre)

def genre():
    
    