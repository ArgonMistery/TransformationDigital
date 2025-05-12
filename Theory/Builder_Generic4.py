from abc import ABC, abstractmethod
from typing import Any

#Define the base of the product.
#In this case I create a product, for aggregation

class Product():
    def __init__(self):
        self.parts=[]
    
    def add(self,part:Any):
        self.parts.append(part)

    def list_parts(self):
        print(self.parts)

#Now we need to create a builder_(Interface from this design pattern)
class Builder(ABC):
    
    @property
    @abstractmethod
    def product():
        pass

    @abstractmethod
    def build_part_a():
        pass

    @abstractmethod
    def build_part_b():
        pass

    @abstractmethod
    def build_part_c():
        pass

#Now we need to define a concrete builder
class Concrete_Builder(Builder):
    
    def __init__(self):
        #This method is a tipic for define the action than create and clean the class
        self.reset()
    
    def reset(self):
        self._product=Product()
        
    @property
    def product(self):
        product=self._product
        self.reset()
        return product
    
   
    def build_part_a(self):
        self._product.add("Part_A")

  
    def build_part_b(self):
        self._product.add("Part_B")

    
    def build_part_c(self):
        self._product.add("Part_C")


#Now we need to create a class for direct the actions and the step of the construction

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
        self._builder.build_part_a()
    
    def maximal_viable_product(self):
        self._builder.build_part_a()
        self._builder.build_part_b()
        self._builder.build_part_c()


if __name__ == "__main__":
    
    #Instance the director than I create in the last class
    Main_Director=Director()
    #Instance the builder than I create in the last class
    Main_builder=Concrete_Builder()

    #Define the builder to the Directo class
    Main_Director.builder=Main_builder


    #Define the kind of action than need to create
    Main_Director.maximal_viable_product()
    Main_builder.product.list_parts()
    Main_Director.minimal_viable_product()
    Main_builder.product.list_parts()