import tkinter as tk
from tkinter import Menu
import fetalForm
from tkinter.filedialog import askopenfilename


class windows(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("FetA.I.")
        self.iconbitmap("blueLogo.ico")
        
        # menu bar with buttons
        menu_bar = Menu(self)

        file = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label = 'File', menu = file)
        file.add_command(label = 'Exit Program', command = self.destroy)

        menu_bar.add_command(label = 'Home', command=lambda: self.show_frame(HomeScreen))

        upload_button = Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label = 'Upload', menu = upload_button)
        upload_button.add_command(label = 'ML Model', command = self.upload_model)

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

class HomeScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Main Page")
        label.pack(padx=10, pady=10)

        # We use the switch_window_button in order to call the show_frame() method as a lambda function
        switch_window_button = tk.Button(
            self,
            text="Start",
            command=lambda: controller.show_frame(fetalForm.FetalForm),
        )
        switch_window_button.pack(side="bottom", fill=tk.X)

if __name__ == "__main__":
    root = windows()
    root.mainloop()