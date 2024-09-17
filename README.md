# Data Decoded: Harnessing Python's PANDAS Library

## Welcome to Experiment 3!
Python Data Analysis (PANDAS), a project showcases fundamental data analysis skills utillizing Python's PANDAS library. The repository includes codes and solutions for data manipulation and analysis, guiding users through important concept like loading, visualizing, and exploring data.

### Little Overview before we start
This experiment explores the use of pandas for efficient data analysis. By loading a CSV file into a pandas DataFrame, we will go through a set of problems designed to help you become familiar with basic operations.

#### I. Intended Learning Outcome
1. To identify the codes and functions incorportaed in the Pandas library
2. To be able to apply and use the different codes and functions in creating a Python program using a Pandas library.

#### II. Instructions
        Write a Python script/code in the Jupyter Notebook to do the given problem. You may submit your Jupyter notebook in the dedicated submission bin.

        For this programming assignment, download the following file and save to your default user folder: https://bit.ly/Cars_file

## Problem Overview
#### Problem 1: Exploring the Cars Dataset
        We will be working with a dataset in .csv format and performing the following tasks: The dataset represents real-world data related to cars, and this simple analysis will help us gain familiarity with loading and exploring the data using pandas.

         Setup Instructions!

         Step 1: The csv file should be uploaded on the same data file with your jupyter notebook before we call the PANDAS library.
         Step 2: Importing the pandas library, which is the core tool used in this experiment for manipulating data.
         Step 3: Next, we will load the data set we are working with contains informations about various cars.
         Step 4: Display the first five rows by using head() method.
         Step 5: Display the last five rows by using tail() method.
         Step 6: Print and we're done!

         By following these steps, we can perform a basic exploration of the dataset using pandas, laying the foundation for more complex problems in the future!

#### Problem 2: Probe further into the Cars Dataset
        Now that we've loaded and explored the basics of our cars dataset, it's time to level up and get hands-on with some advanced -- atleast for me -- pandas techniques. We'll be using subsetting, slicing, and indexing to extract more specific information from the dataset!

        Part A: Displaying Rows with Odd-numbered Columns
                Step 1: Make sure that the csv file is uploaded on the same data file in your jupyter notebook where you will do your code. Never forget to import pandas!
                Step 2: Call the odd_columns and make sure to include the variable car with columns and specifiy which column in the csv file you are extracting.
                Step 3: To make our code cleaner, summon a new variable to specify that we will be getting only the first five rows and use the head() method.
                Step 4: Print and we're done with part A!

                We now have just the odd-numbered columns. Let's move on to the next part of problem 2, shall we?

        Part B: Finding the row with 'Mazda RX4'
                Step 1:  Make sure that the csv file is uploaded on the same data file in your jupyter notebook where you will do your code. Never forget to import pandas!
                Step 2: Call a variable for a new entry, don't forget to summon car since that's where will be getting our data. 
                Step 3: Specify 'Model' for the variable car focus in calling the model column and use .str.contains() method to call a certain element under the model column which is Mazda RX4.
                Step 4: Print! Since its not stated that the index is required for the output, to make our output cleaner use the key index=False.

                Nice! We've successfully retrieved the row for Mazda RX4.

        Part C: How many Cylinders in 'Camaro Z28'?
                Step 1: Make sure that the csv file is uploaded on the same data file in your jupyter notebook where you will do your code. Never forget to import pandas!
                Step 2: Same with Part B, call a new variable for new entry but don't forget to summon car because that's where our dataset is. 
                Step 3: Then again, specify the 'Model' and use .str.contain() method so our code will read on 'Model' column specifically on the 'Camaro Z28'.
                Step 4: To have a presentable output, let's use the newline character to accord the sentence we're trying to make for our output.
                Step 5: With the newline character, lets make a sentence. Start with "\nThe then include plus sign then call model variable to read inside it (the car) then specify model and use .to_string() method to render a DataFrame into a sting presentation with the index=False to remove the index infront, add another plus sign for the word 'have' and another plus sign to include the cylinder number with the help of .to_string again with the index=False and one last plus sign to add the word 'cylinder/s' to complete the sentence.
                Step 6: Add the print() method on the first part of step 5 and voila!

                Now we have the number of cylinders, just like that! Let's move on now to the last and hardest part of this experiment.

        Part D: Finding Cylinders and Gear Types for Multiple Cars
                Step 1: Make sure that the csv file is uploaded on the same data file in your jupyter notebook where you will do your code. Never forget to import pandas!
                Step 2: 
        
