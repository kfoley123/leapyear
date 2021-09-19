# get user to put in the year 
#tell them if this is a leap year or not 
#tell them the next 10 leap years
#modulus (%) checks if something is divisible evenly by something else

print("enter year to see if it is a leap year. Enter 'exit' to quit")

startingYear = 0

while(startingYear != "exit"):
    startingYear = input("enter a year: ")
    if(startingYear == "exit"):
        break

    startingYear =int(startingYear)

    if(startingYear % 4 == 0):
        
        if(startingYear % 100 == 0):
            
            if(startingYear % 400 == 0):
                print("this year is a leap year")
            else:
                print("this is not a leap year")
        else:
            print("this is a leap year")
    else:
        print("this is not a leap year")
