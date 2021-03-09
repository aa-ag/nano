# udacity = {}
# udacity['u'] = 1
# udacity['d'] = 2
# udacity['a'] = 3
# udacity['c'] = 4
# udacity['i'] = 5
# udacity['t'] = 6
# udacity['y'] = 7

# print(udacity)
# print(udacity['t'])

# dictionary = {}
# dictionary['d'] = [1]
# dictionary['i'] = [2]
# dictionary['c'] = [3]
# dictionary['t'] = [4]
# dictionary['i'].append(5)
# dictionary['o'] = [6]
# dictionary['n'] = [7]
# dictionary['a'] = [8]
# dictionary['r'] = [9]
# dictionary['y'] = [10]
# print(dictionary)

###--- Exercise ---###
'''
Task 1
You need to add the cities listed below by modifying the given structure. Cities to add:

Bangalore (India, Asia)
New Delhi (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)
Be careful, while adding a city in an existing country. Consider adding it to the existing list of cities as:

locations['Asia']['India'].append('New Delhi')
'''

locations = {'North America': {'USA': ['Mountain View']}}

locations['Asia'] = {'India': ['Bangalore']}
locations['Asia']['India'].append('New Delhi')
locations['North America']['USA'].append('Atlanta')
locations['Asia']['China'] = ['Shanghai']

print(locations)
'''
 {'North America': {'USA': ['Mountain View', 'Atlanta']}, 
 'Asia': {'India': ['Bangalore', 'New Delhi'], 'China': ['Shanghai']}}
'''

# TODO: Print a list of all cities in the USA in alphabetic order.
# for city in sorted(locations['North America']['USA']):
#     print(city)

# TODO: Print all cities in Asia, in alphabetic order, next to the name of the country
for country in locations['Asia']:
    for city in sorted(locations['Asia'][country]):
        print(country, city)
