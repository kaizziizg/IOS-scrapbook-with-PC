from flask import Flask
from flask import request
import pyperclip
import socket
import webbrowser

def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
print("ip: ",get_host_ip())
print("請將IP_2更改為: ",get_host_ip()[8:])

app = Flask(__name__)  # __name__ 代表目前執行的模組


@app.route("/copy")  
def PC2IOS():
    #這邊的paste 相當於Ctrl + V 把剪貼簿上的文字放入變數中
    paste = pyperclip.paste()
    return paste


@app.route("/paste", methods=['GET'])  
def IOS2PC():
    get_paste = request.values.get('paste') 
    if(get_paste):
        #這邊看有沒有包含http 如果有就複製並打開
        if("http" in str(get_paste)):
            pyperclip.copy(str(get_paste))
            webbrowser.open(str(get_paste))
        else:
            pyperclip.copy(str(get_paste))
            return str(get_paste)
    else:
        pyperclip.copy("COPY error!")
        return "COPY error"


if __name__ == "__main__":  
    app.run(host=get_host_ip(), port=8080) #啟動伺服器

