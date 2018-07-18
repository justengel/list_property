

def test_function():
    from list_property import list_property

    class Person(list):
        first_name = list_property(0)
        last_name = list_property(1)
        middle_initial = list_property(2, '')

    p = Person(("John", "Smith"))
    assert p == ["John", "Smith"]

    assert p.first_name == 'John'
    assert p[0] == 'John'
    assert p.last_name == 'Smith'
    assert p[1] == 'Smith'
    assert p.middle_initial == ''
    try:
        assert p[2] == ''
        raise AssertionError('Index 2 was not set and there should be an IndexError!')
    except IndexError:
        pass  # Success

    p.first_name = "Hello"
    p.last_name = 'World!'
    p.middle_initial = 'T'
    assert p.first_name == 'Hello'
    assert p[0] == 'Hello'
    assert p.last_name == 'World!'
    assert p[1] == 'World!'
    assert p.middle_initial == 'T'
    assert p[2] == 'T'  # Note: p[2] is now set


def test_module():
    import list_property

    class Person(list):
        first_name = list_property(0)
        last_name = list_property(1)
        middle_initial = list_property(2, '')

    p = Person(("John", "Smith"))
    assert p == ["John", "Smith"]

    assert p.first_name == 'John'
    assert p[0] == 'John'
    assert p.last_name == 'Smith'
    assert p[1] == 'Smith'
    assert p.middle_initial == ''
    try:
        assert p[2] == ''
        raise AssertionError('Index 2 was not set and there should be an IndexError!')
    except IndexError:
        pass  # Success


def test_module_attribute():
    import list_property

    class Person(list):
        first_name = list_property.list_property(0)
        last_name = list_property.list_property(1)
        middle_initial = list_property.list_property(2, '')

    p = Person(("John", "Smith"))
    assert p == ["John", "Smith"]

    assert p.first_name == 'John'
    assert p[0] == 'John'
    assert p.last_name == 'Smith'
    assert p[1] == 'Smith'
    assert p.middle_initial == ''
    try:
        assert p[2] == ''
        raise AssertionError('Index 2 was not set and there should be an IndexError!')
    except IndexError:
        pass  # Success


def test_custom_error():
    import list_property

    class Person(list):
        first_name = list_property(0)
        last_name = list_property(1)
        middle_initial = list_property(2, OverflowError("This is an error"))

    p = Person(('Hello', 'World'))

    try:
        p.middle_initial
        raise AssertionError
    except OverflowError:
        pass # Success


if __name__ == '__main__':
    test_function()
    test_module()
    test_module_attribute()
    test_custom_error()

    print("All tests passed successfully!")
