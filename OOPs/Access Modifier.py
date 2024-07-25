# public modifier
"""
class ABC:
    def __init__(self):
        self.public_attribute = None  # this is a public attribute

    def public_function(self):  # this is a public function
        pass


obj1 = ABC()
obj1.public_attribute = 23
obj1.public_function()
print(obj1.public_attribute)
"""



# private modifier ( uses double underscore '__' )
'''
class ABC:
    def __init__(self):
        self.__private_attribute = 10  # this is a private attribute( starting with __ )

    def __private_function(self):  # this is a private function
        pass


obj1 = ABC()
# obj1.__private_function()           # will throw AttributeError
# print(obj1.__private_attribute)     # will throw AttributeError
print(obj1._ABC__private_attribute)   # internally private attribute is stored like this.
print(obj1.__dict__)
'''

# protected modifier ( uses single underscore '_' )
'''
class ABC:
    def __init__(self):
        self._protected_attribute = 10  # this is a protected attribute( starting with __ )

    def _protected_function(self):  # this is a protected function
        pass


class XYZ 
'''