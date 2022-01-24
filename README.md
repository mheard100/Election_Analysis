# Election_Analysis
Congressional Election Analysis Using Python, Visual Studio Code, GIT Bash

# ELECTION ANALYSIS
Create an Election Analysis "PyPoll" with Python
## Overview of Project
A Colorado Board of Elections employee has given you the task to complete the election audit of a recent local congressional election.
Python code is used to analyze an excel csv file with voting data. Things looked for in the data set include:

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.


# Deliverable 1a: Candidate Results
## Deliverable Requirements:

1.Total Votes in the election are printed to the terminal. 

2.Each candidate’s total votes and percentage of votes are printed to the terminal. 

3.The winner of the election, winning vote count, and winning percentage of votes are printed to the terminal. 

# Deliverable 1b: County Results
## Deliverable Requirements:

1. Each county and its total vote count are printed to the terminal. 

2. Each county and its percentage of the total votes are printed to the terminal. 

3. The county with the largest number of voters is printed to the terminal. 



# Resources

* Data Source: election_results.csv
* Software: Python 3.7 (64Bit), Visual Studio Code 



### Election-Audit Results:
> Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

* How many votes were cast in this congressional election?

> - **Total Votes Cast** in this congressional election was **369,711** 

* Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
> ***County Votes:***
> - **Jefferson** county has `10.5%` total percentage with a total votes of **38,855**
> - **Denver** county has the `82.8%` total percentage with a total votes of **306,055**
> - **Arapahoe** county has `6.7%` total percentage with a total votes of **24,801**

* Which county had the largest number of votes?
> ***County with Largest Number of Votes:***
> - **Denver** county has the largest number total of **306,055**
> - In addition, **Denver** county has the total votes percentage of `82.8%`  
> - **Denver** county is the Largest County Turnout

* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
> ***Candidate Percentage of Votes:***
> - **Charles Casper Stockham** candidate has `23.0%` total percentage with a total votes of **85,213**
> - **Diana DeGette** candidate has the `73.8` total percentage with a total votes of **272,892**
> - **Raymon Anthony Doane** candidate has `3.1%` total percentage with a total votes of **11,606**

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
> ***Election Results:***
> - **Diana DeGette** won the election, with a total votes of **272,892**
> - **Diana DeGette** has the total percentage votes of `73.8%`  
> - **Diana DeGette** is the Winner!


#### Election-Audit Summary
This script should be used by the election commission for future elections. To use for other elections, the file
file path may need to be changed dependent on where it is located in the directory. Furthermore, extracting
candidate names and countys by columns may need to change dependent on the raw data set. This may include 
the header if it is more than one row at the top (i.e There's a title row). With minimum tweaks to the code,
it can be reused over and over again. 
