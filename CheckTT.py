import tkinter as tk
from tkinter import filedialog
import openpyxl
from tkinter import messagebox
def CheckTT():
    def read_timetable(file_path):
        workbook = openpyxl.load_workbook(file_path)
        sheet = workbook.active
        timetable = []

        for row in sheet.iter_rows(values_only=True):
            timetable.append(list(row))

        return timetable

    def is_valid_slot(timetable, day, time):
        return timetable[day][time] == 0

    def find_free_slots(timetable, events, day, time, free_slots):
        num_days = len(timetable)
        num_times = len(timetable[0])

        if day == num_days:
            return

        next_day = day
        next_time = time + 1

        if next_time >= num_times:
            next_day = day + 1
            next_time = 0

        if is_valid_slot(timetable, day, time):
            if events[day][time] == 1:
                free_slots.append((day, time))

        find_free_slots(timetable, events, next_day, next_time, free_slots)

    def process():
        timetable_file = file1_entry.get()
        events_file = file2_entry.get()
        if timetable_file == "" or events_file == "":
            messagebox.showerror("Error", "Please select both Excel files")
            return

        timetable = read_timetable(timetable_file)
        events = read_timetable(events_file)

        free_slots = []
        find_free_slots(timetable, events, 0, 0, free_slots)

        result_text.delete(1.0, tk.END)  
        result_text.insert(tk.END, "Free slots:\n")

        for day, time in free_slots:
            result_text.insert(tk.END, f"Time Slot {day}, Day {time}\n")

    root = tk.Tk()
    root.title("Student Event Navigator")
    root.geometry("500x400") 

    root.configure(bg="#ECECEC")  

    file_path1 = tk.StringVar()
    file_path2 = tk.StringVar()
    
    def browse_file1():
        file_path = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
        file1_entry.delete(0, tk.END) 
        file1_entry.insert(0, file_path)

    def browse_file2():
        file_path = filedialog.askopenfilename(filetypes=[('Excel files', '*.xlsx')])
        file2_entry.delete(0, tk.END)  
        file2_entry.insert(0, file_path)



    file1_label = tk.Label(root, text="Select Timetable Excel File:", bg="#ECECEC")
    file1_label.pack()
    file1_entry = tk.Entry(root, textvariable=file_path1)
    file1_entry.pack()
    file1_button = tk.Button(root, text="Browse", command=browse_file1)
    file1_button.pack()

    file2_label = tk.Label(root, text="Select Events Excel File:", bg="#ECECEC")
    file2_label.pack()
    file2_entry = tk.Entry(root, textvariable=file_path2)
    file2_entry.pack()
    file2_button = tk.Button(root, text="Browse", command=browse_file2)
    file2_button.pack()

    process_button = tk.Button(root, text="Process", command=process, bg="#4CAF50", fg="white")
    process_button.pack()

    result_text = tk.Text(root, wrap=tk.WORD, height=10, width=40)
    result_text.pack()

    root.mainloop()
