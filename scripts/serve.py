#!/usr/bin/env python3
"""Local preview for the Voye landing page.

Serves the repository root but only exposes site files: dotfiles (.git, ...)
and the source-asset folders are hidden. Run:

    python3 scripts/serve.py          # http://localhost:3000
    PORT=8080 python3 scripts/serve.py
"""
import http.server
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HIDDEN_TOP_LEVEL = {"assets-inbox", "scripts"}


class SiteHandler(http.server.SimpleHTTPRequestHandler):
    def send_head(self):
        path = self.path.split("?", 1)[0].split("#", 1)[0].lstrip("/")
        top = path.split("/", 1)[0]
        if top.startswith(".") or top in HIDDEN_TOP_LEVEL:
            self.send_error(404, "Not found")
            return None
        return super().send_head()

    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


if __name__ == "__main__":
    os.chdir(ROOT)
    port = int(os.environ.get("PORT", "3000"))
    server = http.server.ThreadingHTTPServer(("0.0.0.0", port), SiteHandler)
    print(f"Serving Voye landing page on http://0.0.0.0:{port}")
    server.serve_forever()
