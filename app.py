from app import create_app
import os
from flask import Flask

app= create_app()

print("Puerto asignado por Render:", os.environ.get("PORT"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Toma el puerto que Render asigna, o usa 5000 por defecto localmente
    app.run(host="0.0.0.0", port=port)