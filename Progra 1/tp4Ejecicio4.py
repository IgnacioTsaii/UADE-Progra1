def numeroRomano(numeroE):
    m = ["M", "MM", "MMM"]
    c = ["C", "CC", "CCC", "CD", "D",
         "DC", "DCC", "DCCC", "CM "]
    x = ["X", "XX", "XXX", "XL", "L",
         "LX", "LXX", "LXXX", "XC"]
    i = ["I", "II", "III", "IV", "V",
         "VI", "VII", "VIII", "IX"]
  
    miles = m[numeroE // 1000 -1]
    centenas = c[(numeroE % 1000) // 100 -1]
    decenas = x[(numeroE % 100) // 10 -1]
    unidades = i[numeroE % 10 -1]
    
  
    respuesta = (miles + centenas +
           decenas + unidades)
    
    return respuesta


numero = int(input('Ingrese el numero para convertir en romano: '))
while numero > 3999:    
    print('Error! El número tine que ser entre 0 y 3999')
    numero = int(input('Ingrese el numero para convertir en romano: '))
if numero == 0:
    print('El valor en números romanos es: N')
else:
    print("El valor en números romanos es: "+ str(numeroRomano(numero)))  