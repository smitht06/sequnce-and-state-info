
while(option != 6):
    print("""
    1. Display the Square and Cube for Integers ranging from 1 to 100
    2. Search the sets for a specific Integer and display the Square
    and Cube values
    3. Display the Union of Square and Cube sets
    4. Display the Intersection of Square and Cube sets
    5. Display the Difference of Square and Cube sets
    6. Exit the program""")
    option = int(input())

    if(option == 1):
        print("0-100 squared:")
        print(sqlist,"\n")
        print("0-100 cubed")
        print(cubelist)
    elif(option == 2):
        num1 = int(input("enter an integer from 0 to 100"))
    elif(option == 3):
        print(displayUnion(sqlist,cubelist))
    elif(option == 4):
        print(displyIntersection(sqlist,cubelist))
    elif(option == 5):
        print(displayDifference(sqlist,cubelist))
    elif(option == 6):
        exit(0)
        
        
list1 = sequence(0,100)
sqlist = square(list1)
cubelist = cube(list1)
dict1 = dict(zip(list1,cubelist))
dict2 = dict(zip(list1,sqlist))
print(sqlist)
print("")
print(cubelist)
print("")
print(dict2)

option = 0