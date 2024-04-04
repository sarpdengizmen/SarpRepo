import tkinter as tk
window = tk.Tk()
window.title("Frame Example")
window.config(bg="skyblue")

#Create Frame Widget
left_frame = tk.Frame(window, width=200, height=400)
left_frame.grid(row=0,column=0, padx=10, pady=5)
tk.Label(left_frame, text="Hey Bitches").grid(row=1,column=0,padx=5,pady=5)
tool_bar = tk.Frame(left_frame, bg="purple", width=180, height=185)
tool_bar.grid(row=2, column=0, padx=5, pady=5)
window.mainloop()

