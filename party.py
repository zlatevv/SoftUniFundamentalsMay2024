class Party:
    def __init__(self):
        self.people = []
    def return_info(self, people):
        return f"Going: {(', '.join(map(str,self.people)))}\nTotal: {len(self.people)}"
party = Party()
while True:
    name = input()
    if name == "End":
        break
    party.people.append(name)
print(party.return_info(party.people))