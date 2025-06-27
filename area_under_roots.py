import math

def moivre(a=1,b=1,n=1): #outputs two lists: of the real, and imaginary parts of the roots, using the algebric form
    xs = []
    ys = []

    def real(theta=0 ,module=0,n=0,k=0): # calculates real part of one specified root
        real = pow(module, (1/n)) * (math.cos((theta + 2*k*math.pi)/n))
        return real

    def imag(theta=0,module=0,n=0,k=0): # calculates imaginary part of one specified root
        imag = pow(module, (1/n)) * (math.sin((theta + 2*k*math.pi)/n))
        return imag

    #this next section calculates the angle and module of the polar representation of the input number
    #---
    if b == 0:
        if a > 0:
            theta = int(0)
        else:
            theta = math.pi
    elif a == 0:
        if b > 0:
            theta = math.pi/2
        else:
            theta = 3*math.pi/2
    else:
        theta = math.atan(b/a)

    module = math.sqrt((b*b) + (a*a))
    #---

    for k in range(n): #inserts those and n into those first two functions, and makes the lists
        xs.append(round((real(theta,module,n,k)), 10))
        ys.append(round((imag(theta,module,n,k)), 10))

    return xs, ys

#following this format to get areas using coords of points: [(x1*y2 + x2*y3 + x3*y1) - (y1*x2 + y2*x3 + y3*x1)]/2

def sum(a=1,b=1,n=1): #defines "(x1*y2 + x2*y3 + x3*y4...)"
    x = 0
    for (ind, i) in enumerate(moivre_list[0], start=0):
        try:
            x = x + (moivre_list[0][ind] * moivre_list[1][(ind+1)])
        except:
            x = x + (moivre_list[0][ind] * moivre_list[1][0])
    return x

def sub(a=1,b=1,n=1): #defines (y1*x2 + y2*x3 + y3*x4...)"
    y = 0
    for (ind, i) in enumerate(moivre_list[0], start=0):
        try:
            y = y + (moivre_list[1][ind] * moivre_list[0][(ind+1)])
        except:
            y = y + (moivre_list[1][ind] * moivre_list[0][0])
    
    return y

#here's where it actually starts running!

print("Following the model n√(a+bi)")
print("")

while 0 == 0: #loop

    try: #checking if values won't crash program
        a = float(input("a="))
    except:
        print("\"n\" must be a number! Try again.")
    else:
        try:
            b = float(input("b="))
        except:
            print("\"n\" must be a number! Try again.")
        else:
            try:
                n = int(input("n="))
            except:
                print("\"n\" must be an integer! Try again.")
            else:
                moivre_list = moivre(a,b,n) #calls the program that makes lists and saves them
                area = (sum(a,b,n) - sub(a,b,n))/2 #does the pseudo-matrix area trick

                print("Area = " + str(area))

    print()
    print("Next:")
    print()
