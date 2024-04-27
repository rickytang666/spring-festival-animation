# Author: Ricky Tang is a pig
# Title: New Year Festival
# Purpose: Create a cool animation describing a new year night scenary. People are driving on the street and playing in the plaza
#          They are also sending lanterns to the sky. When the clock strikes at 12 am, they are happy and they raise their arms. They send off fireworks with different types

#Importing libraries
from tkinter import*
from time import*
from math import*
from random import*

#Initialize the screen
myInterface = Tk()
WIDTH = 900
HEIGHT = 900
screen = Canvas(myInterface, width = WIDTH, height = HEIGHT, background = "black")
screen.pack()

#Draw roads (Static, not in the animation)
def draw_roads(screen):
    #Plaza
    screen.create_rectangle(0, HEIGHT - 300, WIDTH, HEIGHT - 150, fill = "LightGoldenrod4", outline = "LightGoldenrod4")
    #Road
    screen.create_rectangle(0, HEIGHT - 150, WIDTH, HEIGHT, fill = "gray25", outline = "gray25")
    
    i = 0
    while 100 * i <= WIDTH:
        #The white seperate things
        screen.create_line(100 * i, HEIGHT - 75, 100 * i + 70, HEIGHT - 75, fill = "white", width = 8)
        i += 1

#Draw stars and moon (Static)
def draw_MoonStars(screen):
    #Stars
    for i in range(400):
        size = uniform(1, 5)
        x1 = uniform(size, WIDTH - size)
        y1 = uniform(size, HEIGHT - size)
        #Different colors
        screen.create_oval(x1, y1, x1 + size, y1 + size, fill = choice(["tan1", "khaki", "light yellow", "white"]))
    
    #Moon (Crescent)
    #Use 2 identical circles overlapping
    screen.create_oval(20, 20, 90, 90, fill = "khaki1", outline = "khaki1")
    screen.create_oval(35, 20, 105, 90, fill = "black")

#Draw buildings
def draw_buildings(screen, newYear):
    #If it is not new year, the text is transpatent
    if newYear:
        textFill = "gold"
    else:
        textFill = ""

    #Building bodies
    body1 = screen.create_rectangle(25, 450, 150, 600, fill = "forest green", outline = "forest green")
    body2 = screen.create_rectangle(200, 500, 300, 600, fill = "tan4", outline = "tan4")
    mainBody = screen.create_rectangle(350, 350, 550, 600, fill = "brown", outline = "brown")
    body3 = screen.create_rectangle(600, 450, 700, 600, fill = "gray40", outline = "gray40")
    body4 = screen.create_rectangle(750, 480, 900, 600, fill = "saddle brown", outline = "saddle brown")

    #Roofs
    roof1 = screen.create_polygon(25, 450, 150, 450, 175/2, 375, fill = "light sea green", outline = "light sea green")
    roof2 = screen.create_polygon(200, 500, 300, 500, 500/2, 400, fill = "MediumPurple4", outline = "MediumPurple4")
    roof3 = screen.create_polygon(600, 450, 700, 450, 1300/2, 350, fill = "OliveDrab4", outline = "OliveDrab4")
    roof4 = screen.create_polygon(750, 480, 900, 480, 1650/2, 400, fill = "cadet blue", outline = "cadet blue")
    mainRoof = screen.create_polygon(350, 350, 550, 350, 900/2, 200, fill = "VioletRed4", outline = "VioletRed4")
    
    clockStructure = screen.create_oval(375, 375, 525, 525, fill = "gray90", outline = "black", width = 3)

    text = screen.create_text(450, 1125/2, text = "Happy New Year!", font = "Times 15", fill = textFill)

    clockScales = []
    
    for i in range(1, 13):
        angle = pi/6 #Every hour is 30 degrees
        x = 75 * cos(angle * i) + 450
        y = 75 * sin(angle * i) + 450
        clockScale = screen.create_oval(x - 3, y - 3, x + 3, y + 3, fill = "yellow", outline = "yellow")

        clockScales.append(clockScale)

    #Return a list to delete easily
    buildings = [body1, body2, body3, body4, mainBody, roof1, roof2, roof3, roof4, mainRoof, clockStructure, text]
    return buildings, clockScales

#Draw clock hands
def draw_clockhands(screen, hour_angle, minute_angle):
    #Turn to radians
    hour_angle, minute_angle = radians(hour_angle), radians(minute_angle)

    radius = 75

    end_x = (radius - 5) * cos(minute_angle) + 450
    end_y = (radius - 5) * sin(minute_angle) + 450
    end_x2 = (radius - 30) * cos(hour_angle) + 450
    end_y2 = (radius - 30) * sin(hour_angle) + 450

    hour_arm = screen.create_line(450, 450, end_x2, end_y2, fill = "red", width = 6)
    minute_arm = screen.create_line(450, 450, end_x, end_y, fill = "lime green", width = 3)

    center = screen.create_oval(445, 445, 455, 455, fill = "gray40", outline = "gray40")

    #Return a list to delete easily
    clockHands = [hour_arm, minute_arm, center]
    return clockHands

#Draw spark piece
def draw_spark(screen, x1, y1, length_scale, width_scale, spark_length, angle, color):
    length = spark_length * length_scale
    spark_width = spark_length * width_scale
    x4 = x1 + length * cos(angle)
    y4 = y1 + length * sin(angle)

    spark = screen.create_line(x1, y1, x4, y4, fill = color, width = spark_width)

    return spark

#Draw Car
def draw_car(screen, x1, y1, length, color, newYear):
    #If not new year, the car lights are off (transparent)
    if newYear:
        lightColor = "white"
    else:
        lightColor = ""
    
    #Make the relationship in ratios to enable modifying
    car_body = screen.create_rectangle(x1, y1, x1 + length, y1 + 0.4 * length, fill = color, outline = color)
    car_top = screen.create_arc(x1 + 0.2 * length, y1 - 0.3 * length, x1 + 0.8 * length, y1 + 0.3 * length, start = 0, extent = 180, fill = color, outline = color)
    wheel1 = screen.create_oval(x1 + 0.2 * length, y1 + 0.3 * length, x1 + 0.4 * length, y1 + 0.5 * length, fill = "gray30")
    wheel2 = screen.create_oval(x1 + 0.6 * length, y1 + 0.3 * length, x1 + 0.8 * length, y1 + 0.5 * length, fill = "gray30")
    light1 = screen.create_arc(x1 - 0.1 * length, y1 - 0.1 * length, x1 + 0.1 * length, y1 + 0.1 * length, start = 270, extent = 90, fill = lightColor, outline = lightColor)
    light2 = screen.create_arc(x1 + 0.9 * length, y1 - 0.1 * length, x1 + 1.1 * length, y1 + 0.1 * length, start = 180, extent = 90, fill = lightColor, outline = lightColor)
    
    #Return a list to delete easily
    finalCar = [car_body, car_top, wheel1, wheel2, light1, light2]
    
    return finalCar

#Draw person
def draw_Person(screen, x1, y1, height, color, newYear):
    #Make the relationship in ratios to enable modifying
    skin = "bisque"
    head = screen.create_oval(x1, y1 - height * 0.15, x1 + height * 0.15, y1, fill = skin, outline = skin)
    #When new year the people raise their arms to show delightment
    if newYear:
        arm1 = screen.create_line(x1, y1 + 0.05 * height, x1 - 0.15 * height, y1 - 0.25 * height, fill = skin, width = 0.05*height)
        arm2 = screen.create_line(x1 + 0.15 * height, y1 + 0.05 * height, x1 + 0.3 * height, y1 - 0.25 * height, fill = skin, width = 0.05*height)
    else:
        arm1 = screen.create_line(x1, y1 + 0.05 * height, x1 - 0.15 * height, y1 + 0.25 * height, fill = skin, width = 0.05*height)
        arm2 = screen.create_line(x1 + 0.15 * height, y1 + 0.05 * height, x1 + 0.3 * height, y1 + 0.25 * height, fill = skin, width = 0.05*height)
    
    body = screen.create_rectangle(x1, y1, x1 + 0.15 * height, y1 + 0.3 * height, fill = color, outline = color)
    leg1 = screen.create_rectangle(x1, y1 + 0.3 * height, x1 + 0.06 * height, y1 + 0.6 * height, fill = color, outline = color)
    leg2 = screen.create_rectangle(x1 + 0.09 * height, y1 + 0.3 * height, x1 + 0.15 * height, y1 + 0.6 * height, fill = color, outline = color)

    #Return a list, easy to delete (Unpack "*")
    person = [head, body, arm1, arm2, leg1, leg2]
    return person

#Draw lantern
def draw_lantern(screen, x1, y1, diameter):
    color = "gold"
    light = screen.create_rectangle(x1 + 0.25 * diameter, y1 - 0.25 * diameter, x1 + 0.75 * diameter, y1 + 1.25 * diameter, fill = color, outline = color)
    body = screen.create_oval(x1, y1, x1 + diameter, y1 + diameter, fill = "red", outline = "red")

    lantern = [light, body]
    return lantern

#Set Info
FPS = 120
unit_duration = 1 / FPS
frame_num = 1500
newYear_frame_num = 60 * 3 * 4 #Start at 9 pm and new year is 12 am, and 4 frames = 1 minute
newYear = False #When the frame reaches the number it is changed to True

sparks_num = 800 #Number of sparks in every firework
explosion_spacing = 25
explosion_num = ceil((frame_num - newYear_frame_num)/25)

leftcar_num = 5
rightcar_num = 5
#Y-values of the cars are contant as they are moving inline
leftcar_yValue = 775
rightcar_yValue = 850
left_carSpeed = -2
right_carSpeed = 2

people_num = 40

lanterns_num = 20

#Create empty arrays for sparks
# Available colors for every explosion to choose from
color_List = ["red", "orange red", "deep pink", "medium spring green", "cyan3", "blue", "magenta2", "lemon chiffon",
               "dodger blue", "yellow", "gold", "lawn green", "orange", "purple", "firebrick1"]
spark_xSpeeds = []
spark_ySpeeds = []
shootingAngles = []
spark_xValues = []
spark_yValues = []
length_scaleValues = [] #Scale means the dilation in length compared to normal
width_scaleValues = [] #Dilation in width compared to normal
spark_colors = []
sparksArray = [] #To store all the objects of drawings
#The center positions would vary
center_xArray = []
center_yArray = []

#Create empty arrays for cars
leftcar_xValues = []
rightcar_xValues = []
left_carObjects = []
right_carObjects = []
leftcar_colors = []
rightcar_colors = []

#Create empty arrays for people
people_xValues = []
people_yValues = []
people_colors = []
people_drawings = []
people_speeds = []

#Create empty arrays for lanterns
lantern_xValues = []
lantern_yValues = []
lantern_xSpeeds = []
lantern_ySpeeds = []
lantern_drawings = []

#Fill the arrays for cars
for i in range(leftcar_num):
    num = 200 * i
    leftcar_xValues.append(num)
    carObject = []
    left_carObjects.append(carObject)
    leftcar_colors.append(choice(["red","yellow","green","blue","purple","deep pink"]))

for i in range(rightcar_num):
    num = 200 * i
    rightcar_xValues.append(num)
    carObject = []
    right_carObjects.append(carObject)
    rightcar_colors.append(choice(["red","yellow","green","blue","purple","deep pink"]))

#Fill the array for people
for i in range(people_num):
    people_xValues.append(uniform(100, WIDTH - 100))
    people_yValues.append(choice([600, 625, 650, 675, 700]))
    people_colors.append(choice(["red","yellow","green","blue","purple","deep pink"]))
    personObejct = []
    people_drawings.append(personObejct)
    people_speeds.append(choice([1, -1]) * uniform(0.2, 1))

#Fill the arrays for lanterns
for i in range(lanterns_num):
    lantern_xValues.append(uniform(100, 800))
    lantern_yValues.append(uniform(400, 550))
    lantern_xSpeeds.append(uniform(-3, 3))
    lantern_ySpeeds.append(uniform(-3, -1.5))
    lantern = []
    lantern_drawings.append(lantern)

#Fill the arrays for sparks
for i in range(sparks_num):
    spark_colors.append("")
    angle = uniform(0, 2 * pi)  # random angle in radians
    shootingSpeed = uniform(0.5, 4)
    #These 2 are calculated using math
    xSpeed = shootingSpeed * cos(angle)
    ySpeed = shootingSpeed * sin(angle)
    spark_xSpeeds.append(xSpeed)
    spark_ySpeeds.append(ySpeed)
    shootingAngles.append(angle)
    length_scaleValues.append(uniform(1, 3))
    width_scaleValues.append(uniform(0.5, 1))
    #The x and y values will be set in the animation loop
    spark_xValues.append(0)
    spark_yValues.append(0)
    sparksArray.append(0) 

for i in range(100):
    #In order to make every firework explode in different random location
    center_xArray.append(uniform(100, 850))
    center_yArray.append(uniform(0, 300))

#Static Drawings
draw_MoonStars(screen)
draw_roads(screen)

#Animation
for f in range(frame_num):

    #If the frame number reaches the target frame, it is new year
    if f == newYear_frame_num:
        newYear = True

    #Draw fireworks (Behind lanterns (further away))
    if (f - newYear_frame_num) % explosion_spacing == 0:
        #Reset the center and color combo every interval
        color_combo = sample(color_List, 4) #Each explosion randomly choose 4 colors combo
        for i in range(sparks_num):
            spark_xValues[i] = (center_xArray[floor((f - newYear_frame_num) / explosion_spacing)])
            spark_yValues[i] = (center_yArray[floor((f - newYear_frame_num) / explosion_spacing)])
            spark_colors[i] = choice(color_combo)
    
    if newYear:
        for i in range(sparks_num):
            sparksArray[i] = draw_spark(screen, spark_xValues[i], spark_yValues[i], length_scaleValues[i], width_scaleValues[i], 3, shootingAngles[i], spark_colors[i])
            #Update position using speed
            spark_xValues[i] += spark_xSpeeds[i]
            spark_yValues[i] += spark_ySpeeds[i]

    #Draw the lanterns (behind buildings)
    for i in range(lanterns_num):
        #if the yvalue is negative, reset to initial position (to loop in the screen)
        if lantern_yValues[i] < 0:
            lantern_yValues[i] = uniform(400, 550) #Initial can be from 400 to 550
        lantern_drawings[i] = draw_lantern(screen, lantern_xValues[i], lantern_yValues[i], 15)

        #Change x speed every 50 frames
        if f % 50 == 0:
            lantern_xSpeeds[i] = uniform(-3, 3)
        
        lantern_xValues[i] += lantern_xSpeeds[i]
        lantern_yValues[i] += lantern_ySpeeds[i]

    #Draw the buildings
    buildings, clockScales = draw_buildings(screen, newYear)

    #Draw the clock hands (4 frames a minute)
    # In a minute (4 frames), minute hand goes 6 degrees, while hour hand goes 0.5 degrees
    # Starts at 21:00, minute hand is at 12, hour hand is at 9
    minute_angle = ((6/4) * f - 90) % 360
    hour_angle = ((0.5/4) * f - 180) % 360
    clockHands = draw_clockhands(screen, hour_angle, minute_angle)

    #Draw the cars going left
    for i in range(leftcar_num):
        # If the car's x value is less than 0, reset it to the rightmost side of the screen (WIDTH)
        if leftcar_xValues[i] < 0:
            leftcar_xValues[i] = WIDTH

        # Draw the car
        left_carObjects[i] = draw_car(screen, leftcar_xValues[i], leftcar_yValue, 80, leftcar_colors[i], newYear)

        leftcar_xValues[i] += left_carSpeed

    #Draw the cars going right
    for i in range(rightcar_num):
        right_xValue = rightcar_xValues[i] % WIDTH #To make it loop in the screen
        right_carObjects[i] = draw_car(screen, right_xValue, rightcar_yValue, 80, rightcar_colors[i], newYear)

        rightcar_xValues[i] += right_carSpeed

    #Draw people
    for i in range(people_num):
        #make the person loop in the screen
        if people_xValues[i] < 0:
            people_xValues[i] += WIDTH
        elif people_xValues[i] > WIDTH:
            people_xValues[i] -= WIDTH
        people_drawings[i] = draw_Person(screen, people_xValues[i], people_yValues[i], 50, people_colors[i], newYear)

        people_xValues[i] += people_speeds[i]

    #Update, sleep, delete
    screen.update()
    sleep(unit_duration)
    screen.delete(*buildings, *clockScales, *clockHands)
    for i in range(lanterns_num):
        screen.delete(*lantern_drawings[i])
    for i in range(leftcar_num):
        screen.delete(*left_carObjects[i], *right_carObjects[i])
    for i in range(people_num):
        screen.delete(*people_drawings[i])
    if newYear:
        screen.delete(*sparksArray)