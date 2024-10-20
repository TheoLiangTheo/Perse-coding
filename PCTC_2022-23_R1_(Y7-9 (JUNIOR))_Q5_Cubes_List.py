limit = int(input())
x = 1
while True:
    cube = x*x*x
    if cube > limit:
        break
    print(cube)
    x += 1
