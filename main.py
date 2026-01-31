from http.server import HTTPServer, SimpleHTTPRequestHandler
import os


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Language Model Work</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .container {
            text-align: center;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            max-width: 500px;
        }
        h1 {
            color: #333;
            margin-bottom: 1rem;
            font-size: 2rem;
        }
        p {
            color: #666;
            line-height: 1.6;
            margin-bottom: 1rem;
        }
        .status {
            display: inline-block;
            padding: 0.5rem 1rem;
            background: #4CAF50;
            color: white;
            border-radius: 20px;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Language Model Work</h1>
        <p>Your Python project is ready for development.</p>
        <span class="status">Server Running</span>
    </div>
</body>
</html>'''
            self.wfile.write(html.encode())
        else:
            super().do_GET()


def run(port=5000):
    server_address = ('0.0.0.0', port)
    httpd = HTTPServer(server_address, NoCacheHandler)
    print(f"Server running on http://0.0.0.0:{port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
