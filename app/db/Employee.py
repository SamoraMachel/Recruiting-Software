from dataclasses import dataclass
from typing import List
from app.db.Crud import Crud
import hashlib

@dataclass
class Employee(Crud):
    tablename = "Employee"
    
    name : str
    email: str
    password: str
    photo: str = None
    skills: List[str] = None
    education: List[dict] = None  # {"Undergraduate": {"Institution": "", "CertificateName":"", "CertificateFile":"", "StartYear":"", "EndYear":""}}
    resume: str = None
    social_media : dict = None
    blogs: list = None
    tools: list = None 
    location: str = None
    volunteer_work: List[dict] = None # {}
    pay_range: dict = None
        
    def __hash_password(self, password: str):
        hash_object = hashlib.sha256(password.encode())
        return hash_object.hexdigest()
    
    def _verify_password(self, password_entry: str) -> bool:
        password_entry_hash = self.__hash_password(password_entry)
        return self.password == password_entry_hash
    
    def toArray(self):
        self.password = self.__hash_password(self.password)
        return super().toArray()