'''
   Q1. Assign the value True to the variable cat, 
   and the value False to the variable dog.
   Then, use print() function and the type() function 
   to display the type for cat.
'''
cat = True;
dog = False;

print(type(cat));

'''
   Q2. print the boolean value
'''
print(cities);#data of cities is from nfl.csv

first_alb = cities[0] == "Albuquerque";
print(str(first_alb) + "\n");
second_alb = cities[1] == "Albuquerque";
print(str(second_alb) + "\n");
first_last = cities[0] == cities[len(cities)-1];
print(str(first_last) + "\n");

'''
   Q3. print the boolean value 2
'''
print(crime_rates)#data is loaded from nfl.csv

first_500 = crime_rates[0] > 500;
first_749 = crime_rates[0] >= 749;
first_last = crime_rates[0] >= crime_rates[len(crime_rates) - 1];
print(str(first_500) + " " + str(first_749) + " " + str(first_last));

'''
   Q4. boolean value 3
'''
print(crime_rates)

second_500 = crime_rates[1] < 500;
second_371 = crime_rates[1] <= 371;
second_last = crime_rates[1] <= crime_rates[len(crime_rates) - 1];

'''
   Q5. whether the third element in cities is equivalent to the string "Anchorage".
   If it is, change the variable result to 1.
'''
result = 0;
if cities[2]=="Anchorage":
    result = 1;
   
print(result);

'''
   Q6. Nested if
'''
both_conditions = False;

if crime_rates[0] > 500:
    if crime_rates[1] > 300:
        both_conditions = True;
        
print(both_conditions);

'''
   Q7. For loop
'''
five_hundred_list = [];

for cr in crime_rates:
    if(cr > 500):
        five_hundred_list.append(cr);

print(five_hundred_list);

'''
   Q8. Find the highest value
'''
print(crime_rates);
highest = crime_rates[0];
for cr in crime_rates:
    if cr > highest:
        highest = cr;
 
print(highest);
