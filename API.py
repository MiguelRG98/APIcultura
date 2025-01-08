{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8384923d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, jsonify\n",
    "#from threading import Thread"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "6194a81b",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(\"Agricultura\")\n",
    "\n",
    "# Datos de ejemplo\n",
    "datos = {\n",
    "    \"usuarios\": [\n",
    "        {\"id\": 1, \"nombre\": \"Juan\", \"edad\": 25},\n",
    "        {\"id\": 2, \"nombre\": \"Ana\", \"edad\": 30},\n",
    "        {\"id\": 3, \"nombre\": \"Carlos\", \"edad\": 35}\n",
    "    ]\n",
    "}\n",
    "\n",
    "@app.route('/api/datos', methods=['GET'])\n",
    "def obtener_datos():\n",
    "    return jsonify(datos)\n",
    "\n",
    "if \"Agricultura\" == '__main__':\n",
    "    app.run(debug=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e90362e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app 'Agricultura'\n",
      " * Debug mode: on\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [08/Jan/2025 13:45:24] \"GET / HTTP/1.1\" 404 -\n",
      "127.0.0.1 - - [08/Jan/2025 13:45:24] \"GET /favicon.ico HTTP/1.1\" 404 -\n",
      "127.0.0.1 - - [08/Jan/2025 13:46:07] \"GET / HTTP/1.1\" 404 -\n",
      "127.0.0.1 - - [08/Jan/2025 13:47:27] \"GET /api/datos HTTP/1.1\" 200 -\n"
     ]
    }
   ],
   "source": [
    "#def run_flask():\n",
    "#    app.run(port=5000, debug=True, use_reloader=False)  # El use_reloader=False evita reiniciar dos veces\n",
    "#\n",
    "## Iniciar el servidor Flask en segundo plano\n",
    "#thread = Thread(target=run_flask)\n",
    "#thread.start()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ac821ba",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d527beb3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e82149d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "009aff61",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
