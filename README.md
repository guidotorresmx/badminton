# Badminton by MotionCorrect
City of Toronto Community Center Tracker. Filters by postal code, activities and extra characteristics are available - Project by MotionCorrect 

# Specifications
## Features
1. Retrieve the “Table and Subsequent link parsing from the list of all the centers. https://www.toronto.ca/data/parks/prd/facilities/recreationcentres/index.html” 
2. Request data for each of the centres link (e.g. https://www.toronto.ca/data/parks/prd/facilities/complex/3643/index.html) and filter it by: 
   1. Only data for "DROP-IN" adult "badminton" programs. 
      1.  Badminton (17yrs and over)
      2. Not Badminton (60yrs and over)
      3. Not Badminton (13 - 18 yrs)
   2. Activity available for the current week. 
3. Output the information in CLI/Terminal or spreadsheet; nicely formatting excel spreadsheet that clearly identifies the location that offers such drop-in activities and which date/time.

## Bonus features
1. Use open-source mapping related API to narrow search results to the nearest N centers which the clients will provide a Canadian Postal Code. 
2. Filter activities based on date weeks.
3. Generate an easy-to-use frontend that clearly identifies:
   1. Location that offers such drop-in activities and which date/time
   2. Sorted by distance to the given postal code

