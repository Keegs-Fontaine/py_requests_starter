# FIA Python Requests Starter

A super quick and simple project to request CSV FIA csv files and download them to your current directory

# Installation + Getting Started

I recommend setting up a python venv (but you don't have to):

```bash
python3 venv -m ./.venv
source ./.venv/bin/activate
```

Install Python dependencies:

```bash
pip install -r requirements.txt
```

Run the `fetch_csvs.py` file to download FIA csv files locally

# shared.py

The `shared.py` file contains general constants (the current state, filelist we're working with, evalid) and a `subset` function. The subset function follows from lines 36 to 46 in the CSV R file we were given:

```R
#in this loop, I'm subsetting the tables so that they are only for a given EVALID, which is a set of data that make up a full inventory.
for(fn in filelist[1:5]){ #note that this needs to be edited if you change the filelist -- I'm omitting 5th element (POP_EVAL)
if (fn == "plot") {
strSQL3 = paste("select ppsaB.CN as ppsaCN, tbl.* from (select * from POP_PLOT_STRATUM_ASSGN ppsa where ppsa.evalid= ", EVALID, ") ppsaB inner JOIN ", fn," tbl On tbl.cn = ppsaB.PLT_CN",sep="")
} else {
strSQL3 = paste("select ppsaB.CN as ppsaCN, tbl.* from (select * from POP_PLOT_STRATUM_ASSGN ppsa where ppsa.evalid= ", EVALID, ") ppsaB inner JOIN ", fn," tbl On tbl.plt_cn = ppsaB.PLT_CN",sep="")
}

assign(fn,sqldf(strSQL3))

}

```

I've tried to recreate this as best as possible in Python.

# main.py

The `main.py` file can be used for querying the data using SQL queries, similar to the example we were sent in R. You can use the sqlite library, or the `pd.read_sql_query()` function to do that, and load it as a Pandas dataframe.

# main.ipynb

I've also made a quick jupyter notebook file, if you'd prefer to explore the data that way

# Pandas + Data Querying

I'm mainly using Pandas and its sql functionality to query the data, however if you want to integrate something else (like sql alchemy), you totally can. This is just what works for me!
