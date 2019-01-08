f = open('data.csv','r')
val = f.read()
a = val.split(';')
with open ('value.csv','a') as f1:
    for item in a:
        f1.write("%s\n" %item)
