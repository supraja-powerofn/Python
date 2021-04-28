import math

print("Hello")

#Conditional
value = 5
if value == 5:
    print("A welcome")
elif value == 1:
    print("One")
else:
    print("Nothing")

#Loop    
for i in range (value):
    print(i)


def return_cube(n):
    return lambda n : n**3 
func = return_cube(8)
print("Cube returned: ",func(8))

def print_cubes():
    for i in range(5):
        print("Cube of ",i," is: ",i**3)

def sq_root(squares = []):
    for element in squares:
        print("Sq root of ",i," is :" , round(math.sqrt(element)))

#Positional and keyword parameters
def multiply(first,/,second,*,last):
    return first * second * last

print(multiply(1,second = 2,last = 3))


#Bitwise operations
x=2
x &= 3
print(x)
x <<= 2
print(x)

# while loop
loop_value = 1
while loop_value < x:
    print("Sum till",loop_value,": ",sum(range(loop_value)))
    loop_value += 1

#list
squares = [1,4,9,16,25]
squares = squares + [36]
print(squares)
squares.append(65)
print(len(squares))
print(squares)
sq_root(squares)

#set
first = set('abcde')
second=set('cde')
print(first-second)
print(first & second, " ",first | second," ",first ^ second)

#dictionary
dict1 = {'b':1,'a':2,'c':3}
print(dict1,"\n",list(dict1),"\n",sorted(dict1))
print( 'c' in dict1 ,"\n" , 'a' not in dict1)

#user func
print_cubes()

print(multiply(1,2,last=3))

