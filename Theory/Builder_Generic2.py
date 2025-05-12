from abc import ABC,abstractmethod
from typing import Any

#Define the product
class Product():
    def __init__(self):
        self.parts=[]

    def add(self,part:Any):
        self.parts.append(part)

    def list_parts(self):
        print(self.parts)

#Define the interface from the builder
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

    @abstractmethod
    def build_part_C():
        pass

class concret_builder(Builder):

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
        self._product.add("Part_A")

    def build_part_B(self):
        self._product.add("Part_B")

    def build_part_C(self):
        self._product.add("Part_C")        

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
        self._builder.build_part_A()

    def maximal_viable_product(self):
        self._builder.build_part_A()
        self._builder.build_part_B()
        self._builder.build_part_C()

if __name__ == "__main__":
    builder_one=concret_builder()
    Director_one=Director()
    Director_one.builder=builder_one

    Director_one.maximal_viable_product()
    builder_one.product.list_parts()