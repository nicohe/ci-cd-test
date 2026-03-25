from flask import Flask, jsonify, request
from werkzeug.middleware.proxy_fix import ProxyFix
import datetime
import logging
import sys
import time

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='[%(asctime)s] [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

# Tiempo de inicio para calcular uptime
start_time = time.time()

# Middleware para logging de requests
@app.before_request
def log_request():
    logger.info(f'{request.method} {request.path} - IP: {request.remote_addr}')

@app.after_request
def log_response(response):
    logger.info(f'{request.method} {request.path} - Status: {response.status_code}')
    return response

@app.route('/')
def home():
    logger.info('Home endpoint accessed')
    return jsonify({
        'message': '¡Hola DevOps con Roxs!',
        'timestamp': datetime.datetime.now().isoformat(),
        'status': 'success'
    })

@app.route('/health')
def health():
    uptime_seconds = time.time() - start_time
    uptime_minutes = uptime_seconds / 60
    logger.info('Health check executed')
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat(),
        'uptime_seconds': round(uptime_seconds, 2),
        'uptime_minutes': round(uptime_minutes, 2),
        'message': '¡Mi aplicación está funcionando! 🎉'
    })

@app.route('/suma/<int:a>/<int:b>')
def suma(a, b):
    resultado = a + b
    logger.info(f'Suma: {a} + {b} = {resultado}')
    return jsonify({
        'operacion': 'suma',
        'numeros': [a, b],
        'resultado': resultado
    })

@app.route('/saludo/<nombre>')
def saludo(nombre):
    logger.info(f'Saludo a: {nombre}')
    return jsonify({
        'saludo': f'¡Hola {nombre}!',
        'mensaje': 'Bienvenido a mi aplicación'
    })

@app.route('/ping')
def ping():
    logger.info('Ping endpoint accessed')
    return jsonify({'message': 'pong', 'timestamp': datetime.datetime.now().isoformat()})

# Funciones para test
def multiplicar(a, b): return a * b
def es_par(n): return n % 2 == 0

if __name__ == '__main__':
    logger.info('==========================================')
    logger.info('Starting Flask application...')
    logger.info(f'Start time: {datetime.datetime.now().isoformat()}')
    logger.info('==========================================')
    app.run(debug=True, host='0.0.0.0', port=5000)