import time

a = int(input('Cuanto tiempo quieres poner?: '))
b = int(input('Cuantas series són?: '))
e = 0
for i in range(b):
    print('El tiempo sera de:', a)
    c = input('Escriba ya cuando desee comenzar: ')
    if c == 'ya':
        print('Enpieza en:')
        time.sleep(0.5)
        print('3')
        time.sleep(0.5)
        print('2')
        time.sleep(0.5)
        print('1')
        time.sleep(0.5)
        print('ya')
        time.sleep(0.5)
        print('Hellow word!')
    elif c == 'todavia no estoy listo':
        d = int(input('En cuanto tiempo deseea empezar:'))
        time.sleep(d)
        print('Enpieza en:')
        time.sleep(0.5)
        print('3')
        time.sleep(0.5)
        print('2')
        time.sleep(0.5)
        print('1')
        time.sleep(0.5)
        print('ya')
        for i in range(a):
            print(a)
            time.sleep(1)
            a -= 1
            e += 1
        a += e
