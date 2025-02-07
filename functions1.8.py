#Write a function that takes in a list of integers and returns True if it contains 007 in order

def spy_game(nums):
    a = [0, 0, 7]
    for num in nums:
        if num == a[0]:
            a.pop(0)
        if not a:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5])) #True
print(spy_game([1,0,2,4,0,5,7])) #True
print(spy_game([1,7,2,0,4,5,0])) #False