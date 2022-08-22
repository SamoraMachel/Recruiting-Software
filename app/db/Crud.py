from os import getenv
from typing import List
from app.db import create_db
from dotenv import load_dotenv
from abc import ABC
import json


load_dotenv()

class Crud:
    database = create_db()
    tablename = None
    schema = getenv("HARPER_SCHEMA")
    
    def checkTableName(self):
        return self.tablename

    def read(self):
        data = self.database.search_by_value(self.schema, self.tablename, "id", "*")
        return data
    
    # @ABC
    # def retrieveRecord(cls, ids : List[str]):
    #     record = cls.database.search_by_hash(cls.schema, cls.tablename, ids)
    
    def insert(self):
        self.database.insert(self.schema, self.tablename, self.toArray())
        
    def update(self):
        self.database.update(self.schema, self.tablename, self.toArray())
    
    def delete(self):
        self.database.delete(self.schema, self.tablename, self.id)
    
    def displayJson(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=4)
    
    def toArray(self):
        return [self.__dict__]