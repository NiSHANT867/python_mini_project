
import tkinter as tk
from tkinter import messagebox
import datetime
import time


def set_reminder():
    reminder_text = reminder_entry.get()
    date = date_entry.get()
    time = time_entry.get()

    try:
        reminder_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        reminder_time = datetime.datetime.strptime(time, "%I:%M %p").time()

        reminder_datetime = datetime.datetime.combine(reminder_date.date(), reminder_time)

        current_datetime = datetime.datetime.now()

        if reminder_datetime < current_datetime:
            messagebox.showerror("Error", "Invalid date and time. The reminder should be set for a future date and time.")
            return

        time_difference = (reminder_datetime - current_datetime).total_seconds()

        # Saving the reminder
        reminders.append((reminder_datetime, reminder_text))
        reminders.sort(key=lambda x: x[0])

        # Setting Time of the reminder
        root.after(int(time_difference * 1000), display_reminder, reminder_text)

        update_listbox()

    except ValueError:
        messagebox.showerror("Error", "Invalid date or time format. Please use the correct format (YYYY-MM-DD and HH:MM AM/PM).")

def delete_reminder():
    selected_index = reminders_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        if 0 <= index < len(reminders):
            reminders.pop(index)
            update_listbox()

def update_listbox():
    reminders_listbox.delete(0, tk.END)
    for reminder_datetime, reminder_text in reminders:
        reminders_listbox.insert(tk.END, f"{reminder_datetime.strftime('%Y-%m-%d %I:%M %p')}: {reminder_text}")

def display_reminder(reminder_text):
    messagebox.showinfo("Reminder", reminder_text)

def check_reminders():
    while True:
        current_datetime = datetime.datetime.now()
        for reminder_datetime, reminder_text in reminders[:]:
            if reminder_datetime <= current_datetime:
                display_reminder(reminder_text)
                reminders.remove((reminder_datetime, reminder_text))
        time.sleep(60)  




root = tk.Tk()
root.title("Reminder App")


# Label and Entry  for reminder 
reminder_label = tk.Label(root, text="Reminder:")
reminder_label.pack()
reminder_entry = tk.Entry(root, width=40)
reminder_entry.pack()


# Label and Entry for date
date_label = tk.Label(root, text="Date (YYYY-MM-DD):")
date_label.pack()
date_entry = tk.Entry(root, width=20)
date_entry.pack()

# Label and Entry  for time
time_label = tk.Label(root, text="Time (HH:MM AM/PM):")
time_label.pack()
time_entry = tk.Entry(root, width=20)
time_entry.pack()

# Set Reminder button
set_button = tk.Button(root, text="Set Reminder", command=set_reminder)
set_button.pack()

# Listbox to display reminders
reminders_listbox = tk.Listbox(root, height=10, width=50)
reminders_listbox.pack()

# A list to store the reminders 
reminders = []

# Delete Reminder button
delete_button = tk.Button(root, text="Delete Reminder", command=delete_reminder)
delete_button.pack()


root.mainloop()


