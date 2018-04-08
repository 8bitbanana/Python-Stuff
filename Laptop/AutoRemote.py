import urllib.request, urllib.parse

url = "https://autoremotejoaomgcd.appspot.com/sendmessage?key=[redacted]&message={}"


def main():
    print()
    print("AutoRemote Communicate")
    print()
    while True:
        message = input("SEND > ")
        if message == "":
            continue
        message = urllib.parse.quote(message, "")
        print(message)
        urllib.request.urlopen(url.format(message))
        print()


if __name__ == "__main__":
    main()
