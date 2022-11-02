from dotenv import load_dotenv
from pymongo import MongoClient
import json

from os import getenv 


class MongoDB:

    load_dotenv()

    def __init__(self, cluster: str, table: str):
        self.cluster = cluster
        self.table = table

    def _connect(self) -> MongoClient:
        return MongoClient(getenv("MONGO_URL"))[self.cluster][self.table]

    def create(self, data: dict):
        self._connect().insert_many(dict(data))
        return data

    def read(self, query: dict) -> list[dict]:
        return list(self._connect().find(query, {"_id": False}))

    def update(self, query: dict, update_data: dict):
        n_changed_records = self.count(query)
        self._connect().update_many(query, {"$set": update_data})
        return n_changed_records

    def delete(self, query: dict):
        self._connect().delete_many(query)

    def count(self, query: dict) -> int:
        return self._connect().count_documents(query)

    def backup(self):
        with open("data.json", "w") as file:
            json.dump(self.read(), file)

    def create_index(self):
        self._connect().create_index([("$**", "text")])

    def drop_index(self):
        self._connect().drop_index([("$**", "text")])

    def search(self, user_search: str):
        return self.read({"$text": {"$search": user_search}})


# if __name__ == '__main__':
#     mongo = MongoDB("TestCluster", "TestTable")
#     # mongo.create({
#     #     "id": 321654987,
#     #     "Filename": "Filepath",
#     # })
#     print(*mongo.read({'id': 321654987}))