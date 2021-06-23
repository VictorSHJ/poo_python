# Asignatura: Tienda y Productos
# Objetivos : Practica creando clases
#             Practicar asociaciones entre clases
#             Practica el código de modularización
# Comienza creando una clase de Tienda que tenga 2 atributos: un nombre y una lista de productos. El nombre debe proporcionarse en 
# el momento de la creación, pero la lista de productos debe estar vacía.
# A continuación, crea una clase de Producto que tenga 3 atributos: un nombre, un precio y una categoría. Todo esto debe proporcionarse en el momento de la creación.
# Veamos algunos métodos para nuestra clase Producto:
#     update_price(self, percent_change, is_increased) : actualiza el precio del producto. Si is_increased es True, el precio debería aumentar en el porcentaje de cambio proporcionado. Si es False, el precio debe disminuir en el cambio porcentual proporcionado.
#     print_info (self) : imprime el nombre del producto, su categoría y su precio.
# También demos algunos métodos a nuestra clase Tienda:
#     add_product (self, new_product) : toma un producto y lo agrega a la tienda
#     sell_product (self, id) : elimina el producto de la lista de productos de la tienda dada la identificación (suponga que id es el índice del producto en la lista) e imprima su información.
#     inflation(self, percent_increase) : aumenta el precio de cada producto por el percent_increase dado (¡use el método que escribió en la clase Product!)
#     set_clearance (self, category, percent_discount) : actualiza todos los productos que coinciden con la categoría dada reduciendo el precio en el percent_discount dado (¡use el método que escribió en la clase Product!)

#  Crear una clase de tienda con 2 atributos	
#  Crear una clase de producto con 3 atributos	
#  Agrega el método print_info a la clase de Producto	
#  Agrega el método update_price a la clase Product	
#  Agrega el método add_product a la clase Store	
#  Agrega el método sell_product a la clase Store	
#  Prueba tus clases creando una instancia de la Tienda y algunas instancias de la clase Producto, agrega esas instancias a la instancia de la tienda y luego prueba los métodos.	
#  NINJA BONUS: Agregue el método de inflación a la clase Store	
#  NINJA BONUS: Agregue el método set_clearance a la clase Store	
#     NINJA BONUS: modularice su código en 3 archivos separados	
#     SENSEI BONUS: actualice la clase de producto para dar a cada producto una identificación única. Actualice el método sell_product para aceptar la identificación única.
# 

from almacen.tienda import Tienda
from almacen.productos import Producto

print("***************** Creo la Tienda Quilicura *****************")
Quilicura = Tienda("Quilicura")
print(Quilicura)
print("***************** Creo la Tienda Huechuraba ****************")
Huechuraba = Tienda("Huechuraba")
print(Huechuraba)
print(" ")

Leche = Producto("Leche", 3000, "Lacteos")
Yogurt = Producto("Yogurt", 1000, "Lacteos")
Queso = Producto("Queso", 1000, "Lacteos")
Porotos = Producto("Porotos", 3000, "Legumbres")
Lentejas = Producto("Lentejas", 2500, "Legumbres")
Garbanzos = Producto("Garbanzos", 2500, "Legumbres")

print("******************** Creo los Productos ********************")
print(Leche)
print(Yogurt)
print(Queso)
print(Porotos)
print(Lentejas)
print(Garbanzos)

print("************** Agrego Productos a Tienda Quilicura *****************")
Quilicura.add_product(Leche)
Quilicura.add_product(Yogurt)
Quilicura.add_product(Queso)
print(Quilicura)

print("************** Agrego Productos a Tienda Huechuraba ****************")
Huechuraba.add_product(Porotos)
Huechuraba.add_product(Lentejas)
Huechuraba.add_product(Garbanzos)
print(Huechuraba)

print("********* Vendo el Segundo producto de la Tienda Quilicura *********")
Quilicura.sell_product(1)
print(Quilicura)

print("*********************** Actualizo precio 5% de Leche  **************")
Leche.update_price(5,True)
print(Leche)

print("******* Actualizo precio 8% los Precios de Tienda Quilicura  *******")
Quilicura.inflation(8)
