import dataset
miBase = dataset.connect("sqlite:///datos.db")
tabla = miBase["Productos"]

while True:
    opciones = input("""
    
    ***********************
    L - Listar
    A - Agregar 
    Q - Quitar por nombre
    I - Quitar por ID
    B - Buscar primero
    T - Buscar todo 
    P - Actualizar producto
    ***********************
    S - Salir
    
    """).upper()
    match opciones:  
        
        case "P":
            ingresaID = int(input("\nID de producto a actualizar: "))
            nombreAct = input("\nNombre a actualizar: ")
            precioAct = float(input("\nNuevo precio: "))
            categoriaAct = input("\nActualizar categoria: ")
            
            actualizacion = {"id":ingresaID,"Nombre":nombreAct,"Precio":precioAct,"Categoria":categoriaAct}
            tabla.upsert(actualizacion,keys="id")
            
            for cosa in tabla:
                            print(f"ID: {cosa['id']} | Nombre: {cosa['Nombre']} | Precio: {cosa['Precio']} | Categoria: {cosa['Categoria']}")
            
            
        
        
        case "B":
            busco = input("\nProducto a buscar: ").strip()
            encontrado = tabla.find_one(Nombre=busco)
            print(f'{busco} esta en la posicion {encontrado["id"]}')
        
        case "T":
            busco = input("\nBuscar en toda la base: ").strip()
            encontrado = tabla.find(Nombre=busco)
            
            for cosa in encontrado:
                print(f'{busco} esta en el ID: {cosa["id"]}')
                
        case "S":
            break
            
        case "A":
            nombreProducto = input("\nNombre: ")
            precioProducto = float(input("\nPrecio: "))
            categoriaProducto = input("\nCategoría: ")

            productoAgregar = {"Nombre":nombreProducto,"Precio":precioProducto,"Categoria":categoriaProducto}

            # diccionarios
            tabla.insert(productoAgregar)

        
        case "L":
            for cosa in tabla:
                print(f"ID: {cosa['id']} | Nombre: {cosa['Nombre']} | Precio: {cosa['Precio']} | Categoria: {cosa['Categoria']}")

               

        case "Q":
            quitarProducto = input("\nProducto a quitar: ")
            tabla.delete(Nombre=quitarProducto)
            print(f"*** {quitarProducto} eliminado con éxito ***")
        
        case "I":
            quitarProducto = int(input("\nId de producto a quitar: "))
            tabla.delete(id=quitarProducto)
            print(f"*** Producto con ID: {quitarProducto} eliminado con éxito ***")
