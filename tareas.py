import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar  
from datetime import datetime

class ListaDeTareas:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Lista de Tareas")

        self.tareas = []


        self.lista_tareas = tk.Listbox(ventana, width=50)
        self.lista_tareas.pack(pady=10)

        # Crear campo de texto para ingresar nuevas tareas
        self.nueva_tarea_entry = tk.Entry(ventana, width=50)
        self.nueva_tarea_entry.pack()

        # Botón para agregar una nueva tarea
        self.agregar_btn = tk.Button(ventana, text="Agregar Tarea", command=self.agregar_tarea)
        self.agregar_btn.pack(pady=5)

        # Botón para eliminar una tarea seleccionada
        self.eliminar_btn = tk.Button(ventana, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.eliminar_btn.pack(pady=5)

        # Botón para marcar una tarea como completada
        self.completar_btn = tk.Button(ventana, text="Completar Tarea", command=self.completar_tarea)
        self.completar_btn.pack(pady=6)

        # Calendario para seleccionar la fecha de la tarea
        self.calendario = Calendar(ventana, selectmode="day", date_pattern="dd/mm/yyyy")
        self.calendario.pack(pady=10)

    def agregar_tarea(self):
        tarea = self.nueva_tarea_entry.get()
        if tarea:
            fecha_seleccionada = self.calendario.get_date()  # Obtiene la fecha seleccionada en el calendario
            tarea_con_fecha = f"{tarea} - {fecha_seleccionada}"  # Combina la tarea con la fecha seleccionada
            self.tareas.append(tarea_con_fecha)
            self.lista_tareas.insert(tk.END, tarea_con_fecha)
            self.nueva_tarea_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Error", "Por favor, ingrese una tarea.")

    def eliminar_tarea(self):
        tarea_seleccionada = self.lista_tareas.curselection()
        if tarea_seleccionada:
            indice = tarea_seleccionada[0]
            self.lista_tareas.delete(indice)
            del self.tareas[indice]
        else:
            messagebox.showwarning("Error", "Por favor, seleccione una tarea para eliminar.")

    def completar_tarea(self):
        tarea_seleccionada = self.lista_tareas.curselection()
        if tarea_seleccionada:
            indice = tarea_seleccionada[0]
            tarea = self.lista_tareas.get(indice)
            tarea_completada = tarea + " (Completada)"
            self.lista_tareas.delete(indice)
            self.lista_tareas.insert(indice, tarea_completada)
        else:
            messagebox.showwarning("Error", "Por favor, seleccione una tarea para marcar como completada.")

# Crear la ventana principal de la aplicación
ventana_principal = tk.Tk()
app = ListaDeTareas(ventana_principal)
ventana_principal.mainloop()
