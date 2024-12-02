def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode ="w") as write_file:
        write_file.write(file_content)        

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode="a") as append_file:
        append_file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt") as read_me:
        return read_me.read()
