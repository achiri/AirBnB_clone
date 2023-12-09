import uuid
from datetime import datetime


class
 
BaseModel:

    
def
 
__init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def __str__(self):
        return f"[<class {self.__class__.__name__}>] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        data = self.__dict__.copy()
        data["created_at"] = self.created_at.isoformat()
        data["updated_at"] = self.updated_at.isoformat()
        data["__class__"] = self.__class__.__name__
        return data
