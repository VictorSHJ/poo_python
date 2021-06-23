# Asignatura: MathDojo
# Objetivos : Practica creando una clase y creando nuevas instancias
#             Practica los métodos de encadenamiento
#             Practica escribir funciones flexibles que pueden tomar un número variable de argumentos.
# Crea una clase de Python llamada MathDojo que tenga un atributo, resultado y 2 métodos: sumar y restar . Los 2 métodos deben tomar al menos 1 parámetro, pero podrían tomar muchos más.
# Crear una clase de MathDojo	
# Escriba el método add y pruébelo llamándolo 3 veces, con diferentes números de argumentos cada vez	
# Escriba el método de subtract y pruébelo llamándolo 3 veces, con diferentes números de argumentos cada vez	
# Asegúrese de poder encadenar los métodos como se demostró anteriormente	
# BONUS: Calcule la desviación estandar (existe alguna diferencia)	

class MathDojo:
    def __init__(self):
    	self.result = 0
    def add(self, num, *nums):
        self.result += num
        for nro in nums:
            self.result += nro
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for nro in nums:
            self.result -= nro
        return self
    
md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	# debe imprimir 5

x = md.add(10,30,20).result
print(x)	# debe imprimir 65

x = md.subtract(5,2,3).result
print(x)	# debe imprimir 55