from paquete1 import modulos

print(modulos.saludar("Diego Rodriguez"))

modulos.borrarPantalla()
nombre,tel=modulos.solicitarDatos2()
print(f"\n..:Agenda Telefonica:..\n\t\tNombre: {nombre}\n\t\t Telefono: {tel}")
modulos.esperarTecla()