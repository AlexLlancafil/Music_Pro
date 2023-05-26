from flask import Flask, jsonify, redirect
import mysql.connector

app = Flask(__name__)

# Ruta de inicio para redirigir a la lista de productos
@app.route('/')
def inicio():
    return redirect('/productos')

# Ruta para obtener todos los productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    try:
        # Establecer conexión a la base de datos
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='contrasena',
            database='pruebabdd_2'
        )

        cursor = conexion.cursor()

        # Consulta SQL para obtener los productos
        consulta = "SELECT idProductos, nombre, descripcion, precio FROM productos"
        cursor.execute(consulta)

        # Obtener los resultados de la consulta
        resultados = cursor.fetchall()

        # Crear una lista de productos
        productos = []
        for producto in resultados:
            producto_dict = {
                "idProductos": producto[0],
                "nombre": producto[1],
                "descripcion": producto[2],
                "precio": producto[3]
            }
            productos.append(producto_dict)

        # Cerrar la conexión a la base de datos
        cursor.close()
        conexion.close()

        # Devolver la lista de productos como respuesta en formato JSON
        return jsonify(productos)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
