def racine(q, epsilon):
    a=c=0
    b=q+1
    while(b-a>=epsilon):
        c = (a + b)/2
        if(c ** c -q >= 0):
            b = c
        else:
            a = c
    return c

if __name__ == "__main__":
    q = int(input("Q : "))
    e = float(input("epsilon : "))
    print(racine(q,e))
