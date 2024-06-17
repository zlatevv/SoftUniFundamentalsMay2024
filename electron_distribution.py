electrons = int(input())
shells = []
index = 1
while electrons > 0:
    electron = 2 * (index ** 2)
    if electron > electrons:
        electron = electrons
    shells.insert(index - 1, electron)
    index += 1
    electrons -= electron
print(shells)
    