import glob
files = glob.glob("*.csv")
for filename in files:
    f = open(filename,"r")
    data = f.read()
    f.close()
    data_new = data.replace("\t",",")
    f = open(filename,"w")
    f.write(data_new)
    f.close()
