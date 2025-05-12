from abc import ABC, abstractmethod
from typing import Any

class Product():
    def __init__(self):
        self.parts=[]

    def add(self,part:Any):
        self.parts.append(part)
    
    def list_parts(self):
        print(self.parts)

#This is the interface
class Builder(ABC):

    @property
    @abstractmethod
    def product():
        pass

    @abstractmethod
    def build_part_A():
        pass
    
    @abstractmethod
    def build_part_B():
        pass

class concreteBuilder(Builder):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self._product=Product()
    
    @property
    def product(self):
        product=self._product
        self.reset()
        return product

    def build_part_A(self):
        self._product.add('Product A')

    def build_part_B(self):
        self._product.add('Product B')
    
class Director:
    def __init__(self):
        self._builder = None

    @property
    def builder(self):
        return self._builder
    
    @builder.setter
    def builder(self,builder:Builder):
        self._builder=builder
    
    def minimal_viable_product(self):
        self._builder.build_part_A()

    def maximal_viable_product(self):
        self._builder.build_part_A()
        self._builder.build_part_B()

if __name__ == "__main__":
    builder_one = concreteBuilder()
    director_operative = Director()
    director_operative.builder=builder_one
    director_operative.maximal_viable_product()
    builder_one.product.list_parts()
    
    
