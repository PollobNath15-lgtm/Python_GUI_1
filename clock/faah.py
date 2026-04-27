import tkinter as tk
from time import strftime
import pygame

# pygame audio init
pygame.mixer.init()

def show_time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, show_time)

def play_sound():
    pygame.mixer.music.load("Fahhh.mp3")
    pygame.mixer.music.play(-1)  # -1 মানে loop চলবে

root = tk.Tk()
root.title("Current Time App")
root.geometry("300x220")
root.resizable(False, False)

label = tk.Label(root, font=('Arial', 30), fg='blue')
label.pack(pady=20)

# Clock Start Button
b1 = tk.Button(root, text="Show Clock", command=show_time)
b1.pack(pady=5)

# Clock Start Button
b1 = tk.Button(root, text="Show Clock", command=show_time)
b1.pack(pady=5)

# MP3 Play Button
b2 = tk.Button(root, text="Fahhh", command=play_sound)
b2.pack(pady=5)

root.mainloop()