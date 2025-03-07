#Write a Python program with builtin function that returns True if all elements of the tuple are true.

def all_true(t):
    return all(t)

tuple1 = (True, True, True)
tuple2 = (True, False, True)
tuple3 = (45, 67, 113)
tuple4 = (0, 5, 11)

print(all_true(tuple1)) #True
print(all_true(tuple2)) #False
print(all_true(tuple3)) #True
print(all_true(tuple4)) #False