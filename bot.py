contacts = {}

# Декоратор для обробки помилок та виведення повідомлень користувачу.
def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name"
        except ValueError:
            return "Give me name and phone please"
        except IndexError:
            return "Invalid command. Use 'add', 'change', 'phone', 'show all', or 'exit'."
    return wrapper

# Обробник команди 'hello'.
@input_error
def hello_command():
    return "How can I help you?"

# Обробник команди 'add'.
@input_error
def add_contact_command(params):
    name, phone = params
    contacts[name] = phone
    return f"Contact {name} added with phone number {phone}"

# Обробник команди 'change'.
@input_error
def change_contact_command(params):
    name, phone = params
    if name in contacts:
        contacts[name] = phone
        return f"Phone number for {name} changed to {phone}"
    else:
        return f"Contact {name} not found"

# Обробник команди 'phone'.
@input_error
def phone_command(name):
    if name in contacts:
        return f"Phone number for {name} is {contacts[name]}"
    else:
        return f"Contact {name} not found"

# Обробник команди 'show all'.
@input_error
def show_all_command():
    if not contacts:
        return "No contacts found"
    else:
        contact_list = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return contact_list

# Головна функція для взаємодії з користувачем.
def main():
    while True:
        user_input = input("Enter a command: ").strip().lower()
        if user_input in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif user_input == "hello":
            print(hello_command())
        elif user_input.startswith("add"):
            try:
                _, name, phone = user_input.split(" ")
                print(add_contact_command((name, phone)))
            except ValueError:
                print("Invalid 'add' command. Usage: add [name] [phone]")
        elif user_input.startswith("change"):
            try:
                _, name, phone = user_input.split(" ")
                print(change_contact_command((name, phone)))
            except ValueError:
                print("Invalid 'change' command. Usage: change [name] [phone]")
        elif user_input.startswith("phone"):
            try:
                _, name = user_input.split(" ")
                print(phone_command(name))
            except ValueError:
                print("Invalid 'phone' command. Usage: phone [name]")
        elif user_input == "show all":
            print(show_all_command())
        else:
            print("Invalid command. Use 'hello', 'add', 'change', 'phone', 'show all', or 'exit'.")

if __name__ == "__main__":
    main()
