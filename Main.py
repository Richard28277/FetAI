import tkinter as tk
from tkinter import *
import fetalForm
from tkinter.filedialog import askopenfilename


class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("FetA.I.: A Novel Fetal Health Classification Program Using Soft Voting with Deep and Ensemble Learning")
        self.iconbitmap("blueLogo.ico")
        
        # menu bar with buttons
        menu_bar = Menu(self)

        file = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'Exit Program', command = self.destroy)

        win = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label = 'Window', menu = win)
        win.add_command(label = 'Home Screen', command = lambda: self.show_frame(HomeScreen))
        win.add_command(label = 'Input Field', command = lambda: self.show_frame(fetalForm.FetalForm))

        upload_button = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label = 'Upload', menu = upload_button)
        upload_button.add_command(label = 'Classification Model', command = self.upload_model)

        self.config(menu = menu_bar) # config menu bar onto window

        # container for scene - creating a frame and assigning it to container
        container = tk.Frame(self, height=600, width=600)
        # specifying the region where the frame is packed in root
        container.pack(side="bottom", fill="both", expand=True)

        # configuring the location of the container using grid
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # We will now create a dictionary of frames
        self.frames = {}
        # Add all frames to the loop 
        for F in (HomeScreen, fetalForm.FetalForm):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Using a method to switch frames
        self.show_frame(HomeScreen)

    def show_frame(self, cont):
        frame = self.frames[cont]
        # raises the current frame to the top
        frame.tkraise()

    def upload_model(self):
        name = askopenfilename()
        # print("--------------------------Model name-----------------------------" + name)
        fetalForm.FetalForm.set_ml_model(name)
        self.wm_title("FetA.I.: " + name)

class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="FetA.I: Fetal Health Classification", font=("Arial", 25))
        label.pack(padx=10, pady=110)

        author = tk.Label(self, text="Authors: Richard Xu, Yifu Zuo", font=("Arial", 14))
        author.pack(padx=10, pady=0)

        # Creates a start window button for the welcome screen
        switch_window_button = tk.Button(
            self,
            text="Start",
            command=lambda: controller.show_frame(fetalForm.FetalForm),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

if __name__ == "__main__":
    root = windows()
    root.mainloop()