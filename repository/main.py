#En este segundo ejercicio, tendréis que crear un programa
# que tenga una clase llamada Alumno que tenga como atributos
# su nombre y su nota. Deberéis de definir los métodos para
# inicializar sus atributos, imprimirlos y mostrar un mensaje
# con el resultado de la nota y si ha aprobado o no.
class Alumno():
    nombre=None
    nota=0
    def inicializar(self, nombre, nota):
        self.nombre=nombre
        self.nota=nota

    def aprobado(self):
        if self.nota>4:
             print("El alumno ",self.nombre, "con nota ",self.nota," ha aprobado")
        else:
            print("El alumno ",self.nombre," con nota ",self.nota,"no ha aprobado")

alumno1=Alumno()
alumno1.inicializar("Pedro",4)
alumno1.aprobado()
alumno2=Alumno()
alumno2.inicializar("Sara",7)
alumno2.aprobado()
