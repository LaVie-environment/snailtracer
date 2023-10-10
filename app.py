import http.client
import os
import signal
import ssl
import sys
import time

TARGET = os.environ.get("TARGET")
METHOD = os.environ.get("METHOD")
INTERVAL = int(os.environ.get("INTERVAL"))

options = {
    "host": TARGET,
    "method": METHOD,
}

print(f"** web-ping ** Pinging: {options['host']}; method: {options['method']}; {INTERVAL}ms intervals")


def handle_sigint(signum, frame):
    sys.exit()


signal.signal(signal.SIGINT, handle_sigint)

i = 1
start = int(time.time() * 1000)


def make_request():
    global i, start
    start = int(time.time() * 1000)
    print(f"Making request number: {i}; at {start}")
    
    # Using HTTPSConnection
    conn = http.client.HTTPSConnection(options["host"], context=ssl._create_unverified_context())
    
    # Using HTTPConnection (uncomment the line below if you're not using HTTPS)
    # conn = http.client.HTTPConnection(options["host"])

    # Specify the method in the request
    conn.request(METHOD, "/")
    
    response = conn.getresponse()
    end = int(time.time() * 1000)
    duration = end - start
    print(f"Got response status: {response.status} at {end}; duration: {duration}ms")
    conn.close()



while True:
    make_request()
    i += 1
    time.sleep(INTERVAL / 1000)
