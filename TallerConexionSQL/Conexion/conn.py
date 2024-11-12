# Archivo para conexion de base de datos 
import pymysql

conn = pymysql.connect(
    host= 'localhost',
    user= 'root',
    password= '',
    database='universidad',
    port=3306  
)

def consulta_modalidad():
    cursor = conn.cursor()
    cursor.execute('Select* From modalidad')
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila[1])

#para agregar una nueva carrera
def insertar_carrera():
    cursor = conn.cursor()
    cursor.execute("Insert into carrera(cadigo, nombre, universidad, modalidad_id) values('COMP_01','Sistemas','UPTL', 1)")
    conn.commit()
    print("Carrera insertada correctamente.")

#una carrera específica por su código
def consulta_carreras():
    cursor = conn.cursor()
    cursor.execute('Select* From carrera')
    resultados= cursor.fetchall()
    for fila in resultados:
        print(fila[0], '-',fila[1],'-',fila[2])

#para actualizar el nombre de una carrera dado su código
def actualizar_carrera(cadigo, nombre):
    try:
        cursor=conn.cursor()
        sql = "UPDATE carrera SET nombre = %s WHERE cadigo = %s"
        cursor.execute(sql, ( nombre, cadigo))
        conn.commit()
    except Exception as e:
        print("Error al actualizar la carrera:", e)
    finally:
        cursor.close()
    
cadigo_ca = 'COMP_01'
nombre = 'Sistemas Avanzados'
    
#Para eliminar una carrera dado su id.
def eliminar_carrera(id):
    try:
        cursor = conn.cursor()
        sql= "DELETE FROM carrera WHERE id = %s"
        cursor.execute(sql, (id))
        conn.commit()
    finally:
     cursor.close()
id = 1

#Indica el numero total de registros existentes en la tabla carrera
def contar_carreras():
    try:
        cursor = conn.cursor()
        
        sql = "SELECT COUNT(*) FROM carrera"
        cursor.execute(sql)
        total_carreras = cursor.fetchone()[0]
        print(f"Número total de carreras en la tabla: {total_carreras}")
    finally:
        cursor.close()


eliminar_carrera(id)
actualizar_carrera(cadigo_ca, nombre)
contar_carreras()
consulta_modalidad()
consulta_carreras()
insertar_carrera()

conn.close()
