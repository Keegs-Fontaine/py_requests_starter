import pandas as pd
import sqlite3

FILE_LIST = ["plot", "cond","tree","subplot", "POP_PLOT_STRATUM_ASSGN", "POP_EVAL"]
EVALID = 101901
STATE = "DE"

# setup an in-memory sqlite database for querying
with sqlite3.connect(':memory:') as conn:
    for file in FILE_LIST:
        df = pd.read_csv(f"{STATE}_{file}.csv")
        df.to_sql(file, conn, index=False, if_exists='replace')

    query = "SELECT * from tree where plot = 11 limit 10"

    print(pd.read_sql(query, conn))