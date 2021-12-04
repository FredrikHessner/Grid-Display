import pandas as pd
from tkinter import *
from tkinter import ttk
# Read csv file
root = Tk()

# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)
# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=TOP, fill=BOTH, expand=1)

# Add A Scrollbar To the Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=HORIZONTAL,command=my_canvas.xview)
my_scrollbar.pack(side=BOTTOM, fill=X)
# Configure The Canvas
my_canvas.configure(xscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>',
               lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# Create Another Frame Inside the Canvas
second_frame = Frame(my_canvas)

# Add that New Frame To A Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

sales = pd.read_csv(
  '/home/fredrik/PycharmProjects/GridDisplay/venv/sales_data.csv',
  parse_dates=['Date'])
# Select simplified view
data = sales.describe()
# Converts header into Array
headerArray = data.columns.values.tolist()
headerArray.insert(0, "Index")

# Include index in displayed data
res = data.to_records(index=TRUE)
data_records = pd.DataFrame(res.ravel())

# Insert header into table
rows = []
for i in range(len(headerArray)):
    cols = []
    e = Entry(second_frame, relief=GROOVE)
    e.grid(row=0, column=i, sticky=NSEW)
    e.insert(END, headerArray[i])
    cols.append(e)
rows.append(cols)

# Insert data into table
for i in range(len(data_records)):

    cols = []

    for j in range(len(data_records.columns)):
        e = Entry(second_frame, relief=GROOVE)
        e.grid(row=i+1, column=j, sticky=NSEW)
        e.insert(END, data_records.iat[i,j])
        cols.append(e)

    rows.append(cols)



root.mainloop()
