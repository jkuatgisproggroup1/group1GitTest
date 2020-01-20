from tkinter import *
from tkinter import Label
from tkinter import Button
from tkinter import Entry
from tkinter import Tk
import math as math



class RoundDist:
    """docstring for Round Class"""
    def __init__(self, convert):

        self.convert = convert
        self.convert.geometry("525x120")
        self.convert.title("Round Off Tool")
        self.label1 = Label(convert, text="Enter Dist in Meters:", font=( ' Verdana bold', 18))
        self.label2 = Label(convert, text="Converted and Rounded in KM:")
        self.label1.grid(row=0, column=0, padx=0)
        self.convert.config(background="turquoise4")
        self.res = Label(font=(' Verdana ', 16))
        self.res.grid(row=1, column=0, columnspan=3)
        self.convert.entry = Entry(font=( ' Verdana ', 20), width = 10)
        # self.convert.entry.grid(row=0, column=1)
    
def converter():
    metre = float(entry.get())
    kiloMetre = (metre / 1000)
    outKM = int(round(kiloMetre, 0))
    output_label.configure(text = 'Converted To KM: {}'.format(outKM)+ 'KM')
                

#Our tkinter window 
convert = Tk()
w1 = RoundDist(convert)
output_label = Label(font=( ' Verdana ' , 16))
entry = Entry(font=( ' Verdana ', 20), width = 10)
convert_button = Button(text= 'CONVERT' , font=( ' Verdana ' , 16),command = converter)
convert_button.grid(row=0, column=2)
output_label.grid(row=1, column=0, columnspan=3)
entry.grid(row=0, column=1)


if __name__ == "__main__":
    convert.mainloop()
