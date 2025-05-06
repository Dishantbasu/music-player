import http.server
import socketserver
import os
import json

PORT = 8060
SONG_FOLDER = "songs"

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/songs":
            songs = [f for f in os.listdir(SONG_FOLDER) if f.endswith(".mp3")]
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(songs).encode())
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving at http://0.0.0.0:{PORT}")
    httpd.serve_forever()
