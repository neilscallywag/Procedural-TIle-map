from random import randrange 
def step(x:int,y:int,direction):
    return x+direction[0],y+direction[1]

def validatePosition(array,x:int,y:int)->bool:
    return x>=0 and x< len(array[0]) and y>=0 and y< len(array)

def generateMap(configuration={}):
    default = {
        'numberOfPaths' : 40,
        'minPathLength' : 1,
        'maxPathLength' : 10,
        'maxMapWidth'   : 10,
        'maxMapHeight'  : 10,
        'startPosition' : {'x': -1,
                           'y': -1
                           }
        }
    configuration = configuration if configuration else default

    directions = [
        [-1, 0],
        [1, 0],
        [0, -1],
        [0, 1],
        ]

    #Generate Random X and Y coordinate:
    if ( configuration["startPosition"]["x"] < 0 or configuration["startPosition"]["x"] >= configuration["maxMapWidth"]):
        configuration["startPosition"]["x"] = randrange(0,configuration["maxMapWidth"])
    if ( configuration["startPosition"]["y"] < 0 or configuration["startPosition"]["y"] >= configuration["maxMapHeight"]):
        configuration["startPosition"]["y"] = randrange(0,configuration["maxMapHeight"])

    #Generate Empty Map
    array = []
    for i in range(configuration["maxMapHeight"]+1):
        array.append([])
        for j in range(configuration["maxMapWidth"]+1):
            array[i].append(0)
    #populate Map
    x = configuration["startPosition"]["x"]
    y = configuration["startPosition"]["y"]
    lastdirection = None
    pathLength = None
    direction= None
    #Make the starting coordinates a valid position
    array[x][y] = 1

    for i in range(configuration["numberOfPaths"]+1):
        pathLength = randrange(configuration["minPathLength"],configuration["maxPathLength"])
        #pick random direction
        direction = directions[randrange(0,len(directions))]
        for i in range(pathLength+1):
            tempX,tempY = step(x,y,direction)
            if not validatePosition(array,tempX,tempY):
                break
            else:
                x,y = step(x,y,direction)
                array[y][x] = 1
        lastDirection = direction
    return array


arr = generateMap()
print(*arr, sep="\n")



            
        

    
        
        
        
    

    
