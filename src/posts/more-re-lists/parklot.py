



# insert method
# inserts new list elements between
# two existing elements or at the front of the list.

# insert is used as a method of lists and takes two additional arguments.
# The first additional argument is the index position in the list
# where the new element should be inserted, and the second is the new element itself:



x4 = [1, 2, 3]
x4.insert(2, "hello")
print(x4)
[1, 2, 'hello', 3]
x4.insert(0, "start")
print(x4)
['start', 1, 2, 'hello', 3]






# ----------------------------------------
# remove method
# ----------------------------------------
# remove looks for the first instance of a given value in
# list and removes that value from the list:
x5 = [1, 2, 3, 4, 3, 5]
print(x5)
x5.remove(3)
print(x5)






# check whether 'in' a list
# If remove can’t find anything to remove, it raises an error.
# You can catch this error by using the exception-handling abilities of Python, or you can avoid the problem by using  in to check for the presence of something in a list before attempting to remove it.
if 5 in x5:
    x5.remove(5)






# max, min, sum
'''
>>> max(l)
3
>>> l = [0,1,2,3]
>>> max(l)
3
>>> min(l)
0
>>> sum(l)
6
>>>

'''







# The reverse method is a more specialized list modification method.
# It efficiently reverses a list in place:
x6 = [1, 3, 5, 6, 7]
x6.reverse()
[7, 6, 5, 3, 1]

# or
'''
>>> l = [0,1,2,3]
>>> l.reverse()
>>> l
[3, 2, 1, 0]
>>> l[::-1]
[0, 1, 2, 3]
>>> l
[3, 2, 1, 0]
'''






# sort using built-in method:
'''
>>> x = [3, 8, 4, 0, 2, 1]
>>> x.sort()
>>> x
[0, 1, 2, 3, 4, 8]

'''





# Sorting works with strings, too:
'''
>>> x = ["Life", "Is", "Enchanting"]
>>> x.sort()
>>> x
['Enchanting', 'Is', 'Life']
'''

# but not both
'''
>>> x = [1, 2, 'hello', 3]
>>> x.sort()
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'

'''





# ----------------------------------------
#   like strings
# ----------------------------------------

# similarity to strings as containers
# len()
length_of_x2 = len(x2)
print(length_of_x2)

# index values
# second entry to x2
print(x2[1])

# slices
print(x2[1:4])
#

# concatenation
'''
>>> z = [1, 2, 3] + [4, 5]
>>> z
[1, 2, 3, 4, 5]
'''

# the * operation
'''
>>> z = [None] * 4
>>> z
[None, None, None, None]
'''

# in (see above)
'y' in 'velocity'
#






# intersection
sentence = "Now is the time for all good men to come to the aid of their country."
split_sentence = sentence.split()

print(split_sentence)
print(" ".join(split_sentence))
print("---".join(split_sentence))
print(split_sentence)





import requests

url = "https://gist.githubusercontent.com/vlandham/2549b64121112dd9e4dacc47c959472a/raw/4e6883bbab5ab0d42fc4b9555d93e22aefd7baed/1984.txt"

r = requests.get(url, allow_redirects=True)

open('1984.txt', 'wb').write(r.content)

