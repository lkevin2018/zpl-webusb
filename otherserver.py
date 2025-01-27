import http.server
import ssl

# Create an HTTP server
httpd = http.server.HTTPServer(
    ('localhost', 4443), http.server.SimpleHTTPRequestHandler
)

# Create an SSL context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

# Load the certificate and key files
context.load_cert_chain(certfile='./cert.pem', keyfile='./key.pem')

# Wrap the server's socket with the SSL context
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

# Serve HTTPS requests
print("Serving on https://localhost:4443")
httpd.serve_forever()