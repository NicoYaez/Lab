#Nicolas Yañez Ejercicio N°2
x = int(input("Ingrese el departamento que le interese: "))
x = str(x)
pisos = x[0:2]
num = x[2:4]

if pisos==20:
    if num==7 or num==3 :
        print ("El precio es 460")
    elif num==0 or num==4:
        print ("El precio es 320")
    else:
        print ("el precio es 400")
elif pisos==1:
    print ("El precio es 115")
elif num==7 or num==3:
    print ("El precio es 80")
elif num==0 or num==4:
    print ("El precio es 100")    
else: 
    if num==7 or num==3:
        print("El precio es 288")
    elif num==0 or num==4:
        print ("El precio es 200") 
    else:
        print ("El precio es 250")
