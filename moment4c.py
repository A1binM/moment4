from math import sqrt
 

Counter = 0 

sida1 = [] 

sida2 = [] 

Area = [] 

Volym = []

höjd = [] 

Kvadrat = []

def area(b,a): 
    a1 = b*a 
    return a1 

def volym(c,b,a): 
    v1 = c*b*a 
    return v1 

def kvadrat(a,b): 
    if a == b: 
        return "ja" 

while True: 
    svar= input("Vill du göra beräkningar? J / N?").upper() 
    if svar == "J": 
        Counter +=1 


        b=int(input("Ange ena sidans längd!: ")) 
        if b < 0: 
            b = 1 
        sida1.append(b) 

        a=int(input("Ange andra sidans längd!: "))
        if a < 0: 
            a = 1 
        sida2.append(a) 

        c=int(input("Ange att heltal för höjd för rektangel!: ")) 
        if c < 0: 
            c = 1 
        höjd.append(c) 


        Area.append(area(a,b)) 
        Volym.append(volym(c,b,a)) 
        Kvadrat.append(kvadrat(a,b)) 

        if kvadrat(a,b) == "ja": 
            print(f"Arean på rektangel med sidorna {b} och {a} är {area(b,a)} och det är en kvadrat.") 
        else: 
            print(f"Arean på rektangel med sidorna {b} och {a} är {area(b,a)}")


        print("Höjd | Volym") 
        print("------------") 
        for h in range(1,11):
            print(h,"|",b*a*h) 

    else: 
        for d in range(Counter): 
            if Kvadrat[d] == "ja": 
                print(f"Rektangeln har sidorna {sida1[d]} och {sida2[d]} vilket gör att arean är {Area[d]},det betyder rektangeln är en kvadrat.") 
            else: 
                print(f"Rektangeln har sidorna {sida1[d]} och {sida2[d]} vilket gör att arean är {Area[d]}")
        break