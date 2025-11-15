from pydantic import BaseModel, Field
from typing import Optional


class CartItemBase(BaseModel):
    product_id: int = Field( ..., description= " Product ID")
    quantity: int = Field( ..., gt=0,  description= " Quantity ( must be greater than 0)")

class CartItemCreate(CartItemBase):
    pass

class CartItemUpdate(BaseModel):
    product_id: int = Field( ..., description= " Product ID")
    quantity: int = Field( ..., gt=0,  description= " New quantity ( must be greater than 0)")


class CartItem(BaseModel):
    product_id: int 
    name: str =Field(..., description="Product name")
    price: float = Field(..., description="Product price( must be greate than 0)")
    image_url: Optional[str] = Field(None, description="Product image URL")
    quantity: int = Field( ..., gt=0,  description= " Quantity ( must be greater than 0)")
    subtotal: float= Field(...,description="Total price for this item (price * quantity)" )

class CartResponse(BaseModel):
    items: list[CartItem] = Field(..., description= "List of itemsin cart")
    total: float= Field(...,description="Total cart price" )
    items_count: int = Field(..., description="Total number of items in csrt")
