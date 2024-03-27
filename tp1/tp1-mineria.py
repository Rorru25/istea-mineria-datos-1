class Libro:
    def __init__(self, titulo, autor, genero, puntuacion):
      self.titulo=titulo
      self.autor=autor
      self.genero=genero
      self.puntuacion=puntuacion
lista_libros= [Libro("Cien años de soledad", "Gabriel García Márquez", "Ficción", 4.5),
               Libro("1984", "George Orwell", "Ciencia Ficción", 4.3) ,
               Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", 4.7) ,
               Libro("Orgullo y Prejuicio", "Jane Austen", "Romance", 4.2) ,
               Libro("Crimen y Castigo", "Fiódor Dostoyevski", "Clásico", 4.4) ,
               Libro("Los Juegos del Hambre", "Suzanne Collins", "Juvenil", 4.1) , 
               Libro("Don Quijote de la Mancha", "Miguel de Cervantes", "Clásico", 4.6),
               Libro("Harry Potter y la Piedra Filosofal", "J.K. Rowling", "Fantasía", 4.8),
               Libro("Los Pilares de la Tierra", "Ken Follett", "Histórica", 4.4) ,
               Libro("Cazadores de Sombras: Ciudad de Hueso", "Cassandra Clare", "Fantasía", 4.0)]


def agregar_libro():
    titulo = input("título del libro: ")
    autor = input("autor del libro: ")
    genero = input("género del libro: ")
    puntuacion = float(input("puntuación del libro (0-5): "))
    nuevo_libro = Libro(titulo, autor, genero, puntuacion)
    lista_libros.append(nuevo_libro)
    print("libro agregado")
agregar_libro()


def buscar_libros_por_genero():
    genero = input("ingrese un género de libro con el acento correspondiente para buscar: ")
    libros_encontrados = [libro.titulo for libro in lista_libros if libro.genero.lower() == genero.lower()]
    if libros_encontrados:
        print(f"libros encontrados en el género {genero}:")
        for titulo in libros_encontrados:
            print(titulo)
    else:
        print("no se encontraron libros en ese género")
buscar_libros_por_genero()

def recomendar_libro():
    genero = input("ingrese un género de libro con el acento correspondiente para recomendarle: ")
    libros_recomendados = [libro for libro in lista_libros if libro.genero.lower() == genero.lower()]
    if libros_recomendados:
        libro_recomendado = max(libros_recomendados, key=lambda x: x.puntuacion)
        print(f"libro recomendado en '{genero}': {libro_recomendado.titulo} con puntuación de {libro_recomendado.puntuacion}")
    else:
        print("no hay recomendaciones en ese género")
recomendar_libro()
 
def decision_usuario():
    print("Ingrese A si quiere continuar")
    print("Ingrese B si quiere salir")
def ejecutar_programa():
    while True:
        decision_usuario()
        opcion = input("Ingrese una opción: ").upper()
        if opcion == "A":
            agregar_libro()
            buscar_libros_por_genero()
            recomendar_libro()
        elif opcion == "B":
            print("Gracias por participar.")
            break
        else:
            print("Opción no válida. Por favor, ingrese A si quiere continuar o B si quiere salir")
ejecutar_programa()