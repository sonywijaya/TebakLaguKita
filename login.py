from tkinter import * # Import tkinter

    
class CreditsWindow:
    def __init__(self):
        self.window = Tk() # Create a window
        self.window.title("Tebak Lagu Kita") # Set title
        self.window.geometry('{}x{}'.format(480, 640))

        backdrop = PhotoImage(file="images/credits.png")
        bg = Label(self.window, image=backdrop)
        bg.place(x = 0, y = 0)
        
        btSubmitName = Button(self.window, width = 10, text="Tutup", 
            command = self.quit, bg='#17aadd', fg="white",font = "Calibri 16 bold", bd=0)
        btSubmitName.place(x=184, y=497)

        self.window.protocol('WM_DELETE_WINDOW', self.quit)
        
        self.window.mainloop() 

    def quit(self):
        self.window.destroy()
        
CreditsWindow()
