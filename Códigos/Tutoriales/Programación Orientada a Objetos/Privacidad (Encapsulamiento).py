"""
Hacer la explicación sobre los dobles guines bajos y los guines simples. Se puede basarse en el páarafo de propiedaddes
"""

class year_graduated:
   def __init__(self, year=32):
      self._year = year

   # make the getter method
   def get_year(self):
      return self.__year

# make the setter method
def set_year(self, a):
    self.__year = a

grad_obj = year_graduated()
print(grad_obj._year)

# Before using setter
print(grad_obj.get_year())
#
# # After using setter
grad_obj.set_year(2019)
print(grad_obj._year)