import pandas as pd
from tkinter import *
# Read csv file
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
    e = Entry(relief=GROOVE)
    e.grid(row=0, column=i, sticky=NSEW)
    e.insert(END, headerArray[i])
    cols.append(e)
rows.append(cols)

# Insert data into table
for i in range(len(data_records)):

    cols = []

    for j in range(len(data_records.columns)):

        e = Entry(relief=GROOVE)

        e.grid(row=i+1, column=j, sticky=NSEW)

        e.insert(END, data_records.iat[i,j])
        cols.append(e)


    rows.append(cols)



mainloop()
