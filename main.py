# our module for this game
from tkinter import *
import random

# make random number for each game
random_num = random.randint(1, 100)

# make m instead of display
m = Tk()
m.configure(bg='lightgreen')
m.title("Guess Win")
m.geometry("900x900")

def service():
    try:
        result = int(Enter.get())
        if result < random_num:
            guide.configure(text="Too low!", foreground="blue", background="lightgreen")
        elif result > random_num:
            guide.configure(text="Too high!", foreground="blue", background="lightgreen")
        else:
            guide.configure(text="You Win!", foreground="white", background="green")
    except ValueError:
        guide.configure(text="Enter a valid number!", foreground="red", background="lightgreen")
        return


Label(m, text="Welcome to this Game", height=2, width=45,
      borderwidth=1, relief="flat") \
    .grid(column=1, row=0, pady=16)

Label(m, text="Number (1 - 100):", bg="lightgreen",
      font=("Helvetica", 12, "bold")) \
    .grid(row=2, column=0, pady=6)

# guide: fixed size, own row below everything
guide = Label(m, text="I am your guide",
              font=("Helvetica", 30, "bold"),
              bg="lightgreen",
              width=20, height=2)
guide.grid(row=4, column=0, columnspan=3, pady=20)

Enter = Entry(m, font=("Helvetica", 12))
Enter.grid(row=2, column=1, sticky="W", pady=4)

check = Button(m, text="Check", height=1, width=39,
               borderwidth=3, relief="groove", command=service)
check.grid(row=3, column=0, columnspan=2, sticky="W", pady=4)

m.mainloop()