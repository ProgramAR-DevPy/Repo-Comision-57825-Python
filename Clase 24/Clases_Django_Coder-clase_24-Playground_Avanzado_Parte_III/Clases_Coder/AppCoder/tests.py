from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from AppCoder.models import Profesor
from users.utilities.utility import return_today, return_month, return_year
from datetime import datetime as dt


# Create your tests here.
# Creamos una clase llamada 'TestUtilities' que hereda de 'TestCase' para agrupar pruebas relacionadas con utilidades
class TestUtilities(TestCase):

    # Definimos un método de prueba llamado 'test_day'
    def test_day(self):

        # Obtenemos la fecha y hora actual utilizando 'dt.now()' y la almacenamos en la variable 'hoy'
        hoy = dt.now()

        # Utilizamos 'self.assertEqual' para comparar el resultado de la función 'return_today()' con el día actual ('hoy.day')
        # Si son iguales, la prueba pasa; si no, la prueba falla.
        self.assertEqual(hoy.day , return_today() )
    
    def test_return_year(self):
        """Prueba que la función return_year devuelve el año actual correctamente."""
        hoy = dt.now()  # Obtiene la fecha y hora actual
        self.assertEqual(return_year(), hoy.year)  # Compara el resultado de la función con el año actual





class EliminarProfesorTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.login(username='testuser', password='12345')
        self.profesor = Profesor.objects.create(
            nombre="Juan",
            apellido="Perez",
            email="a@b.com"
        )
        self.url = reverse("ProfesorDelete", args=[self.profesor.id])

    def test_eliminar_profesor(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "AppCoder/profesor_confirm_delete.html")
        self.client.post(self.url)
        self.assertQuerysetEqual(Profesor.objects.all(), [])
