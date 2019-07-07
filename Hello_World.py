message="Hello Python World!";
print(message);

message='Hello Python Crash Cousrse World!';
print(message);

message="The language 'Python' is named after Monty Python, not the snake";
print(message);

name="ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name="ada"
last_name="lovelace"
full_name=first_name + " " + last_name
print(full_name)

print("\tPython")

print("Languages:\n\tPython\n\tC\n\tJavascript")

name=" python "
print(name.rstrip())
print(name)
print(name.strip())

print("Hello")
print(2+3)
print(3-2)
print(3*2)
print(3**2)
print(0.1+0.1)

# 向大家问好
age=23
message="Happy " + str(age) + "rd Birthday!"
print(message)

import this

bicycles=['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[-2].title())

bicycles[0]="ducatei"
print(bicycles)

bicycles.append("ducati");
print(bicycles)

bicycles.insert(1, "boy")
print(bicycles)

del(bicycles[2])
print(bicycles)

msg = bicycles.pop();
print(msg)

first_element=bicycles.pop(0);
print(first_element);
print(bicycles)

bicycles.remove("redline")
print(bicycles)

cars=["bmw", "audi", 'toyota', "subaru"]
print(sorted(cars, reverse=True))
cars.reverse()
print(cars);
print(len(cars))

magicians=['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
print("Thank you, everyone");

for value in range(1,5):
	print(value)
numbers=list(range(1,12,2))
print(numbers)
print(sum(numbers))

squares=[value**2 for value in range(1,11)]
print(squares)

players=["charles", "martina", "michael", "florence", "eli"]
print(players[:])

my_foods=["pizza", "falafel", "carrot cake"]
friend_foods=my_foods
my_foods.append("cannoli")
friend_foods.append("ice cream")
print(my_foods)
print(friend_foods)

dimessions=(200,50)
print(dimessions[0])
print(dimessions[1])
dimessions=(100,200)
print(dimessions[0])
print(dimessions[1])
