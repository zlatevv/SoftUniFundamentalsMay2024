file_path = input().split("\\")
file = file_path[-1].split(".")
file_name = file[0]
file_extension = file[1]
print(f"File name: {file_name}\nFile extension: {file_extension}")