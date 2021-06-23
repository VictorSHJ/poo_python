class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
    def update_price(self, percent_change, is_increased): 
        if is_increased:
            self.precio += (self.precio * percent_change) / 100
        else:
            self.precio -= (self.precio * percent_change) / 100
        return self
    def print_info(self):
        print (f"Nombre Producto: {self.nombre}, Precio: {self.precio}, Categoria: {self.categoria}")
    def __str__(self):
        return (f"Nombre Producto: {self.nombre}, Precio: {self.precio}, Categoria: {self.categoria}")