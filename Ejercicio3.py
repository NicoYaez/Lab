#Nicolas Yañez Ejercicio N°3
a= float(input("Ingrese angulo 1: "))
b= float(input("Ingrese angulo 2: "))
c=180-(a+b)
if a==90 or b==90 or c==90:
    print("Es un triangulo rectangulo")
elif a>90 or b>90 or c>90:
    print("Es un triangulo obtusangulo")
elif a<90 or b<90 or c<90:
    print("Es un triangulo acutangulo")
else:
    print("Este no es un triangulo")
