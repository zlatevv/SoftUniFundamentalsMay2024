coffees = 0
event = input()
while event != "END":
    if event.lower() == "coding" or event.lower() == "dog" or event.lower() == "cat" or event.lower() == "movie":
        if event.islower():
            coffees += 1
        elif event.isupper():
            coffees += 2
    event = input()
if coffees > 5:
    print("You need extra sleep")
else:
     print(coffees)