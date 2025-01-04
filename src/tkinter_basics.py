import tkinter as tk

# Create instance of tkinter
root = tk.Tk()

# Set the title
root.title("Tiffany's Game")

# Set the window size
root.geometry("1280x800")

# Add a label
label = tk.Label(root, text = "Welcome to Tkinter!")
label.pack()

# Add a button
button = tk.Button(root, text = "Click me!")
button.pack()

# Run the application
root.mainloop()