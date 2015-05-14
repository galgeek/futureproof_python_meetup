from pets import Dog


def test_dog():
    rover = Dog(name='Rover', sound='bark', age=3)
    assert rover.name == 'Rover'


def test_dog_call():
    kalb = Dog(name='كلب', sound='هو, هو', age=10)
    assert kalb.come_here() == 'Here, كلب, here!'


def test_dog_age():
    spike = Dog(name='Spike', age=14)
    assert spike.dog_years == 2
