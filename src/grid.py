from tkinter import *


class GenerateGrid:
    def __init__(self, data_records, second_frame, header_array):
        self.data_records = data_records
        self.second_frame = second_frame
        self.header_array = header_array

    def generate(self):
        rows = []
        for i in range(len(self.header_array)):
            cols = []
            e = Entry(self.second_frame, relief=GROOVE)
            e.grid(row=0, column=i, sticky=NSEW)
            e.insert(END, self.header_array[i])
            cols.append(e)
        rows.append(cols)

        # Insert data into table
        grid_column = len(self.data_records)
        # Restricts grids that are too large.
        if len(self.data_records) > 100:
            grid_column = 100
        for i in range(grid_column):
            cols = []
            for j in range(len(self.data_records.columns)):
                e = Entry(self.second_frame, relief=GROOVE)
                e.grid(row=i + 1, column=j, sticky=NSEW)
                e.insert(END, self.data_records.iat[i, j])
                cols.append(e)
            rows.append(cols)
