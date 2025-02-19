# from tkinter import*
# import os # is used to read the foldere and the content within it
# import pygame # has a function that can be used to start and stop the music from playing

# root = Tk()
# root.title('Music Player')
# root.geometry("500x300")

# pygame.mixer.init()


# menubar = Menu(root)
# root.config(menu=menubar)

# organise_menu= Menu(menubar, tearoff=False)
# organise_menu.add_command(Label='Select Fold')
# menubar.add_cascade(Label='Organise', menu=organise_menu)


# songlist = Listbox(root, bg='black', fg="white", width=100, height=15)
# songlist.pack()

# play_btn_image = PhotoImage(file='play.png')
# pause_btn_image = PhotoImage(file='pause.png')
# next_btn_image = PhotoImage(file='next.png')
# back_btn_image = PhotoImage(file='backwards.png')

# control_frame= Frame(root)
# control_frame.pack()

# play_btn = Button(control_frame, image=play_btn_image, border=0)
# pause_btn = Button(control_frame, image=pause_btn_image, border=0)
# next_btn = Button(control_frame, image=next_btn_image, border=0)
# back_btn = Button(control_frame, image=back_btn_image, border=0)

# # play_btn.grid(row=0, column=1, padx=7, pady=10)
# pause_btn.grid(row=0, column=2, padx=7, pady=10)
# next_btn.grid(row=0, column=3, padx=7, pady=10)
# back_btn.grid(row=0, column=0, padx=7, pady=10)


# root.mainloop()

#-----------------------------------------------------------------------------------------------------------

# def greet(name):
#     print(f"hello",name)
# greet("user")

# music = input("Would you like to hear music? : ") # Will be asking the user if they want to hear music
# if music == "yes":
#     print("Great, Let's listen to music") 
# elif music == "no":
#     print("Come next time :)")
# else:
#     print("Please respond with 'yes' or 'no' ")

# genre = ['Pop','Rap','Hiphop','R&B','Kpop','Mexican','Country','Jazz','Classical Music','Rock']
# print(f"Pick from these 10 genres -> ")

# for p in genre:
#     print( p)

# print(f"Anwer with Capital case, For Example -> Rap or R&B")

# for genre in genre:
#     print(input(f"Which genre would you like to listen to? :"))
#     break
# else:
#     print("Have a good day")

# def p (genre):
#     if genre == "Rock":
#         print()