from abc import ABC, abstractmethod
from typing import Any

#First we need to define de product, becouse is the base, in this case, is a 
#generic product

class Product():
    
    def __init__(self) -> None:
        self.parts=[]

    def add(self,part:Any) -> None:
        self.parts.append(part)
    
    def list_parts(self) -> None:
        print(self.parts)


#Define the interface for the builder

class Builder(ABC):
    
    @property
    @abstractmethod
    def product():
        pass

    @abstractmethod
    def product_part_A():
        pass

    @abstractmethod
    def product_part_B():
        pass

    @abstractmethod
    def product_part_C():
        pass

#Implement the interface
class Concret_builder_one(Builder):

    def __init__(self):
        self.reset()

    def reset(self):
        self._product=Product()

    @property
    def product(self):
        product=self._product
        self.reset()
        return product
    
    def product_part_A(self):
        self._product.add("Product_A")

    def product_part_B(self):
        self._product.add("Product_B")

    def product_part_C(self):
        self._product.add("Product_C")

class Director():
    def __init__(self):
        self._builder=None
    
    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self,builder:Builder):
        self._builder=builder

    def minimal_viable_product(self):
        self._builder.product_part_A()

    def maximal_viable_product(self):
        self._builder.product_part_B
        self._builder.product_part_A
        self._builder.product_part_C
        
if __name__ == "__main__":

    builer_one=Concret_builder_one()
    Director_one=Director()
    Director_one.builder=builer_one
    Director_one.minimal_viable_product()
    builer_one.product.list_parts()
    
    