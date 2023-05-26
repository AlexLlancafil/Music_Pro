from flask import Flask, jsonify, redirect, request
import mysql.connector
import requests

app = Flask(__name__)

# Ruta de inicio para redirigir a la lista de productos
@app.route('/')
def inicio():
    return redirect('/clientes')

# Ruta para obtener todos los clientes
@app.route('/clientes', methods=['GET'])
def obtener_clientes():
    try:
        # Código existente para obtener la información de los clientes
        # y devolver la respuesta adecuada
        return jsonify({'mensaje': 'Obtener clientes'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ruta para agregar un nuevo cliente
@app.route('/clientes', methods=['POST'])
def agregar_cliente():
    try:
        # Obtener los datos del nuevo cliente desde la solicitud
        datos_cliente = request.get_json()
        nombre = datos_cliente.get('nombre')
        edad = datos_cliente.get('edad')
        direccion = datos_cliente.get('direccion')
        idProductos = datos_cliente.get('idProductos')
        idPeso = datos_cliente.get('idPeso')
        dDolar = datos_cliente.get('dDolar')

        # Establecer conexión a la base de datos
        conexion = mysql.connector.connect(
            host='localhost',
            user='root',
            password='contrasena',
            database='pruebabdd_2'
        )

        cursor = conexion.cursor()

        # Consulta SQL para agregar un nuevo cliente
        consulta = "INSERT INTO cliente (idCliente, nombre, edad, direccion, idProductos, idPeso, dDolar) VALUES (NULL, %s, %s, %s, %s, %s, %s)"
        valores = (nombre, edad, direccion, idProductos, idPeso, dDolar)
        cursor.execute(consulta, valores)

        # Confirmar los cambios en la base de datos
        conexion.commit()

        # Cerrar la conexión a la base de datos
        cursor.close()
        conexion.close()

        return jsonify({'mensaje': 'Cliente agregado correctamente'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
