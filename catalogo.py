import os

class Pelicula:
    def __init__(self, nombre: str):
        # atributo privado
        self.__nombre = nombre.strip()

    @property
    def nombre(self):
        return self.__nombre

    def __str__(self):
        return self.__nombre


class CatalogoPeliculas:
    def __init__(self, nombre_catalogo: str):
        self.nombre = nombre_catalogo.strip()
        self.ruta_archivo = f"{self.nombre}.txt"

    def agregar(self, pelicula: Pelicula):
        """Agrega una película al archivo"""
        with open(self.ruta_archivo, "a", encoding="utf-8") as archivo:
            archivo.write(pelicula.nombre + "\n")
        print(f"✅ Película '{pelicula.nombre}' agregada al catálogo '{self.nombre}'.")

    def listar(self):
        """Lista las películas del archivo"""
        if os.path.exists(self.ruta_archivo):
            print(f"\n📽️ Catálogo de películas '{self.nombre}':")
            with open(self.ruta_archivo, "r", encoding="utf-8") as archivo:
                peliculas = archivo.readlines()
                if peliculas:
                    for i, pelicula in enumerate(peliculas, start=1):
                        print(f"{i}. {pelicula.strip()}")
                else:
                    print("⚠️ El catálogo está vacío.")
        else:
            print("⚠️ No existe el catálogo. Agrega una película primero.")

    def eliminar(self):
        """Elimina el archivo del catálogo"""
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            print(f"🗑️ Catálogo '{self.nombre}' eliminado.")
        else:
            print("⚠️ El catálogo no existe.")