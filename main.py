import pandas as pd
import sqlite3
from shared import FILE_LIST, subset_with_evalid, STATE

# setup an in-memory sqlite database for querying
with sqlite3.connect(':memory:') as conn:
    for file in FILE_LIST:
        df = pd.read_csv(f"{STATE}_{file}.csv")
        df.to_sql(file, conn, index=False, if_exists='replace')

    df = subset_with_evalid(FILE_LIST[0:4], conn)

    # Example query to check data
    example_query = "select * from plot"
    print(pd.read_sql_query(example_query, conn).columns)

    # You can add your own queries here to explore the data
