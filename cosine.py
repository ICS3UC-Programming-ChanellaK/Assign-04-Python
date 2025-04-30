#!/usr/bin/env python3
# Created By: Chanella
# Date: April 28, 2025
# This program generates cosine table for each degree between 0 and 360.


pi = 3.141592653589793

import math
    
def main(): # define the main function
     #The variable that will hold the degree value
     degree = 0
     print("welcome to the cosine table generator") # welcome message 
     while degree <= 360: # this is a loop that will run until degree is 360
         # this is the formula to convert degree to radians 
         radians = degree * (pi / 180)
         Cosine = math.cos(radians) #this is the formula that will calculate the cosine of the degree
         # this is the print message that will display the degree and the cosine value 
         print(f"Degree: {degree},Cosine: {Cosine}")     
         degree= degree + 1 # this is the increment of the degree by 1 until it reaches 360 
         print ("thank you for using the cosine table generator")
if __name__ == "__main__": # this is the main function that runs the program
     #this is the function that will call the main function
     main()


