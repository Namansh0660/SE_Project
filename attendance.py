import tkinter as tk
from tkinter import messagebox
def cgpa():
    class CheckTTDialog(tk.Toplevel):
        def __init__(self, parent):
            super().__init__(parent)
            self.title("Check Cgpa Dialog")
            self.geometry("300x150")

            tk.Label(self, text="Attendance Check").pack(pady=10,padx=10)

    def check_attendance(cgpa):
        if cgpa >= 9:
            messagebox.showinfo("Attendance Check", "No attendance criteria required.")
        else:
            messagebox.showinfo("Attendance Check", "Please check your attendance using the CheckTT button.")

    def get_cgpa(entry):
        try:
            cgpa = float(entry.get())
            check_attendance(cgpa)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid CGPA.")

    top = tk.Tk()
    top.title('Attendance Checker')

    label = tk.Label(top, text='Enter your CGPA:')
    label.pack(pady=10)

    entry = tk.Entry(top)
    entry.pack(pady=10)

    check_button = tk.Button(top, text='Check Attendance', command=lambda: get_cgpa(entry))
    check_button.pack(pady=10)

    top.mainloop()
