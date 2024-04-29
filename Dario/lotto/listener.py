import requests
import socket
import json

SERVER_IP = "85.215.241.148"

class Listener:
    def __init__(self):
        self.server_ip = SERVER_IP

    def listen(self):
        while True:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.bind((self.server_ip, 8080))
                    s.listen(1)
                    print("Listening for requests...")
                    conn, addr = s.accept()
                    print("Connected to:", addr)
                    data = conn.recv(1024).decode()
                    if data:
                        json_data = json.loads(data)
                        self.handle_cases(json_data)
                    conn.close()
            except Exception as e:
                print("Error:", e)

    def handle_cases(self, json_data):
        if "case1" in json_data:
            self.handle_case1(json_data["case1"])
        elif "case2" in json_data:
            self.handle_case2(json_data["case2"])
        else:
            print("Unknown case:", json_data)

    def handle_case1(self, data):
        print("Handling case1:", data)

    def handle_case2(self, data):
        print("Handling case2:", data)


listener = Listener()
listener.listen()