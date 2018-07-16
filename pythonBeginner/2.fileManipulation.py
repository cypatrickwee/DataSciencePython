#files and loops
'''
   Q1. Use the open() function to create a File object.
   The name of the file to open is "crime_rates.csv". Access the file in read mode ("r").
   Assign this File object to the variable f.
'''
f = open("crime_rates.csv","r")
print(f);

'''
   Q2. Run the read() method on the File object f to return the string representation of crime_rates.csv.
   Assign the resulting string to a new variable named data
'''
data = f.read();
print(data);

'''
   Q3. Split the string object data on the new-line character "\n", 
   and store the result in a variable named rows.
   Then, use the print() function to display the first five elements in rows.
'''
# We can split a string into a list.
sample = "john,plastic,joe"
split_list = sample.split(",")
print(split_list)

# Here's another example.
string_two = "How much wood\ncan a woodchuck chuck\nif a woodchuck\ncould chuck wood?"
split_string_two = string_two.split('\n')
print(split_string_two)

# Code from previous cells
f = open('crime_rates.csv', 'r')
data = f.read();
#split the string on the new line
rows = data.split('\n');
#print the first 5 elements
print(rows[:5]);

'''
   Q4. The variable ten_rows contains the first 10 elements in rows.
    Write a for loop that:
        iterates over each element in ten_rows
        uses the print() function to display each element
'''
ten_rows = rows[:10];

for elem in ten_rows:
        print(elem);

'''
   Q5. List in list
'''
three_rows = ["Albuquerque,749", "Anaheim,371", "Anchorage,828"]
final_list = []
for row in three_rows:
    split_list = row.split(',')
    final_list.append(split_list)
print(final_list)
print(final_list[0])
print(final_list[1])
print(final_list[2])

'''
   Q6. Write a for loop that splits each element in rows on the comma delimiter, 
   and appends the resulting list to a new list named final_data.
   Then, use the print() function and list slicing to display the first five elements in final_data.
'''
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
final_data =[];
for elem in rows:
    final_data.append(elem.split(','));
   
print("\nthis is the new list: " + str(final_data));

'''
   Q7. Create a list of strings named cities_list that contains the city names from each list in rows.
'''
cities_list = [];
for elem in final_data:
    cities_list.append(elem[0]);
   
print(cities_list[:5]);

'''
   Q8. Read the crime_rates.csv again and convert the number as string value to int.
   store the list in to int_crime_rates
'''
f = open('crime_rates.csv', 'r')
data = f.read()
rows = data.split('\n')
print(rows[0:5])
int_crime_rates = [];

for elem in rows:
    int_crime_rates.append(int(elem.split(',')[1]));
                           
print(int_crime_rates);


