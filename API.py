{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "8384923d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!pip install uvicorn\n",
    "from fastapi import FastAPI\n",
    "import uvicorn\n",
    "#import uvicorn\n",
    "#from flask import Flask, jsonify\n",
    "#from threading import Thread"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "c3130537",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {'name': \"Pedro\", \"name2\": \"Juan\"}\n",
    "app = FastAPI()\n",
    "\n",
    "@app.get(\"/my-first-api\")\n",
    "def hello():\n",
    "  return data\n",
    "uvicorn API:app --reload"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "c50f031f",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (<ipython-input-25-8fcffc15832e>, line 7)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  Cell \u001b[0;32mIn[25], line 7\u001b[0;36m\u001b[0m\n\u001b[0;31m    uvicorn API:app --reload\u001b[0m\n\u001b[0m            ^\u001b[0m\n\u001b[0;31mSyntaxError\u001b[0m\u001b[0;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f70b0ff",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f979f917",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d9584711",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "6194a81b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
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
      " * Restarting with watchdog (fsevents)\n"
     ]
    },
    {
     "ename": "SystemExit",
     "evalue": "1",
     "output_type": "error",
     "traceback": [
      "An exception has occurred, use %tb to see the full traceback.\n",
      "\u001b[0;31mSystemExit\u001b[0m\u001b[0;31m:\u001b[0m 1\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/Users/miguelrosales/anaconda3/lib/python3.11/site-packages/IPython/core/interactiveshell.py:3534: UserWarning: To exit: use 'exit', 'quit', or Ctrl-D.\n",
      "  warn(\"To exit: use 'exit', 'quit', or Ctrl-D.\", stacklevel=1)\n"
     ]
    }
   ],
   "source": [
    "app = FastAPI()\n",
    "\n",
    "@app.get(\"/my-first-api\")\n",
    "def hello():\n",
    "  return {\"Hello world!\"}\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bc6cc0f5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0f076c5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "592d6ec2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66b269da",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8be31e8c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77ffd87c",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e90362e1",
   "metadata": {},
   "outputs": [],
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
