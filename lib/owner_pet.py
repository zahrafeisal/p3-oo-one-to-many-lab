class Pet:

    PET_TYPES = [
        'dog',
        'cat',
        'rodent',
        'bird',
        'reptile',
        'exotic'
    ]

    all = []

    def __init__(self, name, pet_type, owner = None):
        self.name = name
        self.owner = owner
        self.pet_type = pet_type
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type in Pet.PET_TYPES:
            self._pet_type = pet_type
        else:
            raise ValueError(f'{pet_type} is not a valid pet type.')

    pass

class Owner:

    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
        pass

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise TypeError(f'{pet} is not as instance of Pet')

    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets
        pass
    
    pass