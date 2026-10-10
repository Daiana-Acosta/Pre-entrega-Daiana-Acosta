productos = []
while True:
    print("="*20)
    print("Logan's shop") 
    print("="*20)
    print("1. Agregar productos")
    print("2. Mostrar productos")        
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")


    match input("Elegi una opción (1-5): ").strip():

       case  "1":
        
        print("Agregar productos")

        nombre = input("Nombre del producto:").strip()
        while nombre == "":
            print("Este espacio no puede estar vacio.")
            nombre = input("Nombre del producto:").strip()

        categoria = input("Categoria del producto:").strip()
        while categoria == "":
            print("Este espacio no puede estar vacio.")
            categoria = input("Categoria del producto: ").strip()

        precio_str = input("Precio (sin centavos): ").strip()
        while not precio_str.isdigit():
            print("Este espacio no puede estar vacio.")
            precio_str = input("Precio (sin centavos): ").strip()
        precio = int(precio_str)

        datos = [nombre,categoria,precio]
        productos.append(datos)
       case "2":
        print ("Lista de productos")
        if len(productos) == 0:
         print("Todavía no hay productos cargados.")

        else:
         for i in range(len(productos)):
            print(f"ID: {i+1}")
            print(f"-Nombre: {productos[i][0]}")
            print(f"-Categoría: {productos[i][1]}")
            print(f"-Precio: ${productos[i][2]}")
            print("------------------------")
        
        
       case "3":
        
        print ("Busqueda de producto")

        if len(productos) == 0:
            print("Este campo no puede estar vacio.")
        else:
            busqueda = input("Nombre del producto a buscar: ").strip().lower()

            while busqueda == "":
                print("Este campo no puede estar vacio.")
                busqueda = input("Nombre del producto a buscar: ").strip().lower() # moUse

            encontrado = 0
            for i in range(len(productos)):
                if busqueda in productos[i][0].lower():
                    print(f"ID:{i+1}\n-Nombre: {productos[i][0]}\n-Categoria: {productos[i][1]}\n-Precio: ${productos[i][2]}")
                    encontrado += 1

            if encontrado == 0:
                print("Producto inexistente")
            else:
                print(f"Productos encontrados {encontrado}")

       case "4":
    
           print("Eliminar producto")
           if len(productos) == 0:
            print("Todavia no hay productos cargados.")
           else:
            for i in range(len(productos)):
                print(f"{i+1}. {productos[i][0]} - {productos[i][1]} - ${productos[i][2]}")  

            id_elminar = input("Numero de producto a elminar: ").strip().lower()

            while not id_elminar.isdigit():
                print("Error: ngresa un numero")
                id_elminar = input("Numero de producto a elminar: ").strip().lower()
            posicion = int(id_elminar) - 1
            eliminado = productos.pop(posicion)
            print(f"se elimino el producto: {eliminado[0]} ")

       case "5":
        print("¡Gracias por usar nuestro sistema!")
       case _:
        print ("Esta opcion no es valida.")
          