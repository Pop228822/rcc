x = int(input())
y = int(input())

def ord(x_f, y_f):
    if x_f > 0 and y_f > 0:
        print("I")
    elif x_f < 0 and y_f > 0:
        print('II')
    elif x_f < 0 and y_f < 0:
        print('III')
    else:
        print('IV')
ord(x, y)