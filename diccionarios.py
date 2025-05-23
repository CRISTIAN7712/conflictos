usuario ={
    'Nombre':'Sara',
    'Edad':27,
    'Documento': 1003883,
    'Ciudad':'Bogota',
    'Direccion':'Calle 123'
}

print(usuario)

#usuario['Nombre']='Laura'
#usuario['Direccion']='Calle 123'

print(usuario)

for clave,valor in usuario.items():
    print(clave,":",valor)

usuario.update({'Ciudad':'Cucuta'})
print(usuario)

usuario.setdefault("Telefono")
print(usuario)

diccionario2 = dict.fromkeys(["a","b"],0)

print(diccionario2)