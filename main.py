from tkinter import *

from Book import Book 
from CreateEvent import CreateEvent
from ViewTickets import ViewTickets
from ViewEvents import ViewEvents
from CancelTicket import CancelTicket
from CheckTT import CheckTT
from attendance import cgpa

def open_checktt_dialog():
    CheckTT()
top = Tk()
top.geometry('415x450')
top.title('Event Management System')

Button(top, text='Book Ticket', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: Book()).grid(row=0, column=0, padx=25, pady=30)
Button(top, text='Create Event', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda:CreateEvent()).grid(row=0,pady=25, column=1)
Button(top, text='View Tickets', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda:ViewTickets()).grid(row=1, pady=20, column=0)
Button(top, text='View Events', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda:ViewEvents()).grid(row=1,pady=25, column=1)
Button(top, text='Cancel Ticket', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: CancelTicket()).grid(row=2, pady=25, column=0)
Button(top, text='Attendance', bg='green', fg='white', width=12, font=('Arial', 18),command=lambda:cgpa()).grid(row=2,pady=25,column=1)
Button(top, text='CheckTT', bg='green', fg='white', width=12, font=('Arial', 18),command=lambda:open_checktt_dialog()).grid(row=3, pady=25, column=0)
Button(top, text='Quit App', bg='green', fg='white', width=12, font=('Arial', 18), command=lambda: top.destroy()).grid(row=3,pady=25,column=1)

Label(top, text='Made by ~ Namansh\n22MIA1034', font=('Arial', 12)).grid(row=4, column=0, columnspan=2)
top.mainloop()
