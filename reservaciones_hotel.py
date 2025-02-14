"""
Módulo para gestionar hoteles, clientes y reservaciones usando JSON.

Este módulo permite crear, modificar y eliminar hoteles,
clientes y reservaciones,
almacenando la información en archivos JSON.

Clases:
    - Hotel: Maneja la gestión de hoteles.
    - Cliente: Maneja la gestión de clientes.
    - Reservacion: Maneja la gestión de reservaciones.

Importa:
    - json: Para la codificación y decodificación de datos JSON.
    - os: Para operaciones con el sistema de archivos.
"""

import json
import os


class Hotel:
    """Clase para gestionar hoteles y sus reservas."""
    def __init__(self, archivo="hoteles.json"):
        """Inicializa la clase y verifica la existencia del archivo JSON."""
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump([], f)

    def cargar_datos(self):
        """Carga los datos de los hoteles desde el archivo JSON."""
        with open(self.archivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def guardar_datos(self, datos):
        """Guarda los datos de los hoteles en el archivo JSON."""
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

    def crear_hotel(self, nombre, habitaciones):
        """Añade un nuevo hotel al sistema."""
        datos = self.cargar_datos()
        nuevo_hotel = {
            "id": len(datos) + 1,
            "nombre": nombre,
            "habitaciones": habitaciones,
            "reservas": []
        }
        datos.append(nuevo_hotel)
        self.guardar_datos(datos)
        print(f"Hotel '{nombre}' creado correctamente.")

    def eliminar_hotel(self, id_h):
        """Elimina un hotel del sistema por su ID."""
        datos = self.cargar_datos()
        datos = [hotel for hotel in datos if hotel["id"] != id_h]
        self.guardar_datos(datos)
        print(f"Hotel con ID {id_h} eliminado correctamente.")

    def mostrar_hotel(self, id_mh):
        """Retorna la información del hotel o un mensaje de error."""
        datos = self.cargar_datos()
        for hotel in datos:
            if hotel["id"] == id_mh:
                return hotel
        return {"error": f"No se encontró un hotel con ID {id_mh}."}

    def modificar_hotel(self, id_moh, nombre=None, habitaciones=None):
        """Modifica la información de un hotel existente."""
        datos = self.cargar_datos()
        for hotel in datos:
            if hotel["id"] == id_moh:
                if nombre:
                    hotel["nombre"] = nombre
                if habitaciones:
                    hotel["habitaciones"] = habitaciones
                self.guardar_datos(datos)
                print(f"Hotel con ID {id_moh} modificado correctamente.")
                return
        print(f"Error: No se encontró un hotel con ID {id_moh}.")

    def reservar_habitacion(self, id_hotel, id_cliente):
        """Realiza una reserva de habitación en un hotel."""
        datos = self.cargar_datos()

        for hotel in datos:
            if hotel["id"] == id_hotel:
                hab_disp = hotel["habitaciones"] - len(hotel["reservas"])

                if hab_disp > 0:
                    nueva_reserva = {"id_cliente": id_cliente}
                    hotel["reservas"].append(nueva_reserva)
                    self.guardar_datos(datos)
                    print(f"Habitación reservada en el hotel ID {id_hotel}.")
                    return

                print("Error: No hay habitaciones disponibles.")
                return

        print(f"Error: No se encontró un hotel con ID {id_hotel}.")

    def cancelar_reserva(self, id_hotel, id_cliente):
        """Realiza una reserva de habitación en un hotel."""
        datos = self.cargar_datos()
        for hotel in datos:
            if hotel["id"] == id_hotel:
                reservas = hotel["reservas"]
                for reserva in reservas:
                    if reserva["id_cliente"] == id_cliente:
                        reservas.remove(reserva)
                        self.guardar_datos(datos)
                        print(f"Reserva cancelada en el hotel ID {id_hotel}.")
                        return
                print(f"Error: Sin reserva para el {id_cliente}.")
                return
        print(f"Error: No se encontró un hotel con ID {id_hotel}.")


class Cliente:
    """Clase para gestionar clientes"""
    def __init__(self, archivo="clientes.json"):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump([], f)

    def cargar_datos(self):
        """Carga los datos de los clientes desde el archivo JSON."""
        with open(self.archivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def guardar_datos(self, datos):
        """Guarda los datos de los clientes en el archivo JSON."""
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

    def agregar(self, nombre, edad):
        """Añade un nuevo cliente al sistema."""
        datos = self.cargar_datos()
        nuevo_cliente = {
            "id": len(datos) + 1,
            "nombre": nombre,
            "edad": edad
        }
        datos.append(nuevo_cliente)
        self.guardar_datos(datos)
        print(f"Cliente '{nombre}' añadido correctamente.")

    def editar(self, id_c, nombre=None, edad=None):
        """Edita un cliente con respecto a su id."""
        datos = self.cargar_datos()
        for cliente in datos:
            if cliente["id"] == id_c:
                if nombre:
                    cliente["nombre"] = nombre
                if edad:
                    cliente["edad"] = edad
                self.guardar_datos(datos)
                print(f"Cliente con ID {id_c} editado correctamente.")
                return
        print(f"Error: No se encontró un cliente con ID {id_c}.")

    def eliminar(self, id_e):
        """Elimina un cliente con respecto a su id."""
        datos = self.cargar_datos()
        datos = [cliente for cliente in datos if cliente["id"] != id_e]
        self.guardar_datos(datos)
        print(f"Cliente con ID {id_e} eliminado correctamente.")

    def mostrar_cliente(self, id_mc):
        """Muestra la información de un cliente por su ID."""
        datos = self.cargar_datos()
        for cliente in datos:
            if cliente["id"] == id_mc:
                return cliente
        return {"error": f"No se encontró un hotel con ID {id_mc}."}


class Reservacion:
    """Clase para gestionar clientes"""
    def __init__(self, archivo="reservaciones.json"):
        self.archivo = archivo
        if not os.path.exists(self.archivo):
            with open(self.archivo, "w", encoding="utf-8") as f:
                json.dump([], f)

    def cargar_datos(self):
        """Carga los datos de las reservaciones desde el archivo JSON."""
        with open(self.archivo, "r", encoding="utf-8") as f:
            return json.load(f)

    def guardar_datos(self, datos):
        """Guarda los datos de los clientes en el archivo JSON."""
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(datos, f, indent=4)

    def agregar(self, id_cliente, id_hotel):
        """Añade una nueva reservación al sistema."""
        datos = self.cargar_datos()
        nueva_reservacion = {
            "id": len(datos) + 1,
            "id_cliente": id_cliente,
            "id_hotel": id_hotel
        }
        datos.append(nueva_reservacion)
        self.guardar_datos(datos)
        print("Reservación añadida correctamente.")

    def eliminar(self, id_r):
        """Elimina una reservación con respecto a su id."""
        datos = self.cargar_datos()
        datos = [
            reservacion for reservacion in datos
            if reservacion["id"] != id_r
            ]
        self.guardar_datos(datos)
        print(f"Reservación con ID {id_r} eliminada correctamente.")
