# #1
# def number_of_food_groups():
#     return 5
# print(number_of_food_groups())

# ##Predicted 5...
# # Code returned 5


# #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())

# ##Predicted an error due to a function being called but not defined
# ##Code returned an error function not defined

# #3
# def number_of_books_on_hold():
#     return 5
#     return 10
# print(number_of_books_on_hold())

# ## Predicted the code will return 5 and 10 on separate lines
# ## Wrong!  print statment passes 0 arguments in, therefore nothing will be returned


# #4
# def number_of_fingers():
#     return 5
#     print(10)
# print(number_of_fingers())

# ##Predicted the code will produce 10
# ## WRONG!  the code produced 5


# #5
# def number_of_great_lakes():
#     print(5)
# x = number_of_great_lakes()
# print(x)

# ## Predicted the code will produce 5
# ## Code resulted in a 5 and None ( I see...because x = a function with no arguments passed)


# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))

# ##Predicted 8
# #Code results in 3 and 5 on separate lines


#7
# def concatenate(b,c):
#     return str(b)+str(c)
# print(concatenate(2,5))

# #prediction 2 5
# #code returned 25 with no space





# #8
# def number_of_oceans_or_fingers_or_continents():
#     b = 100
#     print(b)
#     if b < 10:
#         return 5
#     else:
#         return 10
#     return 7
# print(number_of_oceans_or_fingers_or_continents())


# ##Predicted code would produce 100
# ## Code produced 100 and 10 on separate lines


# #9
# def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
#     if b<c:
#         return 7
#     else:
#         return 14
#     return 3
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))

# ##Predicted code would return 7,14,21 on separate lines
# ##Actual code  YES! Got it right!


# #10
# def addition(b,c):
#     return b+c
#     return 10
# print(addition(3,5))

# ##Predicted 8 and 10 on separate lines
# #@Actual code  only 8 was produced




# #11
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
# print(b)
# foobar()
# print(b)

# ##Prediction 500, 500, 300, 500
# ##Actual code produced: YES! got it right!


# #12
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# foobar()
# print(b)


# ##Prediction: 500, 500, 300, 500
# ##Actual Code:Got it right!


# #13
# b = 500
# print(b)
# def foobar():
#     b = 300
#     print(b)
#     return b
# print(b)
# b=foobar()
# print(b)


##Prediction: 500, 500, 300, 300
##Actual Code: 500, 500, 300, 300


# #14
# def foo():
#     print(1)
#     bar()
#     print(2)
# def bar():
#     print(3)
# foo()

##Predicted 1 error 2 
##Actual: 1, 3 , 2


# #15
# def foo():
#     print(1)
#     x = bar()
#     print(x)
#     return 10
# def bar():
#     print(3)
#     return 5
# y = foo()
# print(y)

# ##Predicted: 1, 3, 3
# ##Actual Code: 1,3,5,10