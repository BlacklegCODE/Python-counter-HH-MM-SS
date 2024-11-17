import time

i = int(input("Enter are you ready ? 1 = Yes/ 2 = No"))
if i ==1:
    print("Lets start !")
else:
    print("We'll start anyways !")

p = int(input("Enter time in seconds :"))

for i in range(p,0,-1):
    print(i)
    time.sleep(1)
print("Happy Birthday !")

# two practice codes !


import time

t = int(input("Enter time in seconds :"))

for x in range(t, 0 , -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time up !")
