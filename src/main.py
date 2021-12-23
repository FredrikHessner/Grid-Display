import pandas as pd
from tkinter import *
from src.file_reader import FileReader
from src.grid import GenerateGrid
from src.scrollable_frame import ScrollableFrame

# Read file
file_reader = FileReader()
sales = file_reader.pandas_file_type('c:/xampp/htdocs/grid_display/ghg-emissions.csv')

# Create main frame
main_frame = ScrollableFrame()
# Get the second frame which is encapsulated in the Scrollableframe
second_frame = main_frame.get_second_frame()

# Select simplified view
data = sales.describe()
# Converts header into Array
header_array = data.columns.values.tolist()
header_array.insert(0, "Index")
# Include index in displayed data
res = data.to_records(index=TRUE)
data_records = pd.DataFrame(res.ravel())

# Create grid
grid1 = GenerateGrid(data_records, second_frame, header_array)
grid1.generate()

mainloop()
