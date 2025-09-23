from urllib.request import urlretrieve

FILE_LIST = ["plot", "cond","tree","subplot", "POP_PLOT_STRATUM_ASSGN", "POP_EVAL"]
STATE = "DE"

for file in FILE_LIST:
    url = f"https://apps.fs.usda.gov/fia/datamart/CSV/{STATE}_{file}.csv"
    print(f"Downloading {url}")
    urlretrieve(url, f"{STATE}_{file}.csv")
