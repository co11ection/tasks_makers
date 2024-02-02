import csv
import time
from datetime import datetime


with open("rows_300.csv", mode="w", newline="") as file_:
    writer = csv.writer(file_)

    for i in range(1, 301):
        sec = time.strftime("%S", time.localtime())
        microsec = time.strftime(datetime.now().microsecond.__str__())
        writer.writerow([i, sec, microsec])
        time.sleep(0.01)
