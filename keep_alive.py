from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    # This returns a minimal HTML page directly
    return '<!doctype html><html><head><title>Lightweight Page</title></head><body><p>Alhamdu, lillah!</p></body></html>'

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

if __name__ == "__main__":
    keep_alive()
