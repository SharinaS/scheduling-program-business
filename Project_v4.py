'''
Created on Dec 19, 2017

@author: sharina

Version 4 GOAL: Improved organization with menu and tabs, and improved usability with databases using SQL. 
Steps: Build GUI that is small, linking functionality before expanding the size of the GUI, given multiple stores and times. 
Add in classes later, after creating basic idea of GUI. 

Resources:
Notebook - https://docs.python.org/3.1/library/tkinter.ttk.html#notebook
Lynda - Learning Python GUI Programming

'''

import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as mBox
import csv


win = tk.Tk()
win.title("Scheduling Program")

#---------Tab Control (below)-------------------------
#frame for tabs
tabControl = ttk.Notebook(win)

#the various tabs
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='JX')

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='WS')

tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='P70')

#make tabs visible
tabControl.pack(expand=1, fill="both")

#---------Tab Control (above) -------------------------

workdays = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

saturday_shifts = ["05:45-12:00", "07:00-12:00", "12:00-18:00", "18:00-23:00"]
sunday_shifts = ["05:45-12:00", "08:00-12:00", "12:00-17:00", "17:00-22:00"]
monday_shifts = ["04:45-12:00", "08:00-12:00", "12:00-17:00", "17:00-22:00"]
tuesday_shifts = ["04:45-12:00", "08:00-12:00", "12:00-17:00", "17:00-22:00"]
wednesday_shifts = ["04:45-12:00", "08:00-12:00", "12:00-17:00", "17:00-22:00"]
thursday_shifts = ["04:45-12:00", "08:00-12:00", "12:00-17:00", "17:00-22:00"]
friday_shifts = ["05:45-12:00", "07:00-12:00", "12:00-18:00", "18:00-23:00"]

'''tab1 - JX'''

#Frames for days
days = ttk.LabelFrame(tab1, text="Schedule Builder")
days.grid(column=0, row=0, padx=8, pady=4)
 
saturday_frame = ttk.LabelFrame(days, text="Saturday")
saturday_frame.grid(column=0, row=0, padx=8, pady=4)
  
sunday_frame = ttk.LabelFrame(days, text="Sunday")
sunday_frame.grid(column=1, row=0, padx=8, pady=4)
  
monday_frame = ttk.LabelFrame(days, text="Monday")
monday_frame.grid(column=2, row=0, padx=8, pady=4)

tuesday_frame = ttk.LabelFrame(days, text="Tuesday")
tuesday_frame.grid(column=3, row=0, padx=8, pady=4)

#Labels and entry fields for names

#SATURDAY 
for saturday in range(len(saturday_shifts)):
    ttk.Label(saturday_frame, text=saturday_shifts[saturday]).grid(column=0, row=saturday, sticky='W')

entriesSat = []
for entry in range(len(saturday_shifts)):
    entriesSat.append(ttk.Entry(saturday_frame))
    entriesSat[entry].grid(row=entry, column=1)

#SUNDAY   
for sunday in range(len(sunday_shifts)):
    ttk.Label(sunday_frame, text=sunday_shifts[sunday]).grid(column=0, row=sunday, sticky='W')

entriesSun = []
for entry in range(len(sunday_shifts)):
    entriesSun.append(ttk.Entry(sunday_frame))
    entriesSun[entry].grid(row=entry, column=1)

#MONDAY
for monday in range(len(monday_shifts)):
    ttk.Label(monday_frame, text=monday_shifts[monday]).grid(column=0, row=monday, sticky='W')

entriesMon = []
for entry in range(len(monday_shifts)):
    entriesMon.append(ttk.Entry(monday_frame))
    entriesMon[entry].grid(row=entry, column=1)

#TUESDAY
for tuesday in range(len(tuesday_shifts)):
    ttk.Label(tuesday_frame, text=tuesday_shifts[tuesday]).grid(column=0, row=tuesday, sticky='W')

entriesTues = []
for entry in range(len(tuesday_shifts)):
    entriesTues.append(ttk.Entry(tuesday_frame))
    entriesTues[entry].grid(row=entry, column=1)
    

allEntries = entriesSat + entriesSun + entriesMon + entriesTues


#ACTIONS

def clear_names(): 
    for entry in range(len(allEntries)):
        allEntries[entry].delete(0, 'end')
        

def check_conflicts():
    pass
    #===========================================================================
    # if allEntries[0].get() !="":
    #     print("hi")
    #===========================================================================
    #===========================================================================
    # if text_closeJX1.get() !="" and text_openJX2.get() != "" and text_closeJX1.get() == text_openJX2.get(): 
    #         messagebox.showinfo("Checking".format(text_closeJX1.get()))
    #===========================================================================
    #reference section 3 for message boxes in Tkinter file --> Learning Python GUI Programming Lynda

 
def file_save():
    sumNames = [] 
    sumEntries = []
    for entry in range(len(allEntries)):
        sumEntries.append(entry)
        if allEntries[entry].get() !="":
            sumNames.append(entry)
        
    file_saveAnswer = mBox.askyesno("Attention","There are {} entries that are still blank. Are you sure you want to proceed?".
                  format((len(sumEntries) - len(sumNames)))) 
    
    if file_saveAnswer == True:
        with open('schedule_V4.csv', 'w+', newline='') as csv_file:
            fieldnames = ["Employee", "Day", "Store", "Shift"]
            csv_app = csv.DictWriter(csv_file, fieldnames=fieldnames)
            csv_app.writeheader()
            
            #===================================================================
            # if self.text_openJX1.get() != "":
            #     csv_app.writerow({"Day": "Saturday", "Store": "JX", "Shift": "05:45-12:00", 
            #                       "Employee": self.text_openJX1.get().strip()})
            #===================================================================
    
    sumNames = [] 
    sumEntries = []    
    
               

def SQL_save():
    pass


#Control Panel Frame
control_panel = ttk.LabelFrame(tab1, text=" ")
control_panel.grid(column=0, row=1, padx=8, pady=4)

#Buttons to control scheduling actions:
button_clear = ttk.Button(control_panel, text="Clear Names", command=clear_names).grid(column=3, row=0, sticky="W")    
button_conflicts = ttk.Button(control_panel, text = "Check for Conflicts", command=check_conflicts).grid(column=0, row=0, sticky="W")
button_saveToFile = ttk.Button(control_panel, text = "Save Schedule to File", command=file_save).grid(column=2, row=0, sticky="W")
button_saveSQL = ttk.Button(control_panel, text = "Save Schedule to Database", command=SQL_save).grid(column=1, row=0, sticky="W")


'''tab2 - WS'''
days = ttk.LabelFrame(tab2, text="Schedule Builder")
days.grid(column=0, row=0, padx=8, pady=4)

for workday in range(7):
    ttk.Label(days, text=workdays[workday]).grid(column=0, row=workday, sticky='W')

'''tab3 - P70'''
days = ttk.LabelFrame(tab3, text="Schedule Builder")
days.grid(column=0, row=0, padx=8, pady=4)

for workday in range(7):
    ttk.Label(days, text=workdays[workday]).grid(column=0, row=workday, sticky='W')

#----------- Quitting the GUI  ------
def _quit():
    answer = mBox.askyesno('Attention', 
                  'If you quit now, anything not saved will be lost! \nClick No to return to the page you were on. Click Yes to go ahead and quit.')
    if answer == True:
        win.quit()
        win.destroy()
        exit()
        

#----------- Menu Bar----------------
menuBar = Menu(win)
win.config(menu=menuBar)

#1st menu
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label="Save to a File", command=file_save)
fileMenu.add_separator()
fileMenu.add_command(label="Save to a Database")
fileMenu.add_separator()
fileMenu.add_command(label="Quit", command=_quit)
menuBar.add_cascade(label="File", menu=fileMenu)

#2nd menu
def about():
    mBox.showinfo('About', 
                  'Scheduling GUI created using Python and tkinter, with options to save schedule to txt file or to SQL database. Version 4')
    
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label="About", command=about)
menuBar.add_cascade(label="Help", menu=helpMenu)


win.mainloop()