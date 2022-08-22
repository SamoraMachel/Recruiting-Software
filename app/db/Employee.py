from dataclasses import dataclass
from typing import List
from app.db.Crud import Crud
from app.db._Password import _Password

@dataclass
class Employee(Crud, _Password):
    tablename = "Employee"
    
    name : str
    email: str
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
        
    def set_password(self, password: str):
        self._password = password