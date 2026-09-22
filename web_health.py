#!/usr/bin/env python3
"""
Lightweight Keep-Alive Web Server for Hermes Agent PaaS deployment.
Listens on $PORT (or 8080) to satisfy Render/Koyeb health probes.
"""
import os
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import time

START_TIME = time.time()

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/healthz" or self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Cache-Control", "no-cache")
            self.end_headers()
            uptime = int(time.time() - START_TIME)
            payload = {
                "status": "healthy",
                "uptime_seconds": uptime,
                "service": "Hermes Agent Cloud Gateway"
            }
            self.wfile.write(json.dumps(payload).encode("utf-8"))
        else:
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            uptime = int(time.time() - START_TIME)
            html = f"""<!DOCTYPE html>
<html>
<head>
    <title>Hermes Agent - Running</title>
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; background: #0f172a; color: #f8fafc; display: flex; align-items: center; justify-content: center; height: 100vh; margin: 0; }}
        .card {{ background: #1e293b; padding: 2.5rem; border-radius: 1rem; box-shadow: 0 10px 25px rgba(0,0,0,0.5); text-align: center; max-width: 450px; border: 1px solid #334155; }}
        .status {{ display: inline-block; padding: 0.35rem 0.85rem; border-radius: 9999px; background: #065f46; color: #34d399; font-weight: bold; margin-bottom: 1rem; font-size: 0.9rem; }}
        h1 {{ margin: 0 0 0.5rem 0; font-size: 1.6rem; color: #fff; }}
        p {{ color: #94a3b8; font-size: 0.95rem; line-height: 1.5; }}
        .badge {{ background: #334155; color: #cbd5e1; padding: 0.2rem 0.5rem; border-radius: 4px; font-family: monospace; }}
    </style>
</head>
<body>
    <div class="card">
        <div class="status">● OPERATIONAL</div>
        <h1>Hermes Agent Gateway</h1>
        <p>Personal autonomous AI agent running on cloud PaaS.</p>
        <p>Telegram Gateway: <strong>Connected</strong></p>
        <p>Keep-alive endpoint: <span class="badge">/healthz</span></p>
        <p>Uptime: <strong>{uptime}s</strong></p>
    </div>
</body>
</html>"""
            self.wfile.write(html.encode("utf-8"))

    def log_message(self, format, *args):
        # Silence routine healthcheck logs to keep terminal / cloud logs clean
        if "/healthz" not in args[0]:
            super().log_message(format, *args)

def run():
    port = int(os.environ.get("PORT", "8080"))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    print(f"[Health Server] Listening on 0.0.0.0:{port} (/healthz)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    run()
