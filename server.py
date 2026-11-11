"""Serve the imported page without exposing project files."""

from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


PAGE = Path(__file__).with_name("index.html")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.serve_page(include_body=True)

    def do_HEAD(self):
        self.serve_page(include_body=False)

    def serve_page(self, include_body):
        if urlsplit(self.path).path not in ("/", "/index.html"):
            self.send_error(HTTPStatus.NOT_FOUND)
            return

        content = PAGE.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        if include_body:
            self.wfile.write(content)


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 5000), Handler).serve_forever()
