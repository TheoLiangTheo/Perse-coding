def get_score(info):
    points = int(info[1])*2 + int(info[2])
    info.append(points)
    return info, points
n = int(input())
employees = []
max_points = 0
for x in range(n):
    employee_info = input().split(' ')
    employee_info, points = get_score(employee_info)
    if points > max_points:
        max_points = points
    employees.append(employee_info)
goodemployees = []
for employee in employees:
    if employee[-1] == max_points:
        goodemployees.append(employee)

winner = ""
biggest_colour_sale = -1
for employee in goodemployees:
    if int(employee[1]) > biggest_colour_sale:
        biggest_colour_sale = int(employee[1])
        winner = employee[0]
print(winner)