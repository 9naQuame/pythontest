#!/usr/bin/env python

from wsgiref.simple_server import make_server
from cgi import parse_qs, escape

html = """
<html>
<body>
   <form method="get" action="parsing_get.wsgi">
      <p>
         Age: <input type="text" name="age">
         </p>
      <p>
         Hobbies:
         <input name="hobbies" type="checkbox" value="software"> Software
         <input name="hobbies" type="checkbox" value="tunning"> Auto Tunning
         </p>
      <p>
         <input type="submit" value="Submit">
         </p>
      </form>
   <p>
      Age: %s<br>
      Hobbies: %s
      </p>
   </body>
</html>"""

def application(environ, start_response):

# Returns a dictionary containing lists as values.
    d = parse_qs(environ['QUERY_STRING'])
    age = d.get('age', [''])[0] # Returns the first age value.
    hobbies = d.get('hobbies', []) # Returns a list of hobbies.
    age = escape(age)
    hobbies = [escape(hobby) for hobby in hobbies]

    response_body = html % (age or 'Empty',
               ', '.join(hobbies or ['No Hobbies']))

    status = '200 OK'
    response_headers = [('Content-Type', 'text/html'),
                  ('Content-Length', str(len(response_body)))]
    start_response(status, response_headers)

    return [response_body]

httpd = make_server('localhost', 8080, application)
# Now it is serve_forever() in instead of handle_request().
# In Windows you can kill it in the Task Manager (python.exe).
# In Linux a Ctrl-C will do it.
httpd.serve_forever()