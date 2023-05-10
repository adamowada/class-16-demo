from http.server import BaseHTTPRequestHandler, HTTPServer
# new
from urllib import parse


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Take the url string, and create a dictionary of the parameters
        url = self.path  # this is the url string
        print("self.path is:", url)
        url_components = parse.urlsplit(url)  # is the SplitResult() object
        print("url_components is:", url_components)
        query_string_list = parse.parse_qsl(url_components.query)  # list of key value pair tuples, representing the query string
        print("query_string_list is:", query_string_list)
        dictionary = dict(query_string_list)
        print("dictionary is:", dictionary)

        # We can do stuff!
        # Here we build up a message string
        name = dictionary.get("name")
        age = dictionary.get("age")
        print("name is:", name)

        message = f"Aloha {name}, you are {age} years old"

        # Forming the response
        self.send_response(200)  # HTTP code
        self.send_header('Content-type', 'text/plain')  # define the content type
        self.end_headers()  # add a blank line
        self.wfile.write(message.encode())  # write the message


if __name__ == '__main__':
    server_address = ('localhost', 8000)  # use any available port
    httpd = HTTPServer(server_address, handler)  # httpd is a commonly used abbreviation for "HTTP Daemon"
    print(f'Starting httpd server on {server_address[0]}:{server_address[1]}')
    httpd.serve_forever()
