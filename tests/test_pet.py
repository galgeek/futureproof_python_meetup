from pets import Dog, Household

english = Dog(name='Rover', sound='bark', age=3)
chinese = Dog(name='穗', sound='汪汪', age=10)
hh = Household(english, chinese)


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


def test_household_contains():
    assert english in hh


def test_household_iterable():
    names = []
    for pet in hh:
        names.append(str(pet))
    assert len(names) == 2


def test_household_index():
    assert chinese == hh[-1]
