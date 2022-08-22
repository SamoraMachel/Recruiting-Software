from dataclasses import dataclass
import hashlib

@dataclass
class _Password:
    
    @property
    def _password(self):
        return self.password
    
    @_password.setter
    def _password(self, value):
        self.password = self.__hash_password__(value)
        
    def __hash_password__(self, password: str):
        hash_object = hashlib.sha256(password.encode())
        return hash_object.hexdigest()
    
    def _verify_password(self, password_entry: str) -> bool:
        password_entry_hash = self.__hash_password__(password_entry)
        return self.password == password_entry_hash
    