from urllib.request import urlretrieve
from shared import FILE_LIST, STATE


for file in FILE_LIST:
    url = f"https://apps.fs.usda.gov/fia/datamart/CSV/{STATE}_{file}.csv"
    print(f"Downloading {url}")
    urlretrieve(url, f"{STATE}_{file}.csv")
