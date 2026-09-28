# Nombre del estudiante: Cielo Tatiana Ramirez Garcia
# Grupo: 213022_848
# Programa: Introduccion a la Programacion - UNAD - Fase 2
# Problema 4: Calculo valor final segun categoria con IVA
# Codigo Fuente: autoria propia

# R1: Definir constantes (requisito de la guia)
IVA = 0.19
RECARGO_LUJO = 0.05

def main():
    # R2: Solicitar precio_base
    try:
        precio_base = float(input("Ingrese el precio base del producto: $"))
    except ValueError:
        print("Error: Debe ingresar un valor numerico.")
        return  # FIN 1 - Error por tipo de dato

    # Validacion: precio_base <= 0 ?
    # Camino SI (se estanca) - Como me dijiste
    if precio_base <= 0:
        print("Error: El precio debe ser mayor que 0. Programa finalizado.")
        return  # FIN 1 - Se estanca aqui, NO sigue a pedir codigo

    # Camino NO (sigue todo) - Si tiene numero superior a 0
    # R3: Solicitar codigo de categoria
    print("\n--- Categorias ---")
    print("1 - Basico (no paga IVA)")
    print("2 - Estandar (paga IVA 19%)")
    print("3 - Lujo (paga IVA 0.19 + recargo 5%)")
    
    codigo = input("Ingrese el codigo de categoria (1/2/3): ").strip()

    # Validacion: codigo valido?
    if codigo not in ["1", "2", "3"]:
        print("Error: Codigo de categoria invalido. Programa finalizado.")
        return  # FIN 2 - Error de codigo, tambien se estanca

    # R4: Calcular valor final segun categoria
    # Este es el camino que SI continua
    if codigo == "1":
        valor_final = precio_base
        categoria = "Producto basico"
    elif codigo == "2":
        valor_final = precio_base * (1 + IVA)  # 1.19
        categoria = "Producto estandar"
    else:  # codigo == "3"
        valor_final = precio_base * (1 + IVA + RECARGO_LUJO)  # 1.24
        categoria = "Producto de lujo"

    # R5: Mostrar resultado
    print("\n--- Resultado Final ---")
    print(f"Categoria: {categoria}")
    print(f"Precio base: ${precio_base:,.2f}")
    print(f"Valor final a pagar: ${valor_final:,.2f}")
    
    return  # FIN 3 - Fin normal, todo salio bien

# Ejecucion
if __name__ == "__main__":
    main()