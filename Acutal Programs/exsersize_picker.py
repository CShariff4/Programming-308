tsv_file = open("example.tsv")
read_tsv = csv. reader(tsv_file, delimiter="\t")
for row in read_tsv:
print(row)
tsv_file. close()

