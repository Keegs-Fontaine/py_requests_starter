import pandas as pd

FILE_LIST = ["plot", "cond","tree","subplot", "POP_PLOT_STRATUM_ASSGN", "POP_EVAL"]
EVALID = 101901
STATE = "DE"


# This function subsets data based on EVALID and joins with other tables. 
# Check lines 36 - 46 in the R file for reference.
def subset_with_evalid(filelist, conn):
    for file in filelist:
        query = ""
        
        if file == "plot":
            query = f"""
            select ppsaB.CN as ppsaCN, tbl.* from (select * from POP_PLOT_STRATUM_ASSGN ppsa where ppsa.evalid= {EVALID}) ppsaB inner JOIN {file} tbl On tbl.cn = ppsaB.PLT_CN
            """
        else: 
            query = f"""
            select ppsaB.CN as ppsaCN, tbl.* from (select * from POP_PLOT_STRATUM_ASSGN ppsa where ppsa.evalid= {EVALID}) ppsaB inner JOIN {file} tbl On tbl.plt_cn = ppsaB.PLT_CN
            """

        df = pd.read_sql_query(query, conn)
        df.to_sql(file, conn, index=False, if_exists='replace')
