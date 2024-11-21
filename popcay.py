# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 10:04:42 2024

@author: user
"""

import tkinter as tk
from PIL import Image,ImageTk
def update_count():
    global click_count
    click_count+=1
    count_label.config(text=f"點擊次數:{click_count}")
    
    
def on_click(event):
    people_label.config(image=open_mouth_image)
    window.after(200,lambda:people_label.config(image=closed_mouth_image))
    update_count()
    
    
def reset_count():
    global click_count
    click_count=0
    count_label.config("text=點擊次數:0")
    

window=tk.Tk()
window.title("Popcat 點擊遊戲")
window.geometry("400x200")
window.resizable(False,False)



closed_mouth_image=ImageTk.PhotoImage(Image.open("aa.png").resize((100,100)))
open_mouth_image=ImageTk.PhotoImage(Image.open("bb.png").resize((100,100)))

people_label=tk.Label(window,image=closed_mouth_image)
people_label.pack(pady=20)

count_label=tk.Label(window,text="點擊次數:0",font=("Arial,18"))
count_label.pack(pady=20)


click_count=0

people_label.bind("<Button-1>",on_click)


    
reset_button=tk.Button(window,text="重置",command=reset_count,font=("Arial",14),bg="lightblue")
reset_button.pack(pady=10)

window.mainloop()