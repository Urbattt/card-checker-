from tkinter import* 
from tkinter import messagebox
from PIL import ImageTk, Image

root=Tk()
root.title("card checker")
root.geometry("600x400")
input_box=Entry(root, text = "put credit card pin here")
input_box.pack()

card = ImageTk.PhotoImage(Image.open("card.png"))
cardlabel = Label(root, image = card)
def check():
    try:
        input_value = int(input_box.get())
        messagebox.showinfo("Alert","Credit card accepted.")
    except(ValueError):
        messagebox.showinfo("Error", "Invalid Pin")
            
    
button=Button(root, text="check",command = check)
button.pack()
cardlabel.pack()
root.mainloop()