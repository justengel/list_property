def test_namedlist():
    import list_property

    Person = list_property.namedlist('Person', 'first_name last_name middle_initial', {'middle_initial': '!'})

    p = Person('Hello', 'World')
    assert p.first_name == 'Hello'
    assert p[0] == 'Hello'
    assert p.last_name == 'World'
    assert p[1] == 'World'
    assert p.middle_initial == '!'
    assert p[2] == '!'
    assert isinstance(p, list)
    assert isinstance(p, list_property.NamedList)

    assert list(p) == ['Hello', 'World', '!']


def test_namedlist_import():
    from list_property import namedlist, NamedList

    Person = namedlist('Person', 'first_name last_name middle_initial', {'middle_initial': '!'})

    p = Person('Hello', 'World')
    assert p.first_name == 'Hello'
    assert p[0] == 'Hello'
    assert p.last_name == 'World'
    assert p[1] == 'World'
    assert p.middle_initial == '!'
    assert p[2] == '!'
    assert isinstance(p, list)
    assert isinstance(p, NamedList)

    assert list(p) == ['Hello', 'World', '!']


def test_namedlist_class():
    import list_property

    class Person(list_property.NamedList):
        first_name = list_property(0)
        last_name = list_property(1)
        middle_initial = list_property(2, '!')

    p = Person('Hello', 'World')
    assert p.first_name == 'Hello'
    assert p[0] == 'Hello'
    assert p.last_name == 'World'
    assert p[1] == 'World'
    assert p.middle_initial == '!'
    assert p[2] == '!'
    assert isinstance(p, list)
    assert isinstance(p, list_property.NamedList)


if __name__ == '__main__':
    test_namedlist()
    test_namedlist_import()
    test_namedlist_class()
    print("All tests finished successfully!")
