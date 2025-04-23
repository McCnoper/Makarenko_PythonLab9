def cosDist(speed,timeY):
    dist=speed*timeY
    return dist

def simpGrav(mass1,mass2):
    grav=mass1*mass2
    return grav

def timeDilation(speed,timeS):
    dilation=timeS/(1-speed)
    return dilation

x=True
while x:
    try:
        choice = int(input("1-Cosmic distance, 2-Simplified gravity, 3-Time dilation Approximation: "))
        if 0<choice<3:
            raise ValueError
        match choice:
            case 1:
                speed=float(input("Enter Fraction of speed of light(0-1): "))
                timeY=float(input("Enter time in years: "))
                print(cosDist(speed,timeY))
            case 2:
                mass1=int(input("Enter mass of first object: "))
                mass2=int(input("Enter mass of second object: "))
                print(simpGrav(mass1,mass2))
            case 3:
                speed=float(input("Enter Fraction of speed of light(0-1): "))
                timeS=float(input("Enter time in seconds: "))
                print(timeDilation(speed,timeS))
    except ValueError:
        print("Enter only numbers in proposed limit")
    x=1-int(input("Exit? 1-Yes, 2-No"))
    if -1<x<2:
        x=0
