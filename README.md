## Overview of Election Audit

This audit project is aimed at the tabulated election results of a precinct in Colorado. The total votes casted, votes casted for each candidate and the winning candidate are targeted in this audit. This audit will be coded and automated using Python, which can be utilize by future audits with similar formats. 

The Python code will import the raw tabulated results file and perform a series of calculations. These calculations will produce votes casted: in total, for each candidate and for each county. As well, the code will show the votes casted as a percentage of the total and determine the winning candidate and the county with the largest voter turnout. 

## Election-Audit Results

How many votes were cast in this congressional election?
-Total votes casted in this congressional election was 369,711. 

Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

-The breakdown of the results for each country is as follows:
	-Jefferson County: 38,855 votes (10.5% of total)
	-Denver County: 306,055 votes (82.8% of total)
	-Arapahoe County: 24,801 votes (6.7% of total)

Which county had the largest number of votes?

-Denver county had the largest number of votes.

Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

-The breakdown of the results for each candidate is as follows:
	-Charles Casper Stockham: 85,213 votes (23.0% of total)
	-Diana DeGette: 272,892 votes (73.8% of total)
	-Raymon Anthony Doane: 11,606 votes (3.1% of total)

Which candidate won the election, what was their vote count, and what was their percentage of the total votes?

The winning candidate was Diana DeGette, 272,892 votes were casted for her, which accounted for 73.8% of the total votes. 


##  Election-Audit Summary

There are two additional ways this code can be modified to be used for future elections. 
### Method 1:
Instead of hard coding the row values for variables “candidate_name” and “county_name” (seen here), these variables can be set to dynamic in case the referenced data are located in different columns. 

First of all, the assumption is that all datasets this code will be used on will have columns that are titled “Candidate” and “County”, this is an easy change in the original data to work with the code without messing up any raw data.  To begin, two new variables will be created: TYPE_candidate = “Candidate” and TYPE_county = “County”, which hard codes the values that will be searched for in the data file. 

Secondly, a “for” loops will be constructed. The “len” function will be used to determine the length of variable “header”, which contains data for the first row of the data file. “h_index” is then set to access different index positions in “header” and is looking for a matching value for TYPE_candidate. When a matching value is found, a new variable “candidate_name_col_index” is set to equal to “h_index”, this initializes the position of the column containing candidate data. 

Lastly, another “for” loop is created to perform similar functions as the “for” above, the difference is this time the “h_index” is looking for a matching value for TYPE_county, and a new variable “county_name_col_index” is created and set to equal to “h_index” to initialize the position of the column containing county data. 

These “for” loops can be seen HERE. I had the idea to have the code iterate through the header row to look for matching values to make the variable dynamic, but unfortunately, I did not know how to code it, I had the help of TA James to create these “for” loops. 

### Method 2:
Another modification to this code is to show the breakdown of candidates for each county. This can show how close the race was and the political sentiment within each county. Unfortunately I do not know enough Python to complete this, so I created the results using Pandas in Jupyter Notebook, which can be seen HERE. 

This is done by importing the pandas dependencies first and transforming it to a DataFrame. The DataFrame can then be filtered by using the groupby.() function to be sorted by County and Candidates. The sum of votes for each candidate is tallied up by using the count() function on the sorted DataFrame. 

