# Jeremy Gabriel Villamarín Molina

class Persona:
    '''
    Crear los objetos de tipo Persona
    '''
    def _init_(self, nombre, genero, ocupacion=None): #metodo que inicializa al objeto de tipo persona (constructor)
        self._nombre = nombre
        self._genero = genero
        self._ocupacion = ocupacion

    def _str_(self): #downders son sobre escritos
        return (f'Persona: [nombre: {self._nombre}, genero: {self._genero}, '
                f'ocupación: {self._ocupacion}]')

    def saludar(self):
        print(f'Hola soy {self._nombre}')


if _name_ == '_main_':
    obj_persona1 = Persona('Luis', 'M', 'Estudiante')
    print(obj_persona1._str_())
    obj_persona2 = Persona(genero='F', ocupacion='Tecnolog', nombre='Maria')
    print(obj_persona2)
    p3 = Persona(nombre='Jose', genero='M')
    print(p3)
    obj_persona1.saludar()
