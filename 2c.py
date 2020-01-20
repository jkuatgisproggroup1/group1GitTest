import tkinter as tk

class tabulate:
    def __init__(self, mainw):
        self.mainw = mainw

        #window properties
        mainw.title("Volume")
        mainw.geometry("350x350")

        # intro Label
        self.intro_label = tk.Label(self.mainw, text = "Calculate Volume and Rate of Flow of a swimming pool")
        #legth label and input
        self.a_length = tk.Label(self.mainw, text = "Input Length in metres: ")
        self.a_length.pack()
        self.e_length = tk.Entry(self.mainw)
        self.e_length.pack()
        #width label and Entry
        self.a_width  = tk.Label(self.mainw, text = "Input width in metres: ")
        self.a_width.pack()
        self.e_width = tk.Entry(self.mainw)
        self.e_width.pack()
        #Depth label and Entry
        self.a_depth = tk.Label(self.mainw, text = "Input depth in metres: ")
        self.a_depth.pack()
        self.e_depth = tk.Entry(self.mainw)
        self.e_depth.pack()
        
        #button
        self.button = tk.Button(self.mainw, text = "Calculate", command = self.display)
        self.button.pack()

    def display(self):
        #Save input values
        length = float(self.e_length.get())
        width = float(self.e_width.get())
        depth = float(self.e_depth.get())
        #Calculate volume and convert to litres
        volume = float(length*depth*width)
        volume_l = volume*1000
        #Calculate Rate of flow
        r_o_f = volume_l/2.5
        #show display volume and rate of flow
        o_volume = "The volume is {} Litres".format(volume_l)
        o_r_o_f = "The rate of flow is {} Litres per second".format(r_o_f)
        s_volume = tk.Label(self.mainw, text = o_volume)
        s_volume.pack()
        s_r_o_f = tk.Label(self.mainw, text = o_r_o_f)
        s_r_o_f.pack()

#The main funtion
window = tk.Tk()
w = tabulate(window)
window.mainloop()