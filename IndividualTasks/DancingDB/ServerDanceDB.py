from http.server import HTTPServer, CGIHTTPRequestHandler
from SelectAllFromDB import *
from SpecialSelect import *
import threading

def start_server():
    server_address = ("localhost", 8000)  # Иногда хочет пустые кавычки
    http_server = HTTPServer(server_address, CGIHTTPRequestHandler)
    print("HTTP сервер запущен на http://localhost:8000")
    http_server.serve_forever()

def console_listener():
    while True:
        command = input("Введите команду: ").strip()
        if command == "SelectAll":
            print("Вызов функции SelectAll()")
            SelectAll()
        elif command == "SelectSpecial":
            print("Вызов функции SelectSpecial()")
            SelectSpecial()
        else:
            print(f"Неизвестная команда: {command}")

# Запуск сервера в отдельном потоке
server_thread = threading.Thread(target=start_server, daemon=True)
server_thread.start()

# Обработка консольных команд
console_listener()