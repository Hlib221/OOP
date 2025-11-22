from my_class import MyName

print("\n=== Starting object creation ===\n")

names = ["Gleb", "Dima", None]
all_names = {name: MyName(name) for name in names}
all_names["MyName"] = MyName("YourName")

for name, person in all_names.items():
    print(f"{'='*60}")
    print(f"Object: {person}")
    print(f"Name attribute: {person.name} / ID: {person.my_id}")
    print(f"Type of whoami: {type(person.whoami)} -> {person.whoami}")
    print(f"Type of create_email: {type(person.create_email)} -> {person.create_email()}")
    print(f"Static method say_hello: {person.say_hello()}")
    print(f"Class variable total_names: {MyName.total_names} (class) / {person.total_names} (object)")
    print(f"{'='*60}\n")

print(f"\nTotal names created: {MyName.total_names}\n")

for person in all_names.values():
    print(f"Letters in name '{person.name}': {person.count_name_letters()}")

print("\n=== Calling static method with custom message ===")
print(MyName.say_hello("Hello!"))

print("\n=== Changing email domain for Gleb ===")
obj = all_names["Gleb"]
obj.change_email_domain("newdomain")
print(f"Updated email: {obj.my_email}")

print("\nFull names of all objects:")
for person in all_names.values():
    print(person.full_name)

print("\nSaving all objects to files...")
for person in all_names.values():
    person.save_to_file()

print("\n=== All done! ===")
