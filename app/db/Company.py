from dataclasses import dataclass
from app.db.Crud import Crud
from app.db._Password import _Password

@dataclass
class Company(Crud, _Password):
    tablename = "Company"
    
    company_name : str
    email : str
    location : str = None
    website: str = None
    social_media : str = None
    
    def set_password(self, password: str):
        self._password = password