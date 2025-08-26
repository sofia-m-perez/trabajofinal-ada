from catalogo import Pelicula, CatalogoPeliculas

def menu():
    print("\n--- 🎬 Catálogo de Películas ---")
    nombre_catalogo = input("Ingrese el nombre del catálogo: ").strip()
    catalogo = CatalogoPeliculas(nombre_catalogo)

    while True:
        print("\nMenú de opciones:")
        print("1. Agregar Película")
        print("2. Listar Películas")
        print("3. Eliminar catálogo de películas")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre_peli = input("Ingrese el nombre de la película: ")
            pelicula = Pelicula(nombre_peli)
            catalogo.agregar(pelicula)

        elif opcion == "2":
            catalogo.listar()

        elif opcion == "3":
            confirm = input("¿Está seguro de eliminar el catálogo? (s/n): ").lower()
            if confirm == "s":
                catalogo.eliminar()

        elif opcion == "4":
            print("👋 Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("⚠️ Opción inválida, intente nuevamente.")

if __name__ == "__main__":
    menu()