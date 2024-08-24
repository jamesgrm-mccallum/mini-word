"""
Entry point of the program. 
"""
import tkinter as tk
from docx import Document


        
def save_to_file() -> None:
    """Takes text from <textbox> and writes it into 
    a .docx and .txt file"""
    text = textbox.get("1.0", tk.END)
    
    document = Document()
    document.add_paragraph(text)
    document.save("text.docx")
    
    with open('text.txt', 'w') as f:
        f.writelines(text)


    
def load_from_file() -> None:
    """Opens <text.txt> and writes it's content into <textbox>"""
    with open('text.txt', 'r') as f:
        text = f.readlines()
        textbox.insert("1.0", '\n'.join(text))
                

if __name__ == "__main__":
    
    root = tk.Tk()
    root.title("Mini-Word")
    root.geometry("1920x1024")
    
    page = tk.Frame(root, background='red')
    page.grid()
    
    
    top_bar = tk.Frame(page)
    top_bar.grid(column=0,row=0)
    top_bar.grid()
    
    
    submitbutton = tk.Button(top_bar, width=10, height=1, text='SAVE', command=save_to_file)
    submitbutton.grid(row=0, column=0)
    insertbutton = tk.Button(top_bar, width=10, height=1, text='LOAD', command=load_from_file)
    insertbutton.grid(row=0, column=1)
    textbox = tk.Text(page, height = 20, width = 20, font = ('Arial', 16))
    textbox.grid(column=0, row=1)
    root.mainloop()
    
    
    