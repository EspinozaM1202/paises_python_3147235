##importar, utilizar
# una dependencia en python

from flask import Flask, render_template

#Crear la aplicación de flask

app = Flask(__name__)

#Utilizar app para crear una ruta

@app.route('/prueba')
def prueba():
    #defino la lista de paises
    paises =[
        {
            'nombre': 'Argentina',
            'capital': 'Buenos Aires',
            'moneda': 'Peso argentino',
            'población': '45.54',
            'superficie': '2.78',
            'ciudades_principales': [
                                    'Rosario',
                                    'Resistencia',
                                    'Ciudad de corrientes',
                                  
                                    ]
        },
        {
            'nombre': 'Brasil',
            'capital': 'Brasilia',
            'moneda': 'Peso brasileño',
            'población': '211.1',
            'superficie': '8.51',
            'ciudades_principales': [
                                    'Rio de Janeiro',
                                    'São Paulo'
                                    ]
                                    
        },
        {
           'nombre': 'Colombia',
            'capital': 'Bogotá',
            'moneda': 'Peso colombiano',
            'población': '52.32',
            'superficie': '1.142',
            'ciudades_principales': [
                                    'Medellin',
                                    'Cali',
                                    'Barranquilla' 
                                    ]          
        },
        {
            'nombre': 'Peru',
            'capital': 'Lima',
            'moneda': 'Sol peruano',
            'población': '33.85',
            'superficie': '1.285',
            'ciudades_principales': [
                                    'Arequipa',
                                    'Cusco'
                                    ]
        },
    ]
    
    #envio la lista de paises a la vista
    return render_template('paises.html', paises=paises, usuario="Mariana")