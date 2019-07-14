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

cars=["audi", "bmw", "subaru", "toyota"]
for car in cars:
	if car == "bmw":
		print(car.upper())
	else:
		print(car.title())

car="BMW"
print(car.lower() != "bmw")
print("\n")

age=18
print(age==18)
print("\n")

a=10
b=20
print(a>=10 and b >= 21)
print("\n")

requested_toppings=["mushrooms", "onions", "pineapple"]
print('mushrooms' in requested_toppings)
print("\n")

banned_users=["andrew", "carolina", "david"]
user="marie"
if user not in banned_users:
	print(user.title()+", you can post a response if you wish.")
print("\n")

age=17
if age>=18:
	print("You are old enough to vote!")
	print("Have you registered to voted yet?")
else:
	print("Sorry, you are too young to vote.")
	print("Please registered to vote as soon as you turn 18!")
print("\n")

age=12
if age < 4:
	print("Your admission cost is $0.")
elif age < 18:
	print("Your admission cost is $5.")
else:
	print("Your admission cost is $10.")
print("\n")

age=12;
if age < 4:
	price = 0;
elif age < 18:
	price = 5;
else:
	price = 10;
print("Your admission cost is $" + str(price) + ".");
print("\n")

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
for requested_topping in requested_toppings:
	if requested_topping == "green peppers":
		print("Sorry, we are out of green peppers right now.")
	else:
		print("Adding " + requested_topping + ".")
print("Finished making your pizza!")
print("\n")

requested_toppings=[]
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
	print("Finished making your pizza!")
else:
	print("Are you sure you want a plain pizza")

alien_0={'color':"green", "points":5}
print(alien_0)
alien_0["x_position"]=0
alien_0["y_position"]=25
print(alien_0)

alien_0={}
alien_0["color"]="green"
alien_0["point"]=5
print(alien_0)
print("\n")

alien_0={"color": "green"}
alien_0["color"]="yellow"
print(alien_0)
print("\n")

alien_0 = {"x_position" : 0, "y_position": 25, "speed" : "medium"}
print("Original x-position: " + str(alien_0["x_position"]))

#向右移动外星人
#据外星人当前速度决定将其移动多远
if alien_0["speed"] == "slow":
	x_increment = 1
elif alien_0["speed"] == "medium":
	x_increment = 2
else:
	x_increment = 3
alien_0["x_position"] = alien_0["x_position"] + x_increment
print("New x_position: " + str(alien_0["x_position"]))
print("\n")

alien_0 = {"color": "green", "points": 5}
print(alien_0)
del alien_0["points"]
print(alien_0)
print("\n")

user_0 = {"username": "efermi",
		  "first": "enrico",
		  "last": "fermi"}
for key, value in user_0.items():
	print("key:" + key + ", value:" + value)
print("\n")

favorite_languages = {
	"jen": "python",
	"sarah": "c",
	"edward": "ruby",
	"phil": "python",
	}
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")
print("\n")

for name in favorite_languages.keys():
	print(name.title())
print("\n")

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", thank you for taking the poll.")
for language in set(favorite_languages.values()):
	print(language.title())

alien_0 = {"color" : "green", "points" : 5}
alien_1 = {"color" : "yellow", "points" : 10}
alien_2 = {"color" : "red", "points" : 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)
print(aliens)
