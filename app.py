
from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Attach Prometheus metrics
metrics = PrometheusMetrics(app)

@app.route('/')
def home():
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
