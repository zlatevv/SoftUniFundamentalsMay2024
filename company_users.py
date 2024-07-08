companies = {}

while True:
    data = input().split(" -> ")
    if data[0] == "End":
        break
    company = data[0]
    employee_id = data[1]
    if company not in companies:
        companies[company] = set()
    companies[company].add(employee_id)

for company, ids in companies.items():
    print(company)
    for id in sorted(ids):
        print(f"-- {id}")

