def fun(filename):
    print("\nReading From File: \n")
    path = "./4_Data/" + filename
    file = open(path,'r')
    if(file):
        dataRead = file.readlines()
        for line in dataRead:
            print(line)
        file.close()
    else:
        print("File not found")