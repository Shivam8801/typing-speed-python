# Tkinter is a built-in module in Python that allows you
# to create graphical user interfaces (GUIs) using the Tk GUI toolkit.
import tkinter as tk

# In Python, the time module provides functions for working with time-related tasks,
# such as measuring time intervals, pausing the execution of a program,
# and getting the current date and time.
import time

# The threading module in Python provides a way to create and manage threads,
# which are lightweight processes that can run concurrently within a single process.
import threading

# The random module in Python provides a set of functions for generating
# random numbers and other random objects.
import random


class TypeSpeedGUI:

    def __init__(self):

        # Create a window
        self.root = tk.Tk()
        self.root.title("Typing Speed Application")
        self.root.geometry("800x600")

        # Create a list of texts
        self.texts = open("texts.txt", "r").read().split("\n")

        # Create a frame
        self.frame = tk.Frame(self.root)

        # Change the background color of the frame
        self.root.configure(background='skyblue')
        self.frame.configure(background='skyblue')

        # Create a label
        self.sample_label = tk.Label(self.frame, text=random.choice(self.texts), font=("Helvetica", 18), bg='skyblue')
        self.sample_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # Create an entry
        self.input_entry = tk.Entry(self.frame, width=55, font=("Helvetica", 18))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyRelease>", self.start)

        # Create a label
        self.speed_label = tk.Label(self.frame, text="Speed: \n0.00 CPS \n 0.00 CPM \n 0.00 WPS \n 0.00 WPM ",
                                    font=("Helvetica", 18), bg='skyblue')
        self.speed_label.grid(row=2, column=0, columnspan=2, padx=5, pady=10)

        # Create a button
        self.reset_btn = tk.Button(self.frame, text="Reset", command=self.reset, font=("Helvetica", 18))
        self.reset_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

        # Pack the frame
        self.frame.pack(expand=True)

        # Create a variable to store the time
        self.counter = 0

        # Create a variable to control the main loop
        self.running = False

        # Start the main loop
        self.root.mainloop()

    # Create a function to start the timer
    def start(self, event):

        # Start the timer
        if not self.running:
            if event.keycode not in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()

        # Check if the input is correct
        if not self.sample_label.cget('text') == self.input_entry.get():
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")

        if self.input_entry.get() == self.sample_label.cget('text'):
            self.running = False
            self.input_entry.config(fg="green")

    # Create a function to count the time
    def time_thread(self):

        # Count the time
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1

            # Calculate the speed
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            wps = len(self.input_entry.get().split()) / self.counter
            wpm = wps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS \n {cpm:.2f} CPM \n {wps:.2f} WPS \n {wpm:.2f} WPM")

    # Create a function to reset the application
    def reset(self):
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n0.00 CPS \n 0.00 CPM \n 0.00 WPS \n 0.00 WPM")
        self.sample_label.config(text=random.choice(self.texts))
        self.input_entry.delete(0, tk.END)


# Call the class
TypeSpeedGUI()
