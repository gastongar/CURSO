import unittest

import cambiatexto


class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'buen dia'
        resultado = cambiatexto.todo_mayuscula(palabra)
        self.assertEqual(resultado, 'Buen Dia')


if __name__ == '__main__':
    unittest.main()

