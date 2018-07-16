import math
root = math.sqrt(99);
flr = math.floor(89.9);
print(str(root) + "\n" + str(flr));


'''
   Q2. Import the math module as m.
   Use the sqrt() function from the math module to compute the square root of 33. Assign the result to root.
'''
import math as m
root = m.sqrt(33);
print(str(root));

'''
    Q3. Import all of the functions from math.
    Use the sqrt() function from the math module to compute the square root of 1001. Assign the result to root.
'''
from math import *
root = math.sqrt(1001);
print(str(root));

'''
   Q4. Accessing a module variable by using dot
   Assign the square root of pi to a.
   Assign the ceiling of pi to b.
   Assign the floor of pi to c.
'''
a = math.sqrt(math.pi);
b = math.ceil(math.pi);
c = math.floor(math.pi);

print(str(a) + " " + str(b) + " " + str(c));

'''
   Q5. Read all of the data from "nfl.csv" into a list variable named nfl using the csv module."
'''
import csv
nfl_file = open("new_nfl.csv");
nfl = list(csv.reader(nfl_file));
#print(nfl);

'''
   Q6. Counting the no of wins of "New England Patriots"
   header for new_nfl.csv: Year, Week, Winner, Loser
'''
import csv
f = open("new_nfl.csv", "r")
nfl = list(csv.reader(f))

patriots_wins = 0;

for winner in nfl:
    if winner[2] == "New England Patriots":
        patriots_wins+=1;
        
print(patriots_wins);

'''
   Q7. define function to count the winner based on team_name
'''

import csv

f = open("new_nfl.csv", 'r')
nfl = list(csv.reader(f))
cowboys_wins = 0;
falcons_wins = 0;

# Define your function here.
def nfl_wins(team_name):
    if team_name == "Dallas Cowboys":
        global cowboys_wins;
        for winner in nfl:
            if winner[2] == team_name:
                cowboys_wins+=1;
        return cowboys_wins;
    
    elif team_name == "Atlanta Falcons":
        global falcons_wins;
        for winner in nfl:
            if winner[2] == team_name:
                falcons_wins+=1;
        return falcons_wins;

cowboys_wins = nfl_wins("Dallas Cowboys");
falcons_wins = nfl_wins("Atlanta Falcons");

print(cowboys_wins);
print(falcons_wins);


