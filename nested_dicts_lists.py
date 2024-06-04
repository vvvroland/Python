"""
#1
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0]=15
students[0]['last_name']='Bryant'
sports_directory['soccer'][0]='Andres'
z[0]['y']=30

print(x)
print(students)
print(sports_directory)
print(z)



#2

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

#first_name - Michael, last_name - Jordan
#first_name - John, last_name - Rosales
#first_name - Mark, last_name - Guillen
#first_name - KB, last_name - Tonel


def iterateDictionary(some_list):
    for dixt in some_list:
        for cat in dixt:
            print(cat)
            print(dixt[cat])




iterateDictionary(students) 


#3
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary2(key_name, some_list):
    for people in some_list:
        #for key_name in people:
        print(people[key_name])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)
"""


#4



dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

long=0

def printInfo(some_dict):
    for group in some_dict:
        print(group.upper() + ' ' + str(len(some_dict[group])))
        for x in range(0,len(group)):
            print(some_dict[group][x])


printInfo(dojo)
# output:

