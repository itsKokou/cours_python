def codage(text):
    ch=""
    for i in text:
        if(ord(i)==32):
            x=49
            d=1
        elif (ord(i)>=48 and ord(i)<=57 ) :
            x=ord(i)+17  #ord() => code asci
            d=1   #chr() => caractere en fonction de ascii
        elif ((ord(i)>64 and ord(i)<80) or (ord(i)>64+32 and ord(i)<80+32) ) : 
            x=50
            d=ord(i)-64
            if(ord(i)>=80):
                d=ord(i)-64-32
            while(d>3):
                d-=3
                x+=1
        elif ((ord(i)>79 and ord(i)<84) or (ord(i)>79+32 and ord(i)<84+32)):
            x=55
            d=ord(i)-79
            if(ord(i)>=84):
                d=ord(i)-79-32
        elif ((ord(i)>83 and ord(i)<87) or (ord(i)>83+32 and ord(i)<87+32)):
            x=56
            d=ord(i)-83
            if(ord(i)>=87):
                d=ord(i)-83-32
        elif ((ord(i)>86 and ord(i)<91) or (ord(i)>86+32 and ord(i)<91+32)):
            x=57
            d=ord(i)-86
            if(ord(i)>=91):
                d=ord(i)-86-32   
        while(d!=0):
            ch+=chr(x)
            d-=1
    return ch

ok=codage("10 Francs")
print(ok)

def decodage(code):
    ch=""
    for i in code:
        if(ord(i)==49):
            x=32
            d=1
        elif (ord(i)>=65 and ord(i)<=74 ) :
            x=ord(i)-17  #ord() => code asci
            d=1   #chr() => caractere en fonction de ascii
        while(d!=0):
            ch+=chr(x)
            d-=1
    return ch
oki=decodage("BA1")
print(oki)