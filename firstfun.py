def my_func():
    print("Hello from function")

def add_num(a,b):
    return a+b

def keyword_argument(child3, child2, child1): #keywordArgument
  print("The youngest child is " + child3)

def arbitrary_keyword_argument(**kid): #Arbitrary keywordArgument
  print("His last name is " + kid["lname"])

def arbitary_func(*args):  #Arbitrary Arguments
    return args[0] + args[1] + args[2]

def loop_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

loop_function(fruits)

my_func()
total = add_num(2,3)
res = arbitary_func(2,3,4)
print(total)
print(res)
keyword_argument(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
arbitrary_keyword_argument(fname = "Tobias", lname = "Refsnes")

