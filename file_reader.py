import pandas as pd
import os

class FileReader:

    def pandas_file_type(*args, **kwds):
        if len(args) == 2:
            name, extension = os.path.splitext(args[1])
            if extension == '.xlsx':
                return pd.read_excel(args[1])
            if extension == '.csv':
                return pd.read_csv(args[1], parse_dates=['Date'])

        elif len(args) == 3:
            return pd.read_sql(args[1],args[2])

 #   def pandas_file_type(self,database, type):
  #      return pd.read_sql_table(database, type)


