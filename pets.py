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


class Dog(Pet):
    def __init__(self, name=None, sound=None, age=None):
        sound = sound or 'woof'
        super().__init__(name, sound)
        self.age = age

    @property
    def dog_years(self):
        return self.age / 7
