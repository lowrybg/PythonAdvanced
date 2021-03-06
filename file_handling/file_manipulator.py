import os


def create(file_name):
    with open(file_name, "w") as file:
        file.write("")


def add_content(file_name, content):
    with open(file_name, "a") as file:
        file.write(content+"\n")


def replace_content(file_name, content, replace_with):
    try:
        with open(file_name, "r+") as file:
            text = ''.join(file.readlines())
            replaced_content = text.replace(content, replace_with)
            file.seek(0)
            file.writelines(replaced_content)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(file_name):
    try:
        os.remove(file_name)
    except FileNotFoundError:
        return "An error occurred"


mapper = {
    "Create": create,
    "Add": add_content,
    "Replace": replace_content,
    "Delete": delete_file,

}

command_data = input().split('-')
while not  command_data[0] == "End":
    command, command_args = command_data[0], command_data[1:]
    mapper[command](*command_args)
    command_data =input().split('-')
