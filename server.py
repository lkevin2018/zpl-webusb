import http.server
import ssl

httpd = http.server.HTTPServer(
    ('localhost', 4443), http.server.SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile='./cert.pem', keyfile='./key.pem')

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()