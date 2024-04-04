import tkinter as tk
# Serup the window
window = tk.Tk()
window.title("My First GUI Program")
window.configure(background="yellow")
window.minsize(200,200)
window.maxsize(400,400)
window.geometry("300x300+200+200")
#Create labels
text1 = tk.Label(window, text="Bu ne amk")
text1.pack()
text2 = tk.Label(window, text="Bok gibi program olmus")
text2.pack()
#Insert image
image=tk.PhotoImage(file="~/Downloads/sonic.gif")
img = tk.Label(window, image=image)
img.pack()
window.mainloop()
