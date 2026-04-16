from dataclasses import dataclass, field
import datetime

@dataclass
class Category:
    name : str
    icon : str
    color : str
    id : int | None = None
@dataclass
class Expense:
    amount : float
    description : str
    category_id : int
    date : datetime.date
    id : int | None = None
    created_at : datetime.datetime = field(default_factory=datetime.datetime.now)
    
@dataclass
class Budget:
    category_id : int
    limit : float
    month : int
    year : int 
    id : int | None = None