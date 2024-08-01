# Condicionales simples

# temperature = 40

# if temperature > 35:
    #print('Aviso por alta temperatura')


# Condicionales anidadas

'''temperature = 28

if temperature < 20:
    if temperature < 10:
        print('Nivel azul')
    else:
        print('Nivel verde')
else:
    if temperature < 30:
        print('Nivel naranja')
    else:
        print('Nivel rojo') '''


'''temperature = 35

if temperature < 30:
    fire_risk = 'LOW'
else:
    fire_risk = 'HIGH'

print(fire_risk)'''


# operadores logicos

'''x = 8

x > 4 or x > 12  # True or False

x < 4 or x > 12  # False or False

x > 4 and x > 12  # True and False

x > 4 and x < 12  # True and True

not(x != 8)  # not False'''


'''power = 10
signal_4g = 60

power > 25 and signal_4g > 10'''


#match-case

'''color = '#AF549B'

match color:
    case '#FF0000':
        print('🔴')
    case '#00FF00':
        print('🟢')
    case '#0000FF':
        print('🔵')
    case _:
        print('Unknown color!')'''


#patrones avanzados

'''point = (2, 5)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')

point = (3, 1, 7)

match point:
    case (x, y):
        print(f'({x},{y}) is in plane')
    case (x, y, z):
        print(f'({x},{y},{z}) is in space')'''


#operador morsa

'''radius = 4.25
perimeter = 2 * 3.14 * radius
if perimeter < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)'''

'''radius = 4.25
if (perimeter := 2 * 3.14 * radius) < 100:
    print('Increase radius to reach minimum perimeter')
    print('Actual perimeter: ', perimeter)'''
