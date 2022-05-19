import numpy as np
import matplotlib.pyplot as plt 



HOUSE_PRICE_PER_AREA = 7


def getAxisX(X_Axis):

    if X_Axis == 1:
        x = 'transaction date'
    elif X_Axis == 2:
        x = 'house age'
    elif X_Axis == 3:
        x = 'distance to the nearest MRT station'
    elif X_Axis == 4:
        x = 'number of convenience stores'
    elif X_Axis == 5:
        x = 'latitude'
    elif X_Axis == 6:
        x = 'longitude'
    else:
        x = 'unknown'
    return x



def getUserInput():
    
    valid = False   # is the number of selection valid"
    print("House Price of Unit Area Prediction Using Simple Linear Regression") 
    print("==================================================================") 
    print("X1: transaction date")	
    print("X2: house age")	
    print("X3: distance to the nearest MRT station")	
    print("X4: number of convenience stores")	
    print("X5: latitude")	
    print("X6: longitude")
    while not valid:
        userInput = input("Which attribute X your house price prediction is based on (1-6)? >")

        if not userInput.isnumeric():
            print("Please enter a number between 1-6.")
        else:
            attribute = int(userInput)
            if 1 <= attribute <= 6:
                valid = True
            else:
                print("Please enter a number between 1-6.")

    userInput = input("Please enter the {} >".format(getAxisX(attribute) ))
    valid = False
    while not valid:
        
        if not userInput.replace(".","",1).isdigit():
            print("That was not valid input. Please try again.")
            userInput = input("Please enter the {} >".format(getAxisX(attribute) ))
        else:
            value = float(userInput)
            valid = True
        
    return attribute, value

def initChart():
 
    plt.xlabel(getAxisX(x_axis).title())
    plt.ylabel('House Price Of Unit Area')
      
def getData(fileName, x_axis, y_axis):
  
    inputFile = open(fileName)
    rawData = inputFile.readlines()
    rawData.pop(0) #remove the title
    #create a 2d array
    dataPoints = np.zeros( ( len(rawData), 2), dtype=float )
    
    #fill array with data from file
    for i in range(len(rawData)):
        values = rawData[i].split(",")
        dataPoints[i][0] = float(values[x_axis])
        dataPoints[i][1] = float(values[y_axis])
    return dataPoints

def regression(dataPoints):
    
    #calculate line of best fit
    sumX, sumY = dataPoints.sum(0) #sum over rows / get one sum for each column (alternate: use a loop to find sum)

    meanX, meanY = dataPoints.mean(0)
    #OR
    #meanX = sumX/len(dataPoints)
    #meanY = sumY/len(dataPoints)

    diffX = dataPoints[:,0] - meanX #array of xi - meanX
    diffY = dataPoints[:,1] - meanY #array of yi - meanY

    numerator = 0
    denominator = 0
    for i in range(len(dataPoints)):
        numerator += diffX[i] * diffY[i]
        denominator += diffX[i] * diffX[i]

    # calculate m
    slope = numerator/denominator
    # calculate c
    yintercept = meanY - slope*meanX

    #print the equation for the line
    print("The linear regression model based on {} is y = {:.2f}x + {:.2f}".format(getAxisX(x_axis), slope,yintercept))
    #print the result
    print("The predicted house price of unit area based on {} is ${:.2f}".format(getAxisX(x_axis),slope*valueX+yintercept))

    return slope, yintercept

def plotScatter(dataPoints):

    plt.scatter( dataPoints[:, 0], dataPoints[: , 1], c= 'k')

def plotLine(slope, yintercept):
    #get 2 points to draw the line
    x_min = np.min(dataPoints, axis = 0)
    x1 = x_min[0]
    y1 = slope*x1+yintercept
    x_max = np.max(dataPoints, axis = 0)
    x2 = x_max[0]
    y2 = slope*x2+yintercept
    #add a line to the plot - lists are x coords & ycoords - can list many points to be joined
    plt.plot([x1,x2], [y1,y2], lw=2, color='blue')

#Mainline
x_axis, valueX = getUserInput()
initChart()
dataPoints = getData("HousePrice.csv", x_axis, HOUSE_PRICE_PER_AREA)
slope, yintercept = regression(dataPoints)
plotScatter(dataPoints)
plotLine(slope, yintercept)
print("End of Processing.")
    