class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []
    def __str__(self):        
        return (f"Nombre Tienda: {self.nombre}, Catalogo: {self.catalogo}")
    def add_product (self, new_product):
        self.catalogo.append(new_product)
        return self
    def sell_product (self, id):
        print (f"<<< Producto {self.catalogo[id]} Vendido >>>")
        self.catalogo.pop(id)
        return self
    def inflation(self, percent_increase):
        for x in self.catalogo:
            print(f"Actualizo Precio de {x}")
            x.update_price(percent_increase, True)
        return self
# actualiza todos los productos que coinciden con la categoría dada reduciendo el precio en el percent_discount dado (¡use el método que escribió en la clase Product!)        
    def set_clearance (self, category, percent_discount):
        return self