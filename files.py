
fname = input("enter the filename:")
try:
    fhandle = open("data/"+fname)
except:
    print("File with name :", fname, "not found")
    quit()

for line in fhandle:
    line  = line.rstrip()
    if "From" in line:
        print(line)