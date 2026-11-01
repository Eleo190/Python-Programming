#PROBLEM 1
from testif import testif
class NVector:
    def __init__(self, *args):
        """Initialize an NVector with vectors elements in an internal list"""
        if len(args) == 1:
            self._elements = list(args[0])
        else: self._elements = list(args)

    def __len__(self) -> int:
        """Returns dimension (length of list) as an int"""
        return len(self._elements)

    def __getitem__(self, key:int) -> int:
        """Returns element at _elements[key]
        Precondition: key must correspond to a valid index in the _elements list"""
        return self._elements[key]
    def __setitem__(self, key:int, value) :
        """Updates the element at [key] to value
        Precondition: key must correspond to a valid index in the _elements list"""
        self._elements[key] = value
    def __str__(self) -> str:
        """Returns the vector in string format"""
        return(str(self._elements))

    def __eq__(self, other) -> bool:
        """Returns True if all elements of both self and other contain lists with equal elements, False otherwise"""
        if isinstance(other, NVector):
            return self._elements == other._elements
        else: return False
    def __ne__(self, other) -> bool:
        """Returns True if all self and other do not contain identical _elements lists, False if they are equal"""
        return not self.__eq__(other)

    def __add__(self, other) -> NVector:
        """Returns a new NVector containing either the lists of self and other added element-wise if other is an NVector, or
        if other is an int or float, the the elements of self._elements added with float
        Precondition: if other is an NVector, len(self) == len(other)"""
        #Checking for case of adding two NVectors
        if isinstance(other, NVector):
            if len(self) == len(other):
                result = [self[i] + other[i] for i in range(len(self))]
                return NVector(result)
            else: raise ValueError("NVectors must be of same dimensions to add!")
        elif isinstance(other, (int, float)):
            result = [x + other for x in self._elements]
            return NVector(result)
        else: return NotImplemented

    def __radd__(self, other) -> NVector:
        """Calls __add__ with operands reversed"""
        return self.__add__(other)

    def __mul__(self, other) -> int | float:
        """Returns a sum of dot product if other is an NVector, or if other is an int or float, sum of scalar multiplication
            Precondition: if other is an NVector, len(self) == len(other)"""
        #checking case of NVector or single number
        if isinstance(other, NVector):
            if len(self) == len(other):
                result = [self[i] *other[i] for i in range(len(self))]
                return sum(result)
            else: raise ValueError("NVectors must be of same dimensions to multiply!")
        elif isinstance(other, (int, float)):
            result = [self[i]*other for i in range(len(self))]
            return sum(result)
        else: return NotImplemented

    def __rmul__(self, other) -> int | float:
        """Calls __mul__ with operands reversed"""     
        return self.__mul__(other)

    @classmethod
    def zeros(cls, n: int) -> NVector:
        """Returns an NVector containing a list of length n with only 0's
        Precondition: n>=0"""
        return cls([0]*n)

def main():
    #Testing A, B
    v1=NVector([1,2,3,4])
    v2=NVector(1, 2, 3, 4)
    testif(isinstance(v1, NVector), "Part a", "List creation works", "List creation failed")
    testif(isinstance(v2, NVector), "Part b", "split creation works", "split creation failed")
    #Test C
    testif(len(v1)==4, "part c", "len works", "len failed")
    #Test D
    testif(v1[0]==1, "part d", "getitem works", "getitem failed")
    #Test E
    v1[1] = 10
    testif(v1[1]==10, "part e", "setitem works", "setitem failed")
    v1[1] = 2
    #Test F
    testif(str(v1)=="[1, 2, 3, 4]", "part F", "str works", "str failed")
    #Test G
    v3=NVector(0,0,0,0)
    testif(v1 == v2, "part G", "eq works", "eq failed")
    testif(v1!=v3, "part G", "ne works", "ne failed")
    #Test H
    added = v1 + v2
    testif(str(added)=='[2, 4, 6, 8]', "part g", "vector add works", "vector add failed")
    added = v1 + 1
    testif(str(added)=='[2, 3, 4, 5]', "part g", "scalar add works", "scalar add failed")
    added = 1 + v1
    testif(str(added)=='[2, 3, 4, 5]', "part g", "reflected add works", "reflected add failed")
    #Test I
    testif(v1*v2 == 30, "part I", "vector mult works", "vector mult failed")
    testif(v1*2 == 20, "part I", "scalar mult works", "scalar mult failed")
    testif(2*v1 == 20, "part I", "reflected mult works", "reflected mult failed")
if __name__ == "__main__":
    main()
