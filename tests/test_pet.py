from pets import Dog

english = Dog(name='Rover', sound='bark', age=3)
chinese = Dog(name='穗', sound='汪汪', age=10)


def test_dog():
    assert english.name == 'Rover'
    assert chinese.sound == '汪汪'


def test_dog_call():
    assert chinese.come_here() == 'Here, 穗, here!'


def test_dog_age():
    assert chinese.dog_years >= 1.42


def test_dog_string():
    assert str(chinese) == chinese.name


def test_print_name(capsys):
    print('Name', chinese.name)
    out, err = capsys.readouterr()
    assert out == 'Name {}\n'.format(chinese.name)
