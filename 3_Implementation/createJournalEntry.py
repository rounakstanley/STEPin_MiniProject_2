def fun(filename):
    print("\nEnter data to be Inputted: \n")
    dataToBeInputted = input()
    path = "./4_Data/" + filename
    file = open(path,'w')
    file.write(dataToBeInputted)
    print("\n____________________\n\nSuccessfully stored the entry!\n____________________\n")
    file.close()