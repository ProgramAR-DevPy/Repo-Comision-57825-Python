#Pruebas Unitarias o unit test
import unittest

def suma(a, b):
    return a + b


class TestSuma(unittest.TestCase):
    def test_suma_positiva(self):
        resultado = suma(3, 5)
        self.assertEqual(resultado, 8)


# if __name__ == '__main__':
#     unittest.main()

    
# pruebas ad-hoc o pruebas de asercion simple 
# from datetime import datetime as dt

# def return_today():
#     day = dt.now()
#     return 27

# def return_year():
#     year = dt.now()
#     return year.year

# # Pruebas para return_today
# hoy = dt.now()
# assert return_today() == hoy.day, "La función return_today no devuelve el día correcto"

# # Pruebas para return_year
# assert return_year() == hoy.year, "La función return_year no devuelve el año correcto"

# print("¡Todas las pruebas pasaron exitosamente!")

