with open("pi_digits.txt") as file_object:
	contents = file_object.read();
	print(contents)

with open("pi_digits.txt") as file_object:
	for line in file_object:
		print(line.rstrip());

with open("pi_digits.txt") as file_object:
	lines = file_object.readlines();
pi_string = "";
for line in lines:
	pi_string += line.strip();
print(pi_string);
print(len(pi_string));

try:
	print(5/0);
except ZeroDivisionError:
	print("You can't divide by zero!");
