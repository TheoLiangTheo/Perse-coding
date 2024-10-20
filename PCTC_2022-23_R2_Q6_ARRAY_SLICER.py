array = []
n = '-1'
for x in range(10):
    l = []
    for y in range(10):
        n = str(int(n)+1)
        if len(n) == 1:
            n = '0' + n
        l.append(n)
    array.append(l)
def row(l1,l2):
    del(array[l1:l2])
def column(l1,l2):
    for x in range(len(array)):
        del(array[x][l1:l2])
numb_of_commands = int(input())
for x in range(numb_of_commands):
    command = list(input())
    order = command[0]
    bottom_limit = int(command[1])
    top_limit = int(command[-1]) + 1
    if order == 'r':
        row(bottom_limit,top_limit)
    else:
        column(bottom_limit,top_limit)
for x in range(len(array)):
    print(' '.join(array[x]))
