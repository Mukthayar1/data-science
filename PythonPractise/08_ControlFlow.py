# # Conditional statements

x = -1
if x > 0 :
    print('X IS POSITIVE')
elif x < 0:
    print("X IS NEGATIVE")
else :
    print('X IS NEUTRAL')

# # For loops
items = ["pen","paper","book","copy"];

for x in items:
    print(x)  

i = 0 

while i < 6 :
    i = i + 1
    print(i)

for x in "Mukthayar":
    if x == "a":
        break
    print(x)  

for x in "Mukthayar":
    if x == "a":
        continue
    print(x)  

for x in "Mukthayar":
    if x == "a":
        pass
    print(x) 