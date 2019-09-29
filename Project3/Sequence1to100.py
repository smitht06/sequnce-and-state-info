"""
Anthony Smith
SDEV300
LAB 3
Sequence
"""

#method to create a set with values 0 to 100
def sequence(start, stop):
    listA = list(range(start,stop+1))
    for x in range(len(listA)): 
        listA[x]
    return sorted(set(listA))
    
#method to create set by squaring all values     
def square(list):
    ret =[]
    for i in list:
        ret.append(i ** 2)
    return sorted(set(ret))
    
#method to create set by cubing all values       
def cube(list):
    ret = []
    for i in list:
        ret.append(i ** 3)
    return sorted(set(ret))

#method to display intersection    
def displayIntersection(list1,list2):
    list3  = list1.intersection(list2)
    return list3

#method to display union      
def displayUnion(list1,list2):
    list3 = list1.union(list2)
    return list3

#method to display difference    
def displayDifference(list1,list2):
    list3 = list1.difference(list2)
    return list3
    
#method to search dictionary  
def searchDictionary(x,dic1):
    print(dic1.get(x))

#create list with sequence method    
list1 = sequence(0,100)
#create square and cub sets
sqlist = square(list1)
cubelist = cube(list1)

#combine the numbers and squared and cubed sets into dictionaries 
dict1 = dict(zip(list1,sqlist))
dict2 =dict(zip(list1,cubelist)) 

#initiate option variable
option = 0

"""while loop to orint the menu and 
keep program running until the user enters 6"""
while(option != 6):
    print("""
    1. Display the Square and Cube for Integers ranging from 1 to 100
    2. Search the sets for a specific Integer and display the Square
    and Cube values
    3. Display the Union of Square and Cube sets
    4. Display the Intersection of Square and Cube sets
    5. Display the Difference of Square and Cube sets
    6. Exit the program""")
    #take input from user and assign it to variable option
    option = int(input())

    #if option 1 print 
    if(option == 1):
        print("0-100 squared:")
        print(sqlist,"\n")
        print("0-100 cubed")
        print(cubelist)
    #search dictionary for number input by user    
    elif(option == 2):
        num1 = int(input("enter an integer from 0 to 100 \n"))
        searchDictionary(num1,dict1)
        searchDictionary(num1,dict2)
    #display union    
    elif(option == 3):
        print(sorted(displayUnion(set(sqlist),set(cubelist))))
    #display intersection     
    elif(option == 4):
        print(sorted(displayIntersection(set(sqlist),set(cubelist))))
    #display difference    
    elif(option == 5):
        print(sorted(displayDifference(set(sqlist),set(cubelist))))
    #exit program
    elif(option == 6):
        exit(0)