"""
Anthony Smith
SDEV300
LAB 3
State Info
"""
import pprint

#list of states, capitals, flowers and birds
states = [
"Alabama",
"Alaska",
"Arizona",
"Arkansas",
"California",
"Colorado",
"Connecticut",
"Florida",
"Georgia",
"Hawaii",
"Idaho",
"Illinois",
"Indiana",
"Iowa",
"Kansas",
"Kentucky",
"Louisiana",
"Maine",
"Tennessee",
"Maryland",
"Delaware",
"Massachusetts",
"Rhode Island",
"Minnesota",
"Mississippi",
"Missouri",
"Michigan",
"Montana",
"Nebraska",
"Nevada",
"New Hampshire",
"Vermont",
"New Jersey",
"New Mexico",
"New York",
"North Carolina",
"Wyoming",
"North Dakota",
"Ohio",
"Oklahoma",
"Oregon",
"Pennsylvania",
"South Carolina",
"South Dakota",
"Texas",
"Utah",
"Virginia",
"Washington",
"West Virginia",
"Wisconsin"]

capitals = [
"Montgomery",
"Juneau",
"Phoenix",
"Little Rock",
"Sacramento",
"Denver",
"Hartford",
"Tallahassee",
"Atlanta",
"Honolulu",
"Boise",
"Springfield",
"Indianapolis",
"Des Moines",
"Topeka",
"Frankfort",
"Baton Rouge",
"Augusta",
"Nashville",
"Annapolis",
"Dover",
"Boston",
"Providence",
"St. Paul",
"Jackson",
"Jefferson City",
"Lansing",
"Helena",
"Lincoln",
"Carson City",
"Concord",
"Montpelier",
"Trenton",
"Santa Fe",
"Albany",
"Raleigh",
"Cheyenne",
"Bismarck",
"Columbus",
"Oklahoma City",
"Salem",
"Harrisburg",
"Columbia",
"Pierre",
"Austin",
"Salt Lake City",
"Richmond",
"Olympia",
"Charleston",
"Madison"
    ]

flowers = [
"Camellia",
"Forget-me-not",
"Suguaro Cactus Blossom",
"Apple Blossom",
"Golden Poppy",
"Mountain Columbine",
"Mountain Laurel",
"Orange Blossom",
"Cherokee Rose",
"Red Hibiscus",
"Syringa",
"Violet",
"Peony",
"Wild Rose",
"Sunflower",
"Goldenrod",
"Magnolia",
"Pine Cone & Tassel",
"Iris",
"Black-eyed Susan",
"Peach Blossom",
"Mayflower",
"Violet",
"Lady-slipper",
"Magnolia",
"Hawthorn",
"Apple Blossom",
"Bitterroot",
"Goldenrod",
"Sagebrush",
"Purple Lilac",
"Red Clover",
"Violet",
"Yucca",
"Rose",
"Flowering Dogwood",
"Indian Paintbrush",
"Prairie Rose",
"Scarlet Carnation",
"Mistletoe",
"Grape",
"Mountain Laurel",
"Yellow Jessamine",
"Pasqueflower",
"Bluebonnet",
"Sego Lily",
"Dogwood",
"Coast Rhododendron",
"Rhododendron",
"Wood Violet"]


birds = [
"Yellowhammer",
"Willow Ptarmigan",
"Cactus Wren",
"Mockingbird",
"California Valley Quail",
"Lark Bunting",
"Robin",
"Mockingbird",
"Brown Thrasher",
"Nene (Hawaiian Goose)",
"Mountain Bluebird",
"Cardinal",
"Cardinal",
"Eastern Goldfinch",
"Western Meadowlark",
"Cardinal",
"Eastern Brown Pelican",
"Chickadee",
"Mockingbird",
"Baltimore Oriole",
"Blue Hen Chicken",
"Chickadee",
"Rhode Island Red",
"Loon",
"Mockingbird",
"Bluebird",
"Robin",
"Western Meadowlark",
"Western Meadowlark",
"Mountain Bluebird",
"Purple Finch",
"Hermit Thrush",
"Eastern Goldfinch",
"Road Runner",
"Bluebird",
"Cardinal",
"Meadowlark",
"Meadowlark",
"Cardinal",
"Scissor-tailed Flycatcher",
"Western Meadowlark",
"Ruffed Grouse",
"Carolina Wren",
"Ring-necked Pheasant",
"Mockingbird",
"Sea Gull",
"Cardinal",
"Willow Goldfinch",
"Cardinal",
"Robin"
    ]

#method to search dictionary
def searchDictionary(x,dic1):
    return dic1.get(x)

#combine lists to a dictionary
stateInfo = dict(zip(states, zip(capitals, flowers, birds)))

#set option to 0
option = 0;

#while loop to keep program running until user enters 0
while(option != 4):
    print("""
     1. Display all U.S. States in Alphabetical order along with
        Capital and Flower
     2. Search for a specific state and display the appropriate
        Capital Bird and Flower
     3. Update a Bird for a specific state
     4. Exit the program""")
     #take input from user and assign it to option
    option = int(input("Please make a selection: "))
    
    #pretty print the dictionary if user enters 1
    if(option == 1):
        pprint.pprint((stateInfo))
    #search for state and return bird, flower and capital
    elif(option == 2):
        state = input("enter a state(Please capitlaize first letter): \n")
        print("")
        print(state + " State flower and Bird:")
        print(searchDictionary(state,stateInfo))
    #search state and update the bird of that state then print it back to user    
    elif(option == 3):
        state2 = input("Enter a state you want to update the bird of: ")
        a = searchDictionary(state2,stateInfo)
        print(a)
        updatedBird = input("Enter the new state bird: ")
        stateInfo.update({state2 : {a[0],a[1],updatedBird}})
        print(stateInfo[state2])
    
       