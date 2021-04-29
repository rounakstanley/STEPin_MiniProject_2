def fun(filename):
    path = "./4_Data/" + filename
    file = open(path,'a')
    if(not file):
        print("File not found")
        return
    print("\nEnter data to be Inputted: \n")
    dataToBeInputted = input()
    file.write(" ")
    file.write(dataToBeInputted)
    print("\n____________________\n\nSuccessfully stored the entry!\n____________________\n")
    file.close()