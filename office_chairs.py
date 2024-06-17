rooms = int(input())
flag = False
free_chairs = 0
for room in range(1, rooms + 1):
    chairs, visitor = input().split()
    diff = abs(len(chairs) - int(visitor))
    if len(chairs) < int(visitor):
        flag = True
        print(f"{diff} more chairs needed in room {room}")
    else:
        free_chairs += diff
if not flag:
    print(f"Game On, {free_chairs} free chairs left")