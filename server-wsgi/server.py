# A simple server using WSGI.

from wsgiref.simple_server import make_server

def simple_app(environ, start_response):

    #set status and HTTP header for response, both needed.
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    start_response(status, headers)

    #HTML body to be rendered
    body = [("hello, WSGI server").encode("utf-8") ]

    return body

# define server daemon
httpd = make_server('localhost', 8000, simple_app)
print("WSGI server on port 8000...")

#server
httpd.serve_forever()