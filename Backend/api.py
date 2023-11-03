from flask import Flask, jsonify, request
from flask_cors import CORS
import time
import Proyecto1
import boto3
import os
global_text = ""

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/execute', methods=['POST'])
def get_first_word():
    
    
    data = request.get_json()
    message = data.get('command', '')
    print(message)
    # Dividir el mensaje en palabras
    words = message.split()
    global_text = Proyecto1.new_start(message)
    print(global_text + "Esta es una prueba")

    if words:
        message = f'[Success] => comando {global_text} ejecutado exitosamente'
    else:
        message = "No se encontraron palabras en el mensaje."

    respuesta = {
        'estado': 'OK',
        'mensaje': message,
        'respuestas': global_text
    }
    

    # Esperamos 1 segundo, para simular proceso de ejecución
    time.sleep(1)
    global_text = ""

    return jsonify(respuesta)



@app.route("/reports", methods=['GET'])
def get_report_names():
    aws_access_key_id = os.getenv('ACCES_ID')
    aws_secret_access_key = os.getenv('SECRET_ID')
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    response = s3.list_objects_v2(Bucket='proyecto2-archivos-202010770')
    #print(response)


    reporte = []

    try:
        for obj in response['Contents']:
            reporte.append(obj['Key'])
            #print(obj)
    except KeyError:
        pass

    return jsonify({'data': reporte,
                    'respuesta': 'success'})
if __name__ == '__main__':
    app.run(debug=True)
