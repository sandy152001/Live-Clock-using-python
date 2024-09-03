import tkinter as tk
import time

def update_clock():
    current_time = time.strftime('%H:%M:%S %p')
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)  # Update the clock every second

# Create the main window
window = tk.Tk()
window.title("Live Clock")
window.geometry("400x200")
window.configure(bg='black')

# Create a label to display the time
clock_label = tk.Label(window, font=('arial', 50, 'bold'), bg='black', fg='cyan')
clock_label.pack(anchor='center', pady=20)

# Add a title or description label
title_label = tk.Label(window, text="Current Time", font=('arial', 20, 'bold'), bg='black', fg='white')
title_label.pack(anchor='n')

# Start the clock
update_clock()

# Run the main loop
window.mainloop()
