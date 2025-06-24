import os
from time import sleep as zzz

def borrar_pantalla():
    if os.name=="nt":
        os.system("cls")
        return ""
    if os.name=="posix":
        os.system("clear")
        return ""
    
def alerta(mensaje:str,tiempo=2.5):
    """Imprime un mensaje, espera tiempo y limpia la terminal."""
    print(mensaje)
    zzz(tiempo)
    borrar_pantalla()

menu=f"\n1.- Comprar entrada.\n2.- Consultar comprador.\n3.- Cancelar compra.\n4.- Salir.\n"
registros={"compradores":[]}


def validar_codigo(codigo:str):
    """Retorna True si el codigo tiene al menos 1 mayuscula y 1 numero"""
    mayuscula=False
    numero=False
    for i in codigo:
        if not mayuscula and i.isupper():
            mayuscula=True
        if not numero and i.isdigit():
            numero=True
        if numero and mayuscula: return True
    return False


def verificar_existencias(palabra_clave:str)->dict:
    """Retorna una existencia si la hay, de otro modo retorna None"""
    for existencia in registros["compradores"]:
        if palabra_clave!=existencia["nombre"]: continue
        return existencia
    return None


def nombre_comprador()->str:
    """Pide ingresar un tipo de entrada, hace las validaciones correspondientes."""
    while True:
        nombre=input("\nIngrese su nombre (Para cancelar ingrese 0): ").lower()
        if nombre=="0": return None
        if not nombre:
            alerta("No puede dejar este campo vacío.")
            continue
        if not nombre.isalpha():
            alerta("El nombre no puede contener espacios o números.")
            continue
        if 3>len(nombre):
            alerta("El nombre debe tener al menos 3 letras.")
            continue
        if verificar_existencias(nombre):
            alerta("El nombre ya está en uso. Vuelva a intentarlo.")
            continue
        return nombre

    
def tipo_entrada()->str:
    """Pide ingresar un tipo de entrada, hace las validaciones correspondientes."""
    while True:
        entradas_disponibles={"g":"general","v":"vip"} # Idealmente dentro de la función ya que es algo propio de la misma.
        entrada=input("\n[G] - General\n[V] - Vip.\nIngrese el tipo de entrada que desea comprar. (Para regresar, ingrese 0): ").lower()
        if entrada=="0": return None
        if not entrada:
            alerta("No puede dejar este campo vacío.")
            continue
        if entrada not in entradas_disponibles:
            alerta("Por favor seleccione una opción válida [G/V].")
            continue
        entrada=entradas_disponibles[entrada]
        return entrada


def codigo_confirmacion():
    while True:
        codigo=input("\nIngrese el código de confirmación (Para cancelar ingrese 0): ")
        if codigo=="0": return None
        if not codigo:
            alerta("No puede dejar este campo vacío.")
            continue
        if not codigo.isalnum():
            alerta("El código solo puede contener letras y números.")
        if not validar_codigo(codigo):
            alerta("El codigo debe tener al menos una mayuscula y un número.")
            continue
        return codigo


def nueva_compra()->bool:
    registrar_comprador=nombre_comprador()
    borrar_pantalla()
    if not registrar_comprador: return False
    registrar_entrada=tipo_entrada()
    borrar_pantalla()
    if not registrar_entrada: return False
    registrar_codigo=codigo_confirmacion()
    borrar_pantalla()
    if not registrar_codigo: return False
    registros["compradores"].append(
        {
            "nombre":registrar_comprador,
            "entrada":registrar_entrada,
            "codigo":registrar_codigo
        }
    )
    return True


def mostrar_datos():
    palabra_clave=verificar_existencias(input("Ingrese el nombre del comprador que desea encontrar: "))
    if not palabra_clave: alerta("No hubieron resultados en la búsqueda.")
    print(f"\nNombre del comprador: {palabra_clave["nombre"]}\nTipo de entrada: {palabra_clave["entrada"]}\nCodigo de verificacion: {palabra_clave["codigo"]}\n\n")
    return palabra_clave


def animacion_cerrando_programa():
    for i in range(3):
        alerta("Cerrando programa... |",0.2)
        alerta("Cerrando programa... /",0.2)
        alerta("Cerrando programa... -",0.2)
        alerta("Cerrando programa... \\",0.2)

def principal():
    while True:
        borrar_pantalla()
        opcion=input(f"{menu}Ingrese una opción: ")
        borrar_pantalla()
        if opcion=="1": nueva_compra()
        elif opcion=="2":
            mostrar_datos()
            input("Presione ENTER para continuar")
        elif opcion=="3":
            cancelar_compra=mostrar_datos()
            if input("¿Desea borrar estos datos? [S/N] (Por defecto: n)").upper()!="S": continue
            registros["compradores"].remove(cancelar_compra)
        elif opcion=="4":
            break
        else:
            alerta("Por favor ingrese una opcion válida [1-4]")
    animacion_cerrando_programa()
principal()
