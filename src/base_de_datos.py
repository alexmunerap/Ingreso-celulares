import psycopg2




def guardar_nuevo_ingreso(marca, modelo, diagnostico, nombre, cedula, telefono, dbname="postgres", user="postgres", password="admin", host="localhost", port="5432"):
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        cursor = conn.cursor()

        # Assuming correct column names in the query (modify if different)
        query = '''INSERT INTO celulares(marca, modelo, diagnostico, nombre, cedula, telefono) VALUES (%s, %s, %s, %s, %s, %s)'''
        cursor.execute(query, (marca, modelo, diagnostico, nombre, cedula, telefono))

        conn.commit()
        print("Datos guardados")
    except (Exception, psycopg2.Error) as error:
        print("Error al guardar datos:", error)
    finally:
        if conn:
            conn.close()




