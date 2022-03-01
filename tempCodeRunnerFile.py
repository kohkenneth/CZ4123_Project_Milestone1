output results to csv
with open("ScanResults.csv", 'w', newline="") as f:
    headers = ['Date', 'Station', 'Metric', 'Max Value']
    write = csv.writer(f)
    write.writerow(headers)
    write.writerows(results)