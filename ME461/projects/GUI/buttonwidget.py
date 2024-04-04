def volUp():
    print('Volume increased by 1')
def volDown():
    print('Volume decreased by 1')

import tkinter as tk

window = tk.Tk()
def turnOn():
    new_window = tk.Toplevel(window,background="blue")
    new_window.title("TV")
    image = tk.PhotoImage(file="~/Downloads/sonic.gif")
    image=image.subsample(2,2) #Uses every 2nd pixel in x y dirs
    
    imagelabel = tk.Label(new_window, image=image)
    imagelabel.image=image
    imagelabel.pack()

onb=tk.Button(window,text="ON", command=turnOn)
onb.pack()

offb=tk.Button(window,text="OFF", command=window.quit)
offb.pack(expand=False)

# Create volume up volume down buttons and pack them
vol_up=tk.Button(window,text="Volume Up",command=volUp)
vol_up.pack()

vol_down=tk.Button(window,text="Volume Down",command=volDown)
vol_down.pack()

window.mainloop()
