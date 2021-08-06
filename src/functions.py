import webbrowser
import json
from time import sleep


def wget(url):
    webbrowser.open(url)


def readfile(filename):
    if filename.endswith(".json"):
        with open(filename) as file_handler:
            content = json.load(file_handler)
    else:
        file_handler = open(filename, 'r')
        content = file_handler.read()
        file_handler.close()
    return content


def verify(username, password):
    uname = readfile('config/config.json')
    uname = uname["username"]
    passwd = readfile('config/config.json')
    passwd = passwd["password"]

    if username != uname or password != passwd:
        print("Verification failed. Incorrect username or password.")
        sleep(10)
        exit()


def sudo():
    attempt_count = 0
    attempt_limit = 3
    uname = readfile('config/config.json')
    uname = uname["username"]
    passwd = readfile('config/config.json')
    passwd = passwd["password"]
    while attempt_count < attempt_limit:
        password = input(f"[sudo] password for {uname}: ")
        attempt_count += 1
        if password == passwd:
            break
        else:
            print("Sorry, try again")
    else:
        print("sudo: 3 incorrect password attempts")
