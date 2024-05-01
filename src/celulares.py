from tkinter import Tk, Canvas, Label, Frame, Entry, Button, W, E, Listbox, messagebox, END, Toplevel
import psycopg2
import base_de_datos
from base_de_datos import guardar_nuevo_ingreso

root = Tk()
root.title("Ingresos celulares")




def manejar_guardar_click():
    marca = entry_marca.get()
    modelo = entry_modelo.get()
    diagnostico = entry_diagnostico.get()
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    telefono = entry_telefono.get()

    
    dbname = "postgres"  
    user = "postgres"  
    password = "admin"  
    host = "localhost"  
    port = "5432"  

    
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()

        
        query = '''INSERT INTO celulares(marca, modelo, diagnostico, nombre, cedula, telefono) VALUES (%s, %s, %s, %s, %s, %s)'''
        cursor.execute(query, (marca, modelo, diagnostico, nombre, cedula, telefono))

        
        conn.commit()
        conn.close()
        print("Datos guardados en la base de datos PostgreSQL")
    except (Exception, psycopg2.Error) as error:
        print(f"Error al guardar datos en PostgreSQL: {error}")



ventana_principal = Tk()
ventana_principal.title("Ingreso de Celulares")


marco = Frame(ventana_principal)
marco.pack(padx=10, pady=10)


etiqueta_marca = Label(marco, text="Marca: ")
etiqueta_marca.grid(row=0, column=0, sticky=W)  

entry_marca = Entry(marco)
entry_marca.grid(row=0, column=1)

etiqueta_modelo = Label(marco, text="Modelo: ")
etiqueta_modelo.grid(row=1, column=0, sticky=W)

entry_modelo = Entry(marco)
entry_modelo.grid(row=1, column=1)

etiqueta_diagnostico = Label(marco, text="Diagnóstico: ")
etiqueta_diagnostico.grid(row=2, column=0, sticky=W)

entry_diagnostico = Entry(marco)
entry_diagnostico.grid(row=2, column=1)

etiqueta_nombre = Label(marco, text="Nombre del cliente: ")
etiqueta_nombre.grid(row=3, column=0, sticky=W)

entry_nombre = Entry(marco)
entry_nombre.grid(row=3, column=1)

etiqueta_cedula = Label(marco, text="Cédula del cliente: ")
etiqueta_cedula.grid(row=4, column=0, sticky=W)

entry_cedula = Entry(marco)
entry_cedula.grid(row=4, column=1)

etiqueta_telefono = Label(marco, text="Teléfono del cliente: ")
etiqueta_telefono.grid(row=5, column=0, sticky=W)

entry_telefono = Entry(marco)
entry_telefono.grid(row=5, column=1)

boton_guardar = Button(marco, text="Guardar", command=manejar_guardar_click)
boton_guardar.grid(row=6, column=1, sticky=W+E)  


lista_celulares = Listbox(marco)
lista_celulares.grid(row=7, column=0, rowspan=2, columnspan=2)  

def actualizar_lista_celulares():
    lista_celulares.delete(0, END)  

    
    try:
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
        cursor = conn.cursor()

        query = '''SELECT * FROM celulares'''
        cursor.execute(query)
        celulares = cursor.fetchall()

        
        for celular in celulares:
            lista_celulares.insert(END, f"{celular[0]}: {celular[1]} - {celular[2]}")  

        conn.close()
    except (Exception, psycopg2.Error) as error:
        print(f"Error al actualizar lista de celulares: {error}")


actualizar_lista_celulares()



def modificar_celular():
    indice_seleccionado = lista_celulares.curselection()[0]
    id_celular_seleccionado = lista_celulares.get(indice_seleccionado).split(":")[0]

    modificar_ventana = Toplevel(ventana_principal)
    modificar_ventana.title(f"Modificar Celular {id_celular_seleccionado}")

   

 
    modificar_ventana.destroy()  


    

def eliminar_celular():
    
    indice_seleccionado = lista_celulares.curselection()[0]
    id_celular_seleccionado = lista_celulares.get(indice_seleccionado).split(":")[0]

    
    confirmacion = messagebox.askokcancel("Eliminar Celular", f"¿Desea eliminar el celular {id_celular_seleccionado}?")

    if confirmacion:
       
        try:
            conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
            cursor = conn.cursor()

            query = '''DELETE FROM celulares WHERE id = %s'''
            cursor.execute(query, (id_celular_seleccionado,))

            conn.commit()
            conn.close()

            
            actualizar_lista_celulares()
            print(f"Celular {id_celular_seleccionado} eliminado")
        except (Exception, psycopg2.Error) as error:
            print(f"Error al eliminar celular {id_celular_seleccionado}: {error}")


boton_modificar = Button(marco, text="Modificar", command=modificar_celular)
boton_modificar.grid(row=7, column=2, sticky=W+E)

boton_eliminar = Button(marco, text="Eliminar", command=eliminar_celular)
boton_eliminar.grid(row=8, column=2, sticky=W+E)


def modificar_celular_en_bd(celular_id, marca_nueva, modelo_nuevo, diagnostico_nuevo, nombre_nuevo, cedula_nueva, telefono_nuevo):
        
    
   
        conn = psycopg2.connect(dbname="postgres", user="postgres", password="admin", host="localhost", port="5432")
        cursor = conn.cursor()

        query = '''UPDATE celulares SET marca = %s, modelo = %s, diagnostico = %s, nombre = %s, cedula = %s, telefono = %s WHERE id = %s'''
        cursor.execute(query, (marca_nueva, modelo_nuevo, diagnostico_nuevo, nombre_nuevo, cedula_nueva, telefono_nuevo, celular_id))




ventana_principal.mainloop()








