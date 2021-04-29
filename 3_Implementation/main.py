from datetime import date
import readJournalEntry
import createJournalEntry
import addToJournalEntry

today = date.today()
filename = today.strftime('%d%m%Y.txt')

while(1):
    print("\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n\n\nWelcome to your Journal. \n\n_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \n\n\n")
    print("What would you like to do?\n\n\n1) Create new Journal Entry for Today (", today,")")
    print("2) Add to existing Journal Entry\n3) Read existing Journal Entry\n4) Exit\n\n\nYour Choice: ")


    choice = input()

    if(choice == "1"):
        createJournalEntry.fun(filename)
    elif(choice == "2" or choice =="3"):
        searchFile = input("\nEnter the date created in the format DDMMYYYY: ")
        searchFile += ".txt"
        if(choice == "2"):
            addToJournalEntry.fun(searchFile)
        elif(choice == "3"):
            readJournalEntry.fun(searchFile)
    elif(choice == "4"):
        print("Thank you")
        break
