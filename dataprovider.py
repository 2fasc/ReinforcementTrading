"""
author: fasc
conda: py36
licence: MIT

changelog:
-6/7/18     created
"""
import requests

def load_API_key():
    with open('API_key.txt', 'r') as f:
        data = f.read()
    return str(data)


def parser():
    pass


def main():
    print(load_API_key())


if __name__ == "__main__":
    main()
