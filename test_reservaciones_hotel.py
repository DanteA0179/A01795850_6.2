"""Módulos estándar de Python utilizados en las pruebas del sistema."""

import unittest
import json
import os

from reservaciones_hotel import Hotel
from reservaciones_hotel import Cliente
from reservaciones_hotel import Reservacion


class TestHotel(unittest.TestCase):
    """ Clase de tests para probar las funciones dentro de la clase Hotel"""

    def setUp(self):
        """Prepara un archivo JSON vacío antes de cada prueba."""
        self.hotel = Hotel("test_hoteles.json")
        with open("test_hoteles.json", "w", encoding="utf-8") as f:
            json.dump([], f)

    def test_crear_hotel(self):
        """Verifica que `crear_hotel`
        agrega correctamente un hotel al sistema."""
        self.hotel.crear_hotel("Grand Hotel Budapest", 200)
        hoteles = self.hotel.cargar_datos()

        self.assertEqual(len(hoteles), 1)
        self.assertDictEqual(hoteles[0], {
            "id": 1,
            "nombre": "Grand Hotel Budapest",
            "habitaciones": 200,
            "reservas": []
        })

    def test_mostrar_hotel(self):
        """Verifica que `mostrar_hotel`
        muestra correctamente la información de un hotel."""
        self.hotel.crear_hotel("Grand Hotel Budapest", 200)
        hotel_info = self.hotel.mostrar_hotel(1)

        self.assertDictEqual(hotel_info, {
            "id": 1,
            "nombre": "Grand Hotel Budapest",
            "habitaciones": 200,
            "reservas": []
        })

    def test_modificar_hotel(self):
        """Verifica que `modificar_hotel`
        actualiza correctamente la información de un hotel."""

        self.hotel.crear_hotel("Grand Hotel Budapest", 200)
        self.hotel.modificar_hotel(1, nombre="Hotel California",
                                   habitaciones=250)
        hoteles = self.hotel.cargar_datos()

        self.assertEqual(hoteles[0]["nombre"], "Hotel California")
        self.assertEqual(hoteles[0]["habitaciones"], 250)

    def test_reservar_habitacion(self):
        """Verifica que `reservar_habitacion`
        agrega correctamente una reserva a un hotel."""
        self.hotel.crear_hotel("Grand Hotel Budapest", 200)
        self.hotel.reservar_habitacion(1, 1)
        hoteles = self.hotel.cargar_datos()

        self.assertEqual(len(hoteles[0]["reservas"]), 1)
        self.assertDictEqual(hoteles[0]["reservas"][0], {
            "id_cliente": 1
        })

    def test_cancelar_reserva(self):
        """Verifica que `cancelar_reserva`
        elimina correctamente una reserva de un hotel."""
        self.hotel.crear_hotel("Grand Hotel Budapest", 200)
        self.hotel.reservar_habitacion(1, 1)
        self.hotel.cancelar_reserva(1, 1)
        hoteles = self.hotel.cargar_datos()

        self.assertEqual(len(hoteles[0]["reservas"]), 0)

    def test_eliminar_hotel(self):
        """Verifica que `eliminar_hotel`
        elimina correctamente un hotel del sistema."""
        self.hotel.crear_hotel("Grand Hotel Budapest", 200)
        self.hotel.eliminar_hotel(1)
        hoteles = self.hotel.cargar_datos()

        self.assertEqual(len(hoteles), 0)

    def tearDown(self):
        """Limpia el archivo JSON después de cada prueba."""
        if os.path.exists("test_hoteles.json"):
            os.remove("test_hoteles.json")


class TestCliente(unittest.TestCase):
    """ Clase de tests para probar las funciones dentro de la clase Cliente"""

    def setUp(self):
        """Prepara un archivo JSON vacío antes de cada prueba."""
        self.cliente = Cliente("test_cliente.json")
        with open("test_cliente.json", "w", encoding="utf-8") as f:
            json.dump([], f)

    def test_agregar(self):
        """Verifica que `agregar`
        agrega correctamente un cliente al sistema."""
        self.cliente.agregar("Dante", 31)
        clientes = self.cliente.cargar_datos()

        self.assertEqual(len(clientes), 1)
        self.assertDictEqual(clientes[0], {
            "id": 1,
            "nombre": "Dante",
            "edad": 31
        })

    def test_mostrar_cliente(self):
        """Verifica que `mostrar_cliente`
        muestra correctamente la información de un cliente."""
        self.cliente.agregar("Dante", 31)
        cliente_info = self.cliente.mostrar_cliente(1)

        self.assertDictEqual(cliente_info, {
            "id": 1,
            "nombre": "Dante",
            "edad": 31
        })

    def test_editar(self):
        """Verifica que `editar`
        actualiza correctamente la información de un cliente."""
        self.cliente.agregar("Dante", 31)
        self.cliente.editar(1, nombre="Bruno",
                            edad=29)
        clientes = self.cliente.cargar_datos()

        self.assertEqual(clientes[0]["nombre"], "Bruno")
        self.assertEqual(clientes[0]["edad"], 29)

    def test_eliminar(self):
        """Verifica que `eliminar`
        elimina correctamente un cliente del sistema."""
        self.cliente.agregar("Dante", 31)
        self.cliente.eliminar(1)
        clientes = self.cliente.cargar_datos()

        self.assertEqual(len(clientes), 0)

    def tearDown(self):
        """Limpia el archivo JSON después de cada prueba."""
        if os.path.exists("test_cliente.json"):
            os.remove("test_cliente.json")


class TestReservacion(unittest.TestCase):
    """ Clase de tests para probar las
    funciones dentro de la clase Reservacion"""

    def setUp(self):
        """Prepara un archivo JSON vacío antes de cada prueba."""
        self.reserva = Reservacion("test_reservacion.json")
        with open("test_reservacion.json", "w", encoding="utf-8") as f:
            json.dump([], f)

    def test_agregar(self):
        """Verifica que `agregar`
        agrega correctamente una reservacion al sistema."""
        self.reserva.agregar(1, 1)
        reservaciones = self.reserva.cargar_datos()

        self.assertEqual(len(reservaciones), 1)
        self.assertDictEqual(reservaciones[0], {
            "id": 1,
            "id_cliente": 1,
            "id_hotel": 1
        })

    def test_eliminar(self):
        """Verifica que `eliminar`
        elimina correctamente una reservación del sistema."""
        self.reserva.agregar(1, 1)
        self.reserva.eliminar(1)
        reservaciones = self.reserva.cargar_datos()

        self.assertEqual(len(reservaciones), 0)

    def tearDown(self):
        """Limpia el archivo JSON después de cada prueba."""
        if os.path.exists("test_cliente.json"):
            os.remove("test_cliente.json")


if __name__ == "__main__":
    unittest.main()
