#!/usr/bin/python3

import webapp

PORT = 1234


def form():

    forms = """
    <form action = "/" method = POST> url:<br>
        <input type ="text" name="url" placeholder="URL to short"><br>
        
        <input type ="Submit" value = "Send">
    """
    return forms


class CMS(webapp.webApp):

    long_url = {}
    short_url = {}
    list_url = ""
    s_url = ""

    def parse(self, request):

        method, resource, _ = request.split(' ', 2)

        if method == "POST":
            body = request.split('\r\n\r\n')[1].split('=')[1]
            if len(body.split("%3A%2F%2F")) == 1:
                url = "http://" + body.split('%', 1)[1]
            else:
                url = "https://" + body.split("%3A%2F%2F", 1).split('%', 1)[0]

        else:

            body = " "
            url = body

        print(url)

        return(method,
               resource,
               url)

    def process(self, parse_request):

        method, resource, url = parse_request
        html_form = form()

        if method == "GET":
            if resource == "":
                code = "200 OK"
                body = "<html>url<br>" + html_form + \
                       "<table><tr><td>URL</td><td>short_url</td></tr><tr><td>" + self.list_url + "</td><td>" +\
                       self.sh_url + "</td></tr></table></html>"

            elif resource == "favicon.ico":



if __name__ == '__main__':
    try:
        testWebApp = CMS("localhost", PORT)
    except KeyboardInterrupt:
        print("closing binded socket")
