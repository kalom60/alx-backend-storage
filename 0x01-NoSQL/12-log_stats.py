#!/usr/bin/env python3
"""Log stat"""


from pymongo import MongoClient


def log():
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx = client.logs.nginx

    print(f'{nginx.count_documents({})} logs')
    print('Methods:')
    reqs = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for req in reqs:
        print("\tmethod {}: {}".format(req, nginx.count_documents({"method": req})))
    print("{} status check".format(nginx.count_documents({"path": "/status"})))


if __name__ == "__main__":
    log()
