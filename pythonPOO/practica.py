# crea una clase llamada Producto
# nombre, unidades y precio
# creas un producto camisa, 10, 9.95 de precio
# muestra el nombre de producto por consola

# crea un método de infoProducto. Muestra el nombre, unidades, precio y inventario valorado (uxp)

# práctica de sobreescritura.

# crea una clase llamada Servicio

# tiene un método llamado consultarDetalle que muestra. el servicio es básico.
# la empresa tiene dos servicios. estándar y premium. Son dos clases que derivan de Servicio
# la clase Estandar y Premium tienen un método llamado consultarDetalle y explican que son
# servicio estándar y premium respectivamente.
# pide por consola un servicio. Elegimos premium y te muestra el resultado de consultarDetalle
class Products:
    def __init__(self, nombre, unidades, precio):
        self.nombre = nombre
        self.unidades = unidades
        self.precio = precio

    def infoProducto(self):
        print(f'Detalles del producto: {self.nombre}, {self.unidades} unidades, {self.precio}€. Inventario valorado={self.unidades * self.precio}')


producto1 = Products('camisa', 10, 9.95)
print(f'El nombre del producto es {producto1.nombre}')
producto1.infoProducto()

class Servicio:
    def consultarDetalle(self):
        print('El servicio es básico')

class Estandar(Servicio):
    def consultarDetalle(self):
        print('El servicio estándar contiene limpieza base de la habitación, cambio de sábanas y cambio de toallas.')


class Premium(Servicio):
    def consultarDetalle(self):
        print('El servicio Premium contiene lo mismo que el servicio Estándar pero con comidas incluidas')

servicio1 = Premium()
servicio1.consultarDetalle()