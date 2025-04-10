from pydantic import BaseModel
from datetime import date
from typing import Optional

class UsersignUp(BaseModel):
    full_name : str
    email : str
    password : int
    role: str  # Added role field
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class LoginUser(BaseModel):
    email : str
    password : str
    role: str  # Added role field
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class ContactForm(BaseModel):
    full_name: str
    email: str
    message: str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class ImageData(BaseModel):
    image: str
    plantName : str
    productType : str
    plantType : str
    plantDescription : str
    plantPrice : int
    uploaderEmail: str
    
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class FilterPlant(BaseModel):
    selectPlantType : str 
    selectFertilizerandSeeds : str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class ATC_Btn(BaseModel):
    email_id: str
    name: str
    price: int
    image : str 
    quantity : int
    total : int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class CartIcon(BaseModel):
    email_id : str
     
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class UpdateCartQuantityRequest(BaseModel):
    id: int
    quantity: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class RemoveCartItemRequest(BaseModel):
    itemId: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class OrderForm(BaseModel):
    email_or_phone : str
    news_offers_subscription : bool
    first_name: str
    last_name: str
    address: str
    apartment_details : str
    city : str
    state : str
    pin_code : int
    phone_number : int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
