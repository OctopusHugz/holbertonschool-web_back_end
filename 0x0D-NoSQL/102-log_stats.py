#!/usr/bin/env python3
""" This module creates a script for interacting with log stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    collection = db.nginx
    all_docs = collection.find()
    total_count = collection.count_documents({})
    get_count = collection.count_documents({"method": "GET"})
    post_count = collection.count_documents({"method": "POST"})
    put_count = collection.count_documents({"method": "PUT"})
    patch_count = collection.count_documents({"method": "PATCH"})
    delete_count = collection.count_documents({"method": "DELETE"})
    status_count = collection.count_documents({"path": "/status"})
    print(f"{total_count} logs\nMethods:")
    print(f"\tmethod GET: {get_count}")
    print(f"\tmethod POST: {post_count}")
    print(f"\tmethod PUT: {put_count}")
    print(f"\tmethod PATCH: {patch_count}")
    print(f"\tmethod DELETE: {delete_count}")
    print(f"{status_count} status check")
    print("IPs:")

    pipeline = [
        {"$group": {
            "_id": "$ip",
            "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ]
    ip_list = collection.aggregate(pipeline)
    for ip in ip_list:
        ip_addr = ip.get("_id")
        ip_count = ip.get("count")
        print(f"\t{ip_addr}: {ip_count}")
