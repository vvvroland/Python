"""
#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#predict 5, correct

#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
# Predict undefined/error 5. Partially correct; error in first part stops block

#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#predict 5 (return breaks out of function before next line) Correct

#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#Predict 5. Similar reason as #3 Correct

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#Predict 5 new line five (first print and function call print). Incorrect. 5, new line None, because no actual value passed when x variable defined, so none to print)

#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
#Predict 8 (3+5), though possible you just get 1, 2, 2, 3. Incorrect. The TypeError arises from attempting to sum a list containing ‘None‘ values, representing missing discrete values in the data set.
#If return added, like in 7, should be actual addition.

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#Predict 25. Correct

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#Predict 10. Partial Correct. Forgot about first print.

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#Predict 7 new line, 14 new line, 21. Correct

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#Predict 8. Correct

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#Predict 500 new line, 300 new line, 500 new line, undefined new line, 500. Partial (Yes, no, no, no, yes) Second wrong because function only defined, not called. Actual values in function, so not undefined.

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#Predict 500 newline, 500 new line, 300 new line, 300. Partial correct. Thought return might make the value for outside function, but not right. The rest correct

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#Predict 500 new line, 500 new line, 300 new line, 300. (defining b as the function changes b). Correct


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#Predict 1 new line, 2. Partial correct. Bar is defined as print 3 after function, so pulled in and printed between the two.

"""
#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#Predict 1 new line, 3 new line, 5. Partial correct. Return in bar, only breaks out of the bar function, not all functions the bar function may be inside
