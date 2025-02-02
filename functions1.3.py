#Write a program to solve a classic puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have? create function: solve(numheads, numlegs):
    # c - chicken, r - rabbit, h - heads, l  - legs
    # r+c=h / R1 => R2-2R1 => r=(l-2h)/2
    # 4r+2c=l / R2 => 4R1-R2 => c=(4h-l)/2
def solve(numheads, numlegs):
    chicken = int((4 * numheads - numlegs) / 2)
    rabbit = int((numlegs - 2 * numheads) / 2)
    return chicken, rabbit

print (solve(35, 94))