"""
Entry point of the program. 
"""
from tkinter import *
from tkinter import ttk

        





if __name__ == "__main__":
    # tkinter setup
    
    root = Tk()
    root.title("Mini-Word")
    root.geometry("1280x720")
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=0)
    textbox = Text(root, height = 52, width = 52, font = ('Arial', 16)).grid(column=1,row=1)

    
    while True:
        # get user input (keys)
        
        
        
        # update the backend (storing data)
        
        
        # display to screen
        root.update_idletasks()
        root.update()
    
    
    