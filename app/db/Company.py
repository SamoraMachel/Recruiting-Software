from dataclasses import dataclass
from app.db.Crud import Crud
import hashlib

@dataclass
class Company(Crud):
    tablename = "Company"
    
    company_name : str
    email : str
    password : str 
    location : str = None
    website: str = None
    social_media : str = None
    
    def __hash_password(self, password: str):
        hash_object = hashlib.sha256(password.encode())
        return hash_object.hexdigest()
    
    def _verify_password(self, password_entry: str) -> bool:
        password_entry_hash = self.__hash_password(password_entry)
        return self.password == password_entry_hash
    
    def toArray(self):
        self.password = self.__hash_password(self.password)
        return super().toArray()