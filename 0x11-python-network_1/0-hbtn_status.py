#!/usr/bin/python3

""" A Python script that fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    from urllib.request import urlopen, Request

    url = "https://alx-intranet.hbtn.io/status"
    req = Request(url)
    with urlopen(req) as res:
        content = res.read()

    print("Body response:")
    print("\t- type: ".format(type(content)))
    print("\t- content: ".format(content))
    print("\t- utf8 content: ".format(content.decode('utf-8')))
