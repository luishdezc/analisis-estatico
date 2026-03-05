# -*- coding: utf-8 -*-

"""
Book store unit testing.
"""

import unittest
from io import StringIO
from unittest.mock import patch

from white_box.book_store import Book, BookStore, main


class TestBookInit(unittest.TestCase):
    """
    Pruebas de inicialización de Book.
    """

    def test_attributes_stored_correctly(self):
        """
        Verifica que el constructor almacena correctamente
        título, autor, precio y cantidad.
        """
        book = Book("Clean Code", "Robert Martin", 29.99, 5)
        self.assertEqual(book.title, "Clean Code")
        self.assertEqual(book.author, "Robert Martin")
        self.assertEqual(book.price, 29.99)
        self.assertEqual(book.quantity, 5)

    def test_integer_price_accepted(self):
        """
        Verifica que el precio puede ser un entero
        y se almacena sin modificación.
        """
        book = Book("Python", "Guido", 20, 1)
        self.assertEqual(book.price, 20)

    def test_zero_price_accepted(self):
        """
        Verifica que el precio puede ser cero
        y se guarda correctamente.
        """
        book = Book("Free Book", "Author", 0, 10)
        self.assertEqual(book.price, 0)

    def test_zero_quantity_accepted(self):
        """
        Verifica que la cantidad puede ser cero
        (por ejemplo, libro sin stock).
        """
        book = Book("Out of Stock", "Author", 9.99, 0)
        self.assertEqual(book.quantity, 0)

    def test_title_with_special_chars(self):
        """
        Verifica que el título acepta caracteres especiales
        y se almacena correctamente.
        """
        book = Book("El niño & la lluvia", "Autor", 15.0, 3)
        self.assertEqual(book.title, "El niño & la lluvia")

    def test_empty_strings_accepted(self):
        """
        Verifica que se permiten cadenas vacías
        para título y autor.
        """
        book = Book("", "", 0.0, 0)
        self.assertEqual(book.title, "")
        self.assertEqual(book.author, "")

    def test_negative_price_stored(self):
        """
        Book no valida precios; verifica que almacena el valor tal cual.
        """
        book = Book("Discount", "Author", -5.0, 1)
        self.assertEqual(book.price, -5.0)

    def test_large_quantity(self):
        """
        Verifica que cantidades grandes
        se almacenan correctamente.
        """
        book = Book("Bestseller", "Author", 9.99, 1_000_000)
        self.assertEqual(book.quantity, 1_000_000)


class TestBookDisplay(unittest.TestCase):
    """
    Pruebas de Book.display().
    """

    def setUp(self):
        """
        Crea una instancia de Book que será utilizada
        en cada prueba del método display().
        """
        self.book = Book("1984", "George Orwell", 12.50, 7)

    def test_display_prints_title(self):
        """
        Verifica que display() imprime correctamente el título.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.book.display()
            self.assertIn("Title: 1984", mock_out.getvalue())

    def test_display_prints_author(self):
        """
        Verifica que display() imprime correctamente el autor.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.book.display()
            self.assertIn("Author: George Orwell", mock_out.getvalue())

    def test_display_prints_price(self):
        """
        Verifica que display() imprime correctamente el precio.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.book.display()
            self.assertIn("Price: $12.5", mock_out.getvalue())

    def test_display_prints_quantity(self):
        """
        Verifica que display() imprime correctamente la cantidad.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.book.display()
            self.assertIn("Quantity: 7", mock_out.getvalue())

    def test_display_all_four_lines_present(self):
        """
        Verifica que display() imprime todas las líneas esperadas:
        título, autor, precio y cantidad.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.book.display()
            output = mock_out.getvalue()
        for fragment in ["Title:", "Author:", "Price:", "Quantity:"]:
            self.assertIn(fragment, output)


class TestBookStoreInit(unittest.TestCase):
    """
    Pruebas de inicialización de BookStore.
    """

    def test_books_list_starts_empty(self):
        """
        Verifica que la lista de libros inicia vacía
        al crear una nueva instancia de BookStore.
        """
        store = BookStore()
        self.assertEqual(store.books, [])

    def test_books_attribute_is_list(self):
        """
        Verifica que el atributo books es de tipo list.
        """
        store = BookStore()
        self.assertIsInstance(store.books, list)

    def test_two_stores_are_independent(self):
        """
        Verifica que dos instancias de BookStore
        mantienen listas de libros independientes.
        """
        s1, s2 = BookStore(), BookStore()
        s1.books.append(Book("A", "X", 1, 1))
        self.assertEqual(len(s2.books), 0)


class TestBookStoreAddBook(unittest.TestCase):
    """
    Pruebas de BookStore.add_book().
    """

    def setUp(self):
        """
        Inicializa una instancia de BookStore y un libro
        que será utilizado en las pruebas.
        """
        self.store = BookStore()
        self.book = Book("Dune", "Frank Herbert", 18.99, 4)

    def test_book_added_to_list(self):
        """
        Verifica que el libro se agrega correctamente
        a la lista interna de la tienda.
        """
        with patch("sys.stdout", new_callable=StringIO):
            self.store.add_book(self.book)
        self.assertIn(self.book, self.store.books)

    def test_books_list_length_increases(self):
        """
        Verifica que la longitud de la lista aumenta
        después de agregar un libro.
        """
        with patch("sys.stdout", new_callable=StringIO):
            self.store.add_book(self.book)
        self.assertEqual(len(self.store.books), 1)

    def test_confirmation_message_printed(self):
        """
        Verifica que se imprime un mensaje de confirmación
        al agregar un libro a la tienda.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.add_book(self.book)
        self.assertIn("Dune", mock_out.getvalue())
        self.assertIn("added to the store", mock_out.getvalue())

    def test_add_multiple_books(self):
        """
        Verifica que se pueden agregar múltiples libros
        y que todos se almacenan correctamente.
        """
        books = [Book(f"Book {i}", "Author", i * 10.0, i) for i in range(1, 6)]
        with patch("sys.stdout", new_callable=StringIO):
            for b in books:
                self.store.add_book(b)
        self.assertEqual(len(self.store.books), 5)

    def test_add_duplicate_book_objects(self):
        """
        Verifica que el mismo objeto libro puede agregarse
        más de una vez a la lista.
        """
        with patch("sys.stdout", new_callable=StringIO):
            self.store.add_book(self.book)
            self.store.add_book(self.book)
        self.assertEqual(len(self.store.books), 2)


class TestBookStoreDisplayBooks(unittest.TestCase):
    """
    Pruebas de BookStore.display_books().
    """

    def setUp(self):
        """
        Inicializa una instancia vacía de BookStore
        para cada prueba.
        """
        self.store = BookStore()

    def _add(self, title="Test", author="Author", price=10.0, qty=1):
        """
        Método auxiliar para agregar un libro a la tienda
        sin mostrar la salida en consola.
        """
        book = Book(title, author, price, qty)
        with patch("sys.stdout", new_callable=StringIO):
            self.store.add_book(book)
        return book

    def test_empty_store_message(self):
        """
        Verifica que se imprime el mensaje correspondiente
        cuando la tienda no tiene libros.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.display_books()
        self.assertIn("No books in the store.", mock_out.getvalue())

    def test_empty_store_does_not_print_header(self):
        """
        Verifica que no se imprime el encabezado
        cuando la tienda está vacía.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.display_books()
        self.assertNotIn("Books available", mock_out.getvalue())

    def test_single_book_header_shown(self):
        """
        Verifica que se muestra el encabezado
        cuando existe al menos un libro.
        """
        self._add("Brave New World")
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.display_books()
        self.assertIn("Books available in the store:", mock_out.getvalue())

    def test_single_book_title_shown(self):
        """
        Verifica que el título de un libro agregado
        se muestra correctamente.
        """
        self._add("Brave New World")
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.display_books()
        self.assertIn("Brave New World", mock_out.getvalue())

    def test_multiple_books_all_titles_shown(self):
        """
        Verifica que todos los títulos se muestran
        cuando existen múltiples libros.
        """
        titles = ["Book A", "Book B", "Book C"]
        for t in titles:
            self._add(t)
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.display_books()
        output = mock_out.getvalue()
        for t in titles:
            self.assertIn(t, output)


class TestBookStoreSearchBook(unittest.TestCase):
    """
    Pruebas de BookStore.search_book().
    """

    def setUp(self):
        """
        Inicializa la tienda con libros de prueba,
        incluyendo títulos duplicados.
        """
        self.store = BookStore()
        with patch("sys.stdout", new_callable=StringIO):
            self.store.add_book(Book("The Hobbit", "Tolkien", 14.99, 3))
            self.store.add_book(Book("The Hobbit", "Tolkien", 14.99, 2))
            self.store.add_book(Book("Foundation", "Asimov", 11.99, 5))

    def test_not_found_message(self):
        """
        Verifica que se muestra el mensaje adecuado
        cuando no se encuentra ningún libro.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.search_book("Nonexistent Book")
        self.assertIn(
            "No book found with title 'Nonexistent Book'.", mock_out.getvalue()
        )

    def test_found_one_book(self):
        """
        Verifica que se muestra el mensaje correcto
        cuando se encuentra un solo libro.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.search_book("Foundation")
        self.assertIn("Found 1 book(s) with title 'Foundation':", mock_out.getvalue())

    def test_found_multiple_books(self):
        """
        Verifica que se indica correctamente
        cuando se encuentran múltiples libros con el mismo título.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.search_book("The Hobbit")
        self.assertIn("Found 2 book(s) with title 'The Hobbit':", mock_out.getvalue())

    def test_case_insensitive_lower(self):
        """
        Verifica que la búsqueda no distingue
        entre mayúsculas y minúsculas (minúsculas).
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.search_book("the hobbit")
        self.assertIn("Found", mock_out.getvalue())
        self.assertNotIn("No book found", mock_out.getvalue())

    def test_case_insensitive_upper(self):
        """
        Verifica que la búsqueda no distingue
        entre mayúsculas y minúsculas (mayúsculas).
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.search_book("FOUNDATION")
        self.assertIn("Found", mock_out.getvalue())

    def test_case_insensitive_mixed(self):
        """
        Verifica que la búsqueda funciona correctamente
        con combinación de mayúsculas y minúsculas.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.search_book("fOuNdAtIoN")
        self.assertIn("Found", mock_out.getvalue())

    def test_partial_title_not_matched(self):
        """
        Verifica que no se consideran coincidencias parciales
        como resultados válidos.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.search_book("Hobbit")
        self.assertIn("No book found", mock_out.getvalue())

    def test_empty_string_search_on_empty_store(self):
        """
        Verifica el comportamiento al buscar una cadena vacía
        en una tienda sin libros.
        """
        store = BookStore()
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            store.search_book("")
        self.assertIn("No book found", mock_out.getvalue())

    def test_search_displays_book_details(self):
        """
        Verifica que los detalles del libro encontrado
        se muestran correctamente.
        """
        with patch("sys.stdout", new_callable=StringIO) as mock_out:
            self.store.search_book("Foundation")
        output = mock_out.getvalue()
        self.assertIn("Asimov", output)
        self.assertIn("11.99", output)


class TestMain(unittest.TestCase):
    """
    Pruebas del bucle interactivo main().
    """

    def _run_main(self, inputs):
        """
        Helper: ejecuta main() con una lista de entradas simuladas.
        """
        with patch("builtins.input", side_effect=inputs), patch(
            "sys.stdout", new_callable=StringIO
        ) as mock_out:
            main()
        return mock_out.getvalue()

    def test_exit_immediately(self):
        """
        Verifica que el programa termina correctamente
        cuando el usuario selecciona la opción de salida.
        """
        output = self._run_main(["4"])
        self.assertIn("Exiting...", output)

    def test_exit_prints_menu(self):
        """
        Verifica que el menú se muestra antes
        de salir del programa.
        """
        output = self._run_main(["4"])
        self.assertIn("1. Display all books", output)

    def test_display_books_empty_store(self):
        """
        Verifica que se muestra el mensaje adecuado
        al intentar mostrar libros en una tienda vacía.
        """
        output = self._run_main(["1", "4"])
        self.assertIn("No books in the store.", output)

    def test_display_books_after_adding(self):
        """
        Verifica que un libro agregado se muestra
        correctamente al listar los libros.
        """
        inputs = [
            "3",
            "Moby Dick",
            "Melville",
            "9.99",
            "2",
            "1",
            "4",
        ]
        output = self._run_main(inputs)
        self.assertIn("Moby Dick", output)

    def test_search_not_found(self):
        """
        Verifica que se muestra el mensaje correcto
        cuando la búsqueda no encuentra coincidencias.
        """
        output = self._run_main(["2", "Unknown Book", "4"])
        self.assertIn("No book found with title 'Unknown Book'.", output)

    def test_search_found_after_adding(self):
        """
        Verifica que la búsqueda encuentra un libro
        previamente agregado.
        """
        inputs = [
            "3",
            "Don Quijote",
            "Cervantes",
            "7.50",
            "1",
            "2",
            "Don Quijote",
            "4",
        ]
        output = self._run_main(inputs)
        self.assertIn("Found 1 book(s) with title 'Don Quijote':", output)

    def test_add_book_confirmation(self):
        """
        Verifica que se imprime el mensaje de confirmación
        después de agregar un libro.
        """
        inputs = ["3", "Hamlet", "Shakespeare", "5.00", "10", "4"]
        output = self._run_main(inputs)
        self.assertIn("Hamlet", output)
        self.assertIn("added to the store", output)

    def test_add_multiple_books_then_display(self):
        """
        Verifica que múltiples libros agregados
        se muestran correctamente al listarlos.
        """
        inputs = [
            "3",
            "Book A",
            "Auth A",
            "10.0",
            "1",
            "3",
            "Book B",
            "Auth B",
            "20.0",
            "2",
            "1",
            "4",
        ]
        output = self._run_main(inputs)
        self.assertIn("Book A", output)
        self.assertIn("Book B", output)

    def test_invalid_choice_message(self):
        """
        Verifica que se muestra un mensaje de error
        cuando el usuario ingresa una opción inválida.
        """
        output = self._run_main(["9", "4"])
        self.assertIn("Invalid choice. Please try again.", output)

    def test_invalid_choice_loops_back_to_menu(self):
        """
        Verifica que después de una opción inválida,
        el menú se vuelve a mostrar.
        """
        output = self._run_main(["x", "4"])
        self.assertGreaterEqual(output.count("1. Display all books"), 2)

    def test_multiple_invalid_then_exit(self):
        """
        Verifica que múltiples entradas inválidas
        muestran el mensaje correspondiente cada vez.
        """
        output = self._run_main(["!", "0", "abc", "4"])
        self.assertEqual(output.count("Invalid choice"), 3)

    def test_full_workflow(self):
        """
        Verifica el flujo completo del programa:
        agregar libro, mostrar libros, buscar libro existente,
        buscar libro inexistente y salir.
        """
        inputs = [
            "3",
            "Cosmos",
            "Sagan",
            "14.99",
            "3",
            "1",
            "2",
            "Cosmos",
            "2",
            "Ghost Book",
            "4",
        ]
        output = self._run_main(inputs)
        self.assertIn("added to the store", output)
        self.assertIn("Books available in the store:", output)
        self.assertIn("Found 1 book(s) with title 'Cosmos':", output)
        self.assertIn("No book found with title 'Ghost Book'.", output)
        self.assertIn("Exiting...", output)
