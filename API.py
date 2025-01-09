{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "8384923d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!pip install uvicorn\n",
    "from fastapi import FastAPI\n",
    "import uvicorn\n",
    "import os\n",
    "#import uvicorn\n",
    "#from flask import Flask, jsonify\n",
    "#from threading import Thread"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "33283960",
   "metadata": {},
   "outputs": [
    {
     "ename": "RuntimeError",
     "evalue": "asyncio.run() cannot be called from a running event loop",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
      "Cell \u001b[0;32mIn[29], line 13\u001b[0m\n\u001b[1;32m     10\u001b[0m port \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mint\u001b[39m(os\u001b[38;5;241m.\u001b[39menviron\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mPORT\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;241m8000\u001b[39m))\n\u001b[1;32m     12\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m\"\u001b[39m:\n\u001b[0;32m---> 13\u001b[0m     uvicorn\u001b[38;5;241m.\u001b[39mrun(app, host\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m0.0.0.0\u001b[39m\u001b[38;5;124m\"\u001b[39m, port\u001b[38;5;241m=\u001b[39mport)\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.11/site-packages/uvicorn/main.py:579\u001b[0m, in \u001b[0;36mrun\u001b[0;34m(app, host, port, uds, fd, loop, http, ws, ws_max_size, ws_max_queue, ws_ping_interval, ws_ping_timeout, ws_per_message_deflate, lifespan, interface, reload, reload_dirs, reload_includes, reload_excludes, reload_delay, workers, env_file, log_config, log_level, access_log, proxy_headers, server_header, date_header, forwarded_allow_ips, root_path, limit_concurrency, backlog, limit_max_requests, timeout_keep_alive, timeout_graceful_shutdown, ssl_keyfile, ssl_certfile, ssl_keyfile_password, ssl_version, ssl_cert_reqs, ssl_ca_certs, ssl_ciphers, headers, use_colors, app_dir, factory, h11_max_incomplete_event_size)\u001b[0m\n\u001b[1;32m    577\u001b[0m         Multiprocess(config, target\u001b[38;5;241m=\u001b[39mserver\u001b[38;5;241m.\u001b[39mrun, sockets\u001b[38;5;241m=\u001b[39m[sock])\u001b[38;5;241m.\u001b[39mrun()\n\u001b[1;32m    578\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m--> 579\u001b[0m         server\u001b[38;5;241m.\u001b[39mrun()\n\u001b[1;32m    580\u001b[0m \u001b[38;5;28;01mexcept\u001b[39;00m \u001b[38;5;167;01mKeyboardInterrupt\u001b[39;00m:\n\u001b[1;32m    581\u001b[0m     \u001b[38;5;28;01mpass\u001b[39;00m  \u001b[38;5;66;03m# pragma: full coverage\u001b[39;00m\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.11/site-packages/uvicorn/server.py:66\u001b[0m, in \u001b[0;36mServer.run\u001b[0;34m(self, sockets)\u001b[0m\n\u001b[1;32m     64\u001b[0m \u001b[38;5;28;01mdef\u001b[39;00m \u001b[38;5;21mrun\u001b[39m(\u001b[38;5;28mself\u001b[39m, sockets: \u001b[38;5;28mlist\u001b[39m[socket\u001b[38;5;241m.\u001b[39msocket] \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m) \u001b[38;5;241m-\u001b[39m\u001b[38;5;241m>\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m     65\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mconfig\u001b[38;5;241m.\u001b[39msetup_event_loop()\n\u001b[0;32m---> 66\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m asyncio\u001b[38;5;241m.\u001b[39mrun(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mserve(sockets\u001b[38;5;241m=\u001b[39msockets))\n",
      "File \u001b[0;32m~/anaconda3/lib/python3.11/asyncio/runners.py:186\u001b[0m, in \u001b[0;36mrun\u001b[0;34m(main, debug)\u001b[0m\n\u001b[1;32m    161\u001b[0m \u001b[38;5;250m\u001b[39m\u001b[38;5;124;03m\"\"\"Execute the coroutine and return the result.\u001b[39;00m\n\u001b[1;32m    162\u001b[0m \n\u001b[1;32m    163\u001b[0m \u001b[38;5;124;03mThis function runs the passed coroutine, taking care of\u001b[39;00m\n\u001b[0;32m   (...)\u001b[0m\n\u001b[1;32m    182\u001b[0m \u001b[38;5;124;03m    asyncio.run(main())\u001b[39;00m\n\u001b[1;32m    183\u001b[0m \u001b[38;5;124;03m\"\"\"\u001b[39;00m\n\u001b[1;32m    184\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m events\u001b[38;5;241m.\u001b[39m_get_running_loop() \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m:\n\u001b[1;32m    185\u001b[0m     \u001b[38;5;66;03m# fail fast with short traceback\u001b[39;00m\n\u001b[0;32m--> 186\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mRuntimeError\u001b[39;00m(\n\u001b[1;32m    187\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124masyncio.run() cannot be called from a running event loop\u001b[39m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m    189\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m Runner(debug\u001b[38;5;241m=\u001b[39mdebug) \u001b[38;5;28;01mas\u001b[39;00m runner:\n\u001b[1;32m    190\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m runner\u001b[38;5;241m.\u001b[39mrun(main)\n",
      "\u001b[0;31mRuntimeError\u001b[0m: asyncio.run() cannot be called from a running event loop"
     ]
    }
   ],
   "source": [
    "data = {'name': \"Pedro\", \"name2\": \"Juan\"}\n",
    "app = FastAPI()\n",
    "\n",
    "@app.get(\"/my-first-api\")\n",
    "def hello():\n",
    "  return data\n",
    "\n",
    "\n",
    "# Tomar el puerto de la variable de entorno, si está definida\n",
    "port = int(os.environ.get(\"PORT\", 8000))\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    uvicorn.run(app, host=\"0.0.0.0\", port=port)\n",
    "\n",
    "uvicorn API:app --reload"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "ab1da4c9",
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
   "id": "86c8dc98",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fc2f592a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6121c577",
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
   "id": "a62f8cc8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d6d1091a",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8cd34840",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b341756d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "463db1bb",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f7f44eaf",
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
