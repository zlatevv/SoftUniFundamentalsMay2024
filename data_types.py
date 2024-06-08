def data_type(data, number):
    if data == "int":
        return int(number) * 2
    elif data == "real":
        return f"{float(number) * 1.5:.2f}"
    elif data == "string":
        return f"${number}$"
command = input()
number = input()
print(data_type(command, number))