"""E"""
import tkinter as tk
from tkinter import simpledialog

class mainwindow:
    def __init__(self, mainw):
        self.mainw = mainw
        #window properties
        mainw.title("Speed")
        mainw.geometry("250x250")
        #intro label
        self.i_l = tk.Label(self.mainw, text = "A program to calculate speed(Km/h)")
        self.i_l.pack()
        #ask disatnce label & distance Entry
        self.d_label = tk.Label(self.mainw, text = "Input distance(Km)")
        self.d_label.pack()
        self.d_entry = tk.StringVar()
        self.distance = tk.Entry(self.mainw, textvariable = self.d_entry)
        self.distance.pack()
        #ask time label & time input
        self.t_label = tk.Label(self.mainw, text = "Input Time(hours)")
        self.t_label.pack()
        self.t_entry = tk.StringVar()
        self.time = tk.Entry(self.mainw, textvariable = self.t_entry)
        self.time.pack()
        #show speed label and speed display Entry
        self.o_speed = tk.StringVar() 
        self.s_speed = tk.Entry(self.mainw, textvariable = self.o_speed)
        self.s_speed.pack()
        #button
        self.button2 = tk.Button(self.mainw, text = "Show Speed", command = self.show_s)
        self.button2.pack()
        
        
        
#function to configure the s_entry widget to display speed
    def show_s(self):
        #converting input to integers to enable for calculation
        t = int(self.time.get())
        d = int(self.distance.get())
        speed = float(d/t)
        #settiing the s_speed entry box to show the speed
        self.o_speed.set("Speed is {} Km/h".format(speed))
        
        

#main function
main_window = tk.Tk()
m = mainwindow(main_window)
main_window.mainloop()
