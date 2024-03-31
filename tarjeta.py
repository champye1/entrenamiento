#CREAR UNA APLICACION DE PAGO AUTOMATICO ATRAVEZ DE ESCANEO DE TARJETA

#Importar librerias
import os
import sys
import time
import datetime
import RPi.GPIO as GPIO
import MFRC522
import signal
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from mysql.connector import (connection)
from mysql.connector import (cursor)

#Definir variables
continue_reading = True
#Definir funciones
def end_read(signal,frame):
    global continue_reading
    print("Ctrl+C detectado, finalizando lectura")
    continue_reading = False
    GPIO.cleanup()

def insertar_registro(id_tarjeta, nombre, apellido, fecha, hora):
    self.id_tarjeta = id_tarjeta
    self.nombre = nombre
    self.apellido = apellido
    self.fecha = fecha
    self.hora = hora
    try:
        print("Conectando a la base de datos...")
        connection = mysql.connector.connect(host='localhost',
                                                database='tarjetas',
                                                user='root',
                                                password='root')
        cursor = connection.cursor()
        sql_insert_query = """ INSERT INTO `registro`
                            (`id_tarjeta`, `nombre`, `apellido`, `fecha`, `hora`) VALUES (%s,%s,%s,%s,%s)"""
        insert_tuple = (id_tarjeta, nombre, apellido, fecha, hora)
        result = cursor.execute(sql_insert_query, insert_tuple)
        connection.commit()
        print("Registro insertado con exito")
    except mysql.connector.Error as error:
        print("Error al insertar registro {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("Conexion a la base de datos cerrada")

