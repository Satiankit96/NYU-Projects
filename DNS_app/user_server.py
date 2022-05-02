import pickle
import socket

from flask import Flask, request

import logging as log
log.basicConfig(format='[%(asctime)s] %(message)s',
                datefmt='%I:%M:%S %p',
                level=log.INFO)

app = Flask(__name__)


BUFFER_SIZE = 1024

@app.route('/')
def hello_world():
    return 'Hello world! This is User Server'


def get_fs_ip_from_as(hostname, as_ip, as_port):
    # fs_ip = "localhost"
    as_addr = (as_ip, as_port)
    SERVER_UDP_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    msg_bytes = pickle.dumps(("A", hostname))
    SERVER_UDP_SOCKET.sendto(msg_bytes, as_addr)
    response, _ = SERVER_UDP_SOCKET.recvfrom(BUFFER_SIZE)
    response = pickle.loads(response)
    type, hostname, fs_ip, ttl = response
    log.info(f"Resolved fs{hostname} to IP {fs_ip}")


@app.route('/fibonacci', methods=["GET"])
def fibonacci():
    # Fibonacci Server hostname
    hostname = request.args.get('hostname')
    fs_port  = request.args.get('fs_port')
    # Fibonacci number to calculate
    number   = request.args.get('number')
    # Authorative server IP, port
    as_ip    = request.args.get('as_ip')
    as_port  = request.args.get('as_port')
    fs_ip = get_fs_ip_from_as(hostname=hostname,
                              as_ip=as_ip,
                              as_port=as_port)

app.run(host='0.0.0.0',
        port=8080,
        debug=True)
