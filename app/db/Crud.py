from os import getenv
from typing import List
from app.db import create_db
from dotenv import load_dotenv
from abc import ABC, abstractmethod
import json


load_dotenv()

class Crud:
    database = create_db()
    tablename = None
    schema = getenv("HARPER_SCHEMA")
    
    def checkTableName(self):
        return self.tablename

    @classmethod
    def read(cls, attributes=["*"]) :
        data = cls.database.search_by_value(cls.schema, cls.tablename, "id", attributes)
        return data
    
    @classmethod
    def readByValue(cls, field, attributes=["*"]):
        data = cls.database.search_by_value(cls.schema, cls.tablename, field, attributes)
        return data
    
    @classmethod
    def retrieveSpecificRecords(cls, ids : List[str]):
        record = cls.database.search_by_hash(cls.schema, cls.tablename, ids)
        return record
    
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
    
    @classmethod
    def toClassObject(cls, data: dict):
        instance = Crud.__new__(cls)
        for key in data:
            setattr(instance, key, data[key])
    
        return instance