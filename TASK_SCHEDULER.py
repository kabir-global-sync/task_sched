from tkinter import *
from tkinter import ttk
import datetime as dt
import sqlite3

count = 0
root = Tk()
root.title('TASK SCHEDULAR')
conn = sqlite3.connect('taskscehduler.db')
cur = conn.cursor()
cur.execute('''
                CREATE TABLE if not exists task(
                ID INT(3),
                Start VARCHAR(25),
                End VARCHAR(25),
                Task text
                )''')
conn.commit()
conn.close()

g_font = ('Lato', 16)
frm_font = ('Franklin Gothic Demi', 12)
myNotebook = ttk.Notebook(root)
myNotebook.pack()

schedular_frm = Frame(myNotebook, width=400, height=400, bg='#ecd348')
schedular_frm.pack(fill='both', expand=1)

start_date_frm = LabelFrame(schedular_frm, text='Start Date', font=frm_font, bg='#ecd348')
start_date_frm.pack(pady=5, padx=5)
lbl1 = ['Day', 'Month', 'Year']
mon={'JAN':1,'FEB':2,'MAR':3,'APR':4,'MAY':5,'JUNE':6,'JULY':7,'AUG':8,'SEP':9,'OCT':10,'NOV':11,'DEC':12}
Label(start_date_frm, text=lbl1[0], font=g_font, bg='black', fg='white').grid(row=0, column=0, ipadx=10,pady=(0, 10))
Label(start_date_frm, text=lbl1[1], font=g_font, bg='black', fg='white').grid(row=0, column=1, ipadx=10,pady=(0, 10))
Label(start_date_frm, text=lbl1[2], font=g_font, bg='black', fg='white').grid(row=0, column=2, ipadx=10,pady=(0, 10))

day_strt_e = Entry(start_date_frm, width=8, justify=CENTER, font=('Lato', 11))
day_strt_e.grid(row=1, column=0, pady=(0, 5), padx=(2, 5))

month_strt_var = StringVar()
month_strt_combobox = ttk.Combobox(start_date_frm, width=10, textvariable=month_strt_var)
month_strt_combobox['values'] = list(mon.keys())
month_strt_combobox['state'] = 'readonly'
month_strt_combobox.grid(row=1, column=1, pady=(0, 5))

year_list = [str(dt.date.today().year + i) for i in range(5)]
year_strt_var = StringVar()
year_strt_var.set(year_list[0])
year_strt_combobox = ttk.Combobox(start_date_frm, width=10, textvariable=year_strt_var)
year_strt_combobox['values'] = year_list
year_strt_combobox['state'] = 'readonly'
year_strt_combobox.grid(row=1, column=2, pady=(0, 5), padx=5)

hrs_list = [str(z) for z in range(1, 13)]
min_list = [str(v) for v in range(0, 61, 5)]

start_time_frm = LabelFrame(schedular_frm, text='Start Time', font=frm_font, bg='#ecd348')
start_time_frm.pack(padx=5, pady=5)

hrs_lbl = Label(start_time_frm, text='HOURS', bg='black', fg='white')
hrs_lbl.grid(row=0, column=0, pady=(0,5), padx=5)

hrs_var = StringVar()
hrs_combobox = ttk.Combobox(start_time_frm, textvariable=hrs_var, width=5)
hrs_combobox['values'] = hrs_list
hrs_combobox['state'] = 'readonly'
hrs_combobox.grid(row=1, column=0)

min_lbl = Label(start_time_frm, text='MINUTES', bg='black', fg='white')
min_lbl.grid(row=0, column=1, pady=(0, 5), padx=5)

minute_var = StringVar()
min_combobox = ttk.Combobox(start_time_frm, textvariable=minute_var, width=5)
min_combobox['values'] = min_list
min_combobox['state'] = 'readonly'
min_combobox.grid(row=1, column=1)

mer_lbl = Label(start_time_frm, text='AM/PM', bg='black', fg='white')
mer_lbl.grid(row=0, column=2, pady=(0,5), padx=5)

mer_var = StringVar()
mer_combobox = ttk.Combobox(start_time_frm, textvariable=mer_var, width=5)
mer_combobox['values'] = ['AM', 'PM']
mer_combobox['state'] = 'readonly'
mer_combobox.grid(row=1, column=2)

end_date_frm = LabelFrame(schedular_frm, text='End Date', font=frm_font, bg='#ecd348')
end_date_frm.pack(pady=5, padx=5)
end_date_list = []
Label(end_date_frm, text=lbl1[0], font=g_font, bg='black', fg='white').grid(row=0, column=0, ipadx=10, pady=(0, 10))
Label(end_date_frm, text=lbl1[1], font=g_font, bg='black', fg='white').grid(row=0, column=1, ipadx=10, pady=(0, 10))
Label(end_date_frm, text=lbl1[2], font=g_font, bg='black', fg='white').grid(row=0, column=2, ipadx=10, pady=(0, 10))

day_end_e = Entry(end_date_frm, width=8, font=('Lato', 11), justify=CENTER)
day_end_e.grid(row=1, column=0, pady=(0, 5), padx=(2, 5))

month_end_var = StringVar()
month_end_combobox = ttk.Combobox(end_date_frm, width=10, textvariable=month_end_var)
month_end_combobox['values'] = list(mon.keys())
month_end_combobox['state'] = 'readonly'
month_end_combobox.grid(row=1, column=1, pady=(0, 5))

year_end_var = StringVar()
year_end_var.set(year_list[0])
year_end_combobox = ttk.Combobox(end_date_frm, width=10, textvariable=year_end_var)
year_end_combobox['values'] = year_list
year_end_combobox['state'] = 'readonly'
year_end_combobox.grid(row=1, column=2, pady=(0, 5), padx=5)

end_time_frm = LabelFrame(schedular_frm, text='End Time', font=frm_font, bg='#ecd348')
end_time_frm.pack(padx=5, pady=10)

hrs_end_lbl = Label(end_time_frm, text='Hours', bg='black', fg='white')
hrs_end_lbl.grid(row=0, column=0, pady=(0, 5), padx=5)

hrs_end_var = StringVar()
hrs_end_combobox = ttk.Combobox(end_time_frm, textvariable=hrs_end_var, width=5)
hrs_end_combobox['values'] = hrs_list
hrs_end_combobox['state'] = 'readonly'
hrs_end_combobox.grid(row=1, column=0,pady=(0,5))

min_end_lbl = Label(end_time_frm, text='Minutes', bg='black', fg='white')
min_end_lbl.grid(row=0, column=1, pady=(0, 5), padx=5)

minute_end_var = StringVar()
min_end_combobox = ttk.Combobox(end_time_frm, textvariable=minute_end_var, width=5)
min_end_combobox['values'] = min_list
min_end_combobox['state'] = 'readonly'
min_end_combobox.grid(row=1, column=1, pady=(0, 5))

mer_end_lbl = Label(end_time_frm, text='AM/PM', bg='black', fg='white')
mer_end_lbl.grid(row=0, column=2, pady=(0,5), padx=5)

mer_end_var = StringVar()
mer_end_combobox = ttk.Combobox(end_time_frm, textvariable=mer_end_var, width=5)
mer_end_combobox['values'] = ['AM', 'PM']
mer_end_combobox['state'] = 'readonly'
mer_end_combobox.grid(row=1, column=2, pady=(0, 5))

task_frm = LabelFrame(schedular_frm, text='Task Description', bg='#ecd348', font=frm_font)
task_frm.pack()

task_e = Entry(task_frm, width=30, font=('Lato', 12))
task_e.pack(pady=(0, 10), padx=10)
##############################################################################
viewer_frm = Frame(myNotebook, width=400, height=400)
viewer_frm.pack(fill='both', expand=1)
# Task viewer area

style = ttk.Style()

style.map('Treeview',
          background=[('selected', 'yellow')],
          foreground=[('selected', 'black')])

tree_frm = Frame(viewer_frm)
tree_frm.pack(pady=10)
tree_scrl = Scrollbar(tree_frm)
tree_scrl.pack(side=RIGHT, fill=Y)
tree = ttk.Treeview(tree_frm, yscrollcommand=tree_scrl.set, height=25)

tree_scrl.config(command=tree.yview)
tree.pack()

tree['columns'] = ('ID', 'Start(Time)', 'End(Time)', 'Task')
tree.column('#0', width=0, stretch=NO)
tree.column('ID', width=50, anchor=CENTER)
tree.column('Start(Time)', width=150, anchor=W, minwidth=150)
tree.column('End(Time)', width=150, anchor=W, minwidth=150)
tree.column('Task', width=200, anchor=W)

tree.heading('ID', text='ID')
tree.heading('Start(Time)', text='Start(Time)')
tree.heading('End(Time)', text='End(Time)')
tree.heading('Task', text='Task')

##############################################################################
tree.tag_configure('evenrow', background='#c0c0c0')
tree.tag_configure('oddrow', background='beige')


def query():
    global count
    conn = sqlite3.connect('taskscehduler.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM task')
    record = cur.fetchall()
    for i in record:
        if count % 2 == 0:
            tree.insert(parent='', index='end', iid=count, values=(i[0], i[1], i[2], i[3]), tags='evenrow')

        else:
            tree.insert(parent='', index='end', iid=count, values=(i[0], i[1], i[2], i[3]), tags='oddrow')
        count += 1
    conn.commit()
    conn.close()


def schedule(sy, sm, sd, shr, smin, smer, ey, em, ed, ehr, emin, emer, tsk):
    global count
    start = str(dt.datetime(int(sy), mon[sm], int(sd), int(shr), int(smin))) + smer
    end = str(dt.datetime(int(ey), mon[em], int(ed), int(ehr), int(emin))) + emer
    conn = sqlite3.connect('taskscehduler.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO task VALUES(:id,:Strt,:End,:Tsk)',
                {
                    'id': count,
                    'Strt': start,
                    'End': end,
                    'Tsk': tsk
                })
    conn.commit()
    conn.close()
    if count % 2 == 0:
        tree.insert(parent='', index='end', iid=count, values=(count, start, end, tsk), tags='oddrow')
    else:
        tree.insert(parent='', index='end', iid=count, values=(count, start, end, tsk), tags='evenrow')
    count += 1
    day_strt_e.delete(0, END)
    day_end_e.delete(0, END)
    year_strt_var.set(year_list[0])
    year_end_var.set(year_list[0])
    month_strt_var.set('')
    month_end_var.set('')
    hrs_var.set('')
    hrs_end_var.set('')
    minute_var.set('')
    minute_end_var.set('')
    task_e.delete(0, END)


set_sched = Button(schedular_frm, text='Schedule Task', font=('Fixedsys', 15), bg='black', fg='white',
                   command=lambda: schedule(year_strt_var.get(), month_strt_var.get(), day_strt_e.get(), hrs_var.get(),
                                            minute_var.get(), mer_var.get(), year_end_var.get(), month_end_var.get(),
                                            day_end_e.get(),
                                            hrs_end_var.get(), minute_end_var.get(), mer_end_var.get(), task_e.get()))
set_sched.pack(ipadx=30,pady=(10,0))


def task_delete():
    global count
    rec = tree.selection()[0]
    conn = sqlite3.connect('taskscehduler.db')
    cur = conn.cursor()
    cur.execute('DELETE from task WHERE oid=' + str(int(rec) + 1))
    conn.commit()
    conn.close()
    tree.delete(rec)
    count -= 1


rec_delete = Button(viewer_frm, text='Delete Task', font=('Fixedsys', 15), bg='black', fg='white', command=task_delete)
rec_delete.pack(pady=(5, 0))
query()
myNotebook.add(schedular_frm, text='Set Task')
myNotebook.add(viewer_frm, text='View Task')
mainloop()
