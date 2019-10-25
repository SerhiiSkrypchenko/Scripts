from tkinter import *

from tkinter import messagebox
import testNet2_first_try
import functions
import testNet1

top = Tk()
top.geometry("500x300")
top.title("Instrument for Apollo Loading")
top.wm_minsize(800, 500)

# Gets the requested values of the height and widht.
windowWidth = top.winfo_reqwidth()
windowHeight = top.winfo_reqheight()
#print("Width", windowWidth, "Height", windowHeight)

# Gets both half the screen width/height and window width/height
positionRight = int(top.winfo_screenwidth() / 3 - windowWidth / 2)
positionDown = int(top.winfo_screenheight() / 3 - windowHeight / 2)

# Positions the window in the center of the page.
top.geometry("+{}+{}".format(positionRight, positionDown))

C = Canvas(top, bg="blue", height=250, width=300)
filename = PhotoImage(file = "C:\\Python\\ApolloLogo.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

TestNet1 = Button(top, bd = 3, text="TestNet1", command=functions.showUrls(testNet1.t1), bg ="grey")
TestNet1.place(x=200, y=50)

TestNet2 = Button(top, bd = 3, text="TestNet2", bg ="grey")
TestNet2.place(x=400, y=50)

TestNet3 = Button(top, bd = 3, text="TestNet3", bg ="grey")
TestNet3.place(x=600, y=50)

#L1 = Label(top, text = "Forging")
#L1.pack(x=10, y=50)


#startForgingButton = Button(top, bd = 3, text="Start Forging", command=testNet2_first_try.startForging, bg ="green")
#startForgingButton.place(x=50, y=50)

#stopForgingButton = Button(top, bd = 3, text="Stop Forging", command=testNet2_first_try.stopForging, bg ="red")
#stopForgingButton.place(x=150, y=50)

#startAliasButton = Button(top, bd = 3, text="Start Alias Transactions", command=testNet2_first_try.alias)
#startAliasButton.place(x=50, y=100)



top.mainloop()
