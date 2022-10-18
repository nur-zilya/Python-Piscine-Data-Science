def read_and_write():
    csv = open("ex01/ds.csv", "r") 
    ds_csv = csv.read()

    csv.close()

    tsv = ""
    quote = 0

    for i in range(len(ds_csv)):
        if ds_csv[i] == '\"':
            quote += 1
        if ds_csv[i] == "," and quote%2== 0:
            tsv +=  "\t"
        else:
            tsv += ds_csv[i]

    tsv_doc = open("ex01/ds.tsv", "w")
    tsv_doc.write(tsv) 

if __name__ == "__main__":
    read_and_write()
