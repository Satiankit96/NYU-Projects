import json
import socket
import pickle

import requests
from flask import Flask, request

import logging as log
log.basicConfig(format='[fibonacci server: %(asctime)s] %(message)s',
                datefmt='%I:%M:%S %p',
                level=log.INFO)

app = Flask(__name__)


BUFFER_SIZE = 1024

@app.route('/')
def blah():
    return "This is fibonacci server"

def fib(n):
    if n < 0:
        raise ValueError(f"n should be > 0, got n={n}")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

@app.route('/fibonacci')
def fibonacci():
    n = int(request.args.get('number'))
    log.info(f"/fibonacci got n={n}")
    return str(fib(n))

def register_with_as(as_ip, as_port, hostname, value, type, ttl):
    msg = ((hostname, value, type, ttl))
    msg_bytes = pickle.dumps(msg)
    as_addr = (as_ip, as_port)
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.sendto(msg_bytes, as_addr)

@app.route('/register', methods=['PUT'])
def register():
    body = request.json
    print(f"/register got body={body!r}")
    if not body:
        raise ValueError("body is None")
    hostname = body["hostname"]
    fs_ip    = body["fs_ip"]
    as_ip    = body["as_ip"]
    as_port  = body["as_port"]
    ttl      = body["ttl"]
    register_with_as(as_port=as_port,
                     as_ip=as_ip,
                     hostname=hostname,
                     value=fs_ip,
                     type="A",
                     ttl=ttl)
    return "Registration Done!"

# def main():
#     # dns_record = ("Hello from UDP Client", 123, )
#     dns_record = ("A",
#                   "fibonacci.com",
#                   "localhost",
#                   5)
#     register_wit_as(*dns_record)
#     response = ""
#     # while not response:
#     for i in range(8):
#         import time
#         time.sleep(1)
#         send_mssg_to_authoritative_server(("A", "fibonacci.com"))
#         response, _ = SERVER_UDP_SOCKET.recvfrom(BUFFER_SIZE)
#         response = pickle.loads(response)
#         log.info("Message from Server {}\n".format(response))
#
#     send_mssg_to_authoritative_server(("A", "fibonacci2.com"))


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            port=9090,
            debug=True)
