version = input().split(".")
new_version = int(''.join(version)) + 1
print('.'.join(str(new_version)))