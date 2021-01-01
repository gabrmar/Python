print(all([1,2,0,4,4]))
print(any([0,0,0,0,0,0]))
número = 10
x = [i > número for i in [1,2,3,4,5,6,7,8,9,0,10,11]]
print(x)
print(all(x))
print(any(x))