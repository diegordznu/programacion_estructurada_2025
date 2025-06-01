# 1er utilizar los modulos
import modulo

print(modulo.saludar("Diego Rodriguez"))

# 2da forma de utilizar modulos

from modulo import saludar,borrarPantalla

borrarPantalla()
print(saludar("Daniel Contreras Renecio"))

nombre=input("Ingresa el nombre del contacto: ")
telefono=input("Ingresa su numero de telefono: ")
nom,tel=modulo.solicitarDatos4(nombre,telefono)
print(f"\t Nombre completo: {nom} \n\tTelefono: {tel}")
