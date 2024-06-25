from polydrome import solve


def test_palindromes():
    phrases = [
        "нажал кабан на баклажан",
        "дом как комод",
        "рвал дед лавр",
        "азот калий и лактоза",
        "а собака боса",
        "тонет енот",
        "карман мрак",
        "пуст суп"
    ]
    expected_result = [
        "нажал кабан на баклажан",
        "рвал дед лавр",
        "азот калий и лактоза",
        "а собака боса",
        "тонет енот",
        "пуст суп"
    ]
    result = solve(phrases)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"


def test_no_palindromes():
    phrases = [
        "это не палиндром",
        "и это тоже не",
        "еще одно предложение без палиндромов"
    ]
    expected_result = []
    result = solve(phrases)
    assert result == expected_result, f"Expected {expected_result}, but got {result}"
