import random
caracteres = ["+","-","/","*","!","&","$","#","?","=","@","a","b","c","d","e","f","g","h","i","j","k","l","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","0"]
longuitud = int(input("que tan larga va a ser la clave: "))
clave = ""
for i in range(longuitud):
    caracter = random.choice(caracteres)
    clave = clave + caracter
print("tu clave es:")
print(clave)
