libros = [('El perfume','Suskind','Misterio'),
          ('La metamorfosis', 'Kafka', 'Novela'),
          ('Misery','Stephen King', 'Misterio')]

clasificacion = input("Ingrese el genero literario: ").title()
resultado = [libro[0] for libro in libros if libro[2] == clasificacion]
print(resultado if resultado else f"No hay libros con el genero {clasificacion}")

