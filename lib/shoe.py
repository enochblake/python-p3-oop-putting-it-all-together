class Shoe:
    def __init__(self,brand,size) -> None:
        self.brand= brand
        self.size = size
        self.condition = None

    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self,brand):
        self._brand = brand

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,size):
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'

stan_smith = Shoe("Adidas", 9)
print(f'Condition before repair: {stan_smith.condition}')
stan_smith.cobble()
print(f'Condition after repair: {stan_smith.condition}')