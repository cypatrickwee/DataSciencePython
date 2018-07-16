'''
   Q1.
'''
weather_data = [];
f = open("la_weather.csv","r");
data = f.read();

#split the data on the newline character convert it to a list of rows
_convertData=data.split("\n");
#print(_convertData);
#split each row on the comma and append each list to weather_data
weather_data = [];
for elem in _convertData:
    weather_data.append(elem.split(','));
                        
print(weather_data);

'''
   Q2. Loop over each row in weather_data
   append the second item in each row to the weather list.
'''
# weather_data has already been read in automatically to make things easier.
weather = [];
for elem in weather_data:
    weather.append(elem[1]);

print(weather);

'''
   Q3. Count the element in weather
'''
count = 0;

for elem in weather:
    count+=1;

print(count==len(weather));

'''
   Q6. the use of in
'''
animals = ["cat", "dog", "rabbit", "horse", "giant_horrible_monster"]

cat_found = "cat" in animals;#true
space_monster_found = "space_monster" in animals;#false
print(str(cat_found) + " " + str(space_monster_found));

'''
    Q7. 