import tkinter as tk
import os
import subprocess

# List your apps and their paths here
apps = {
    "App 1": "C:/Path/To/App1.exe",
    "App 2": "C:/Path/To/App2.exe",
    "App 3": "C:/Path/To/App3.exe",
    "App 4": "C:/Path/To/App4.exe",
    "App 5": "C:/Path/To/App5.exe",
    "App 6": "C:/Path/To/App6.exe",
    # Add more apps as needed
}

def launch_app(app_path):
    try:
        subprocess.Popen(app_path)
    except Exception as e:
        print(f"Error launching app: {e}")

# Create the main window
root = tk.Tk()
root.title("My App Launcher")
root.geometry("300x300")  # Adjust the window size as needed

# Create a Canvas widget for scrolling
canvas = tk.Canvas(root)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar and attach it to the Canvas
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the Canvas to hold the buttons
frame = tk.Frame(canvas)

# Create a window in the canvas for the frame
canvas.create_window((0, 0), window=frame, anchor="nw")

# Add a label to describe the app list
label = tk.Label(frame, text="Select an App to Launch", font=("Arial", 14))
label.pack(pady=10)

# Add buttons for each app
for app_name, app_path in apps.items():
    button = tk.Button(frame, text=app_name, width=20, command=lambda app_path=app_path: launch_app(app_path))
    button.pack(pady=5)

# Update the scrollable region of the canvas
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Start the Tkinter event loop
root.mainloop()
