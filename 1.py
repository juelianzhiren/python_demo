def describe_pet(pet_name, animal_type="dog"):
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".");
	print("My " + animal_type + "'s name is " + pet_name.title() + ".");
	
describe_pet(pet_name="willie")
describe_pet(animal_type="hamster", pet_name="harry")


def get_formatted_name(first_name, last_name, middle_name=""):
	if middle_name:
		full_name = first_name + " " + middle_name + " " + last_name;
	else:
		full_name = first_name + " " + last_name;
	return full_name.title();
	
musician = get_formatted_name("jimi", "hendrix");
print(musician);
print(get_formatted_name("john", "hooker", "lee"));
print("\n");

def build_person(first_name, last_name, age=""):
	"""返回一个字典，其中包含一个人的信息"""
	person = {"first": first_name, "last": last_name};
	if age:
		person["age"]=age;
	return person;
musician = build_person("jimi", "hendrix", 28);
print(musician);

while True:
	print("\nPlease tell me your name:");
	print("(enter 'q' at any time to quit)");
	f_name=input("First name:");
	if f_name=="q":
		break;
		
	l_name=input("Last_name:");
	if l_name=="q":
		break;
	formatted_name=get_formatted_name(f_name, l_name);
	print("\nHello, " + formatted_name + "!");


def greet_users(names):
	"""向列表中的每位用户都发出简单的问候"""
	for name in names:
		msg = "Hellow, " + name.title() + "!";
		print(msg);
usernames=["hannah", "ty", "margot"];
greet_users(usernames);


# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ["iphone case", "rebot pendant", "dodecahedron"];
completed_models=[];
# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移动到表completed_models中
while unprinted_designs:
	current_design = unprinted_designs.pop();
	#模拟根据设计制作3D打印模型的过程
	print("Printing model " + current_design);
	completed_models.append(current_design);
print("\nThe following models have been printed:");
for completed_model in completed_models:
	print(completed_model);
print(completed_models)
print("\n");

def print_models(unprinted_designs, completed_models):
	"""模模拟打印每个设计，直到没有未打印的设计为止 打印每个设计后，都将其移动到表completed_models中"""
	while unprinted_designs:
		current_design = unprinted_designs.pop();
		#模拟根据设计制作3D打印模型的过程
		print("Printing model:" + current_design);
		completed_models.append(current_design);

def show_completed_models(completed_models):
	"""显示打印好的模型"""
	print("\nThe following models have been printed:");
	for completed_model in completed_models:
		print(completed_model);
		
unprint_designs = ["iphone case", "robot pendant", "dodecahedron"];
completed_models = [];
print_models(unprint_designs[:], completed_models);
show_completed_models(completed_models);
show_completed_models(unprint_designs)
