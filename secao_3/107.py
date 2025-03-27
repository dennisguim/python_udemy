def soma(x, y, z=0):
    if z != 0:
        print(f'{x=} + {y=} + {z=}', x + y + z)
    else:
        print(f'{x=} + {y=}', x + y)

soma(2, 3)

soma(1, 4, 5)