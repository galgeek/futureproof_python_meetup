class Pet:
    def __init__(self, name=None, sound=None):
        super().__init__()
        self.name = name
        self.sound = sound

    def speak(self):
        return '{}!'.format(self.sound.upper())

    def come_here(self):
        return 'Here, {}, here!'.format(self.name)

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return other.name == self.name and other.sound == self.sound


class Dog(Pet):
    def __init__(self, name=None, sound=None, age=None):
        sound = sound or 'woof'
        super().__init__(name, sound)
        self.age = age

    @property
    def dog_years(self):
        return self.age / 7

    def __eq__(self, other):
        eq = super().__eq__(other)
        return eq and other.age == self.age


class Household:
    def __init__(self, *args):
        self.members = []
        if args:
            self.members.extend(args)

    def add_pet(self, pet):
        self.members.append(pet)

    def __iter__(self):
        for pet in self.members:
            yield pet

    def __contains__(self, pet):
        return pet in self.members

    def __getitem__(self, index):
        try:
            return self.members[index]
        except IndexError, e:
            raise e
