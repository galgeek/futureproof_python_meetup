from pets import Dog

rover = Dog(name='Rover', sound='bark', age=3)
chinese = Dog(name='Chow', sound='汪汪', age=10)

def test_dog():
    assert rover.name == 'Rover'


def test_dog_call():
    assert kalb.come_here() == 'Here, كلب, here!'


def test_dog_age():
    assert spike.dog_years == 2
