import bpy
from bpy.types import Operator

import http.server
import socketserver
import threading
from urllib.parse import urlparse
from urllib.parse import parse_qs
import math
import json

class ServerData():
    def __init__(self):
        self.data = None
        self.port = 8004
    
    def putData(self,dataString):
        self.data = dataString

data = ServerData()

class RLTOBLENDER_OT_Start_Socket_Connection_Op(Operator):
    bl_idname = "generic.start_socket_connection"
    bl_label = "Start RL Connection"
    bl_description = "Starts a webserver to retrieve data from RL"

    def __init__(self):
        self.running = False
    

    # @classmethod
    # def poll(cls, context):
    #     # A poll method is a class method (much like a static method not bound to the object). It returns a boolean value for if it should run the code or not
    #     pass        

    def execute(self, context):
        # Starts websocket
        self.handler = HttpHandler
        self.thread = threading.Thread(target=self.HTTPThread)
        self.thread.start()
        return {'FINISHED'}

    
    def HTTPThread(self):
        server = socketserver.TCPServer(("", data.port), self.handler)
        print(threading.current_thread().name, "Running")
        print(threading.current_thread().ident)
        print("Server started at localhost:" + str(data.port))
        server.serve_forever()
        # httpd.shutdown


class HttpHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()

        self.query = parse_qs(urlparse(self.path).query)
        self.data = json.loads(self.query["data"][0])
        # print(self.data)
        data.putData(self.data)
        # print(data.data)

        self.wfile.write(bytes(f"<html></html>", "utf8"))
        return

    def log_message(self, format, *args):
        pass


class RLTOBLENDER_OT_Print_Data(Operator):
    bl_idname = "generic.print_data"
    bl_label = "Print Data"
    bl_description = "Prints Current Data"
    port = 8004

    # @classmethod
    # def poll(cls, context):
    #     # A poll method is a class method (much like a static method not bound to the object). It returns a boolean value for if it should run the code or not
    #     pass        

    def execute(self, context):
        # Starts websocket
        print(data.data)
        return {'FINISHED'}