def parse(url):
    result = {}

    if "?" in url:
        query_string = url.split("?")[1]

        # Split the query string into key-value pairs
        pairs = query_string.split("&")

        for pair in pairs:
            key_value = pair.split("=")
            if len(key_value) == 2:
                key, value = key_value
                # Only include non-empty values
                if value:
                    result[key] = value

    return result


# tests of student
def test_to_parse():
    # Test number 1
    url = "https://example.com/?param1=value1"
    assert parse(url) == {"param1": "value1"}

    # Test number 2
    url = "https://example.com/?param1=value1&param2=value2&param3=value3"
    assert parse(url) == {"param1": "value1", "param2": "value2", "param3": "value3"}

    # Test number 3
    url = "https://example.com/?param1=&param2=value2&param3="
    assert parse(url) == {"param2": "value2"}

    # Test number 4
    url = "https://example.com/?param1=valueWithSpaces&param2=value-special"
    assert parse(url) == {"param1": "valueWithSpaces", "param2": "value-special"}

    # Test number 5
    url = "https://example.com/?param1=value1&param1=value2&param1=value3"
    assert parse(url) == {"param1": "value3"}

    # Test number 6
    url = "https://example.com/"
    assert parse(url) == {}

    # Test number 7
    url = "https://example.com/?"
    assert parse(url) == {}

    # Test number 8
    url = "https://example.com/?param1=helloworld"
    assert parse(url) == {"param1": "helloworld"}

    # Test number 9
    url = "https://example.com/?key1=123&key2=456"
    assert parse(url) == {"key1": "123", "key2": "456"}

    # Test number 10
    url = "https://example.com/?param1=&param1=value2"
    assert parse(url) == {"param1": "value2"}


if __name__ == "__main__":
    assert parse("https://example.com/path/to/page?name=ferret&color=purple") == {
        "name": "ferret",
        "color": "purple",
    }
    assert parse("https://example.com/path/to/page?name=ferret&color=purple&") == {
        "name": "ferret",
        "color": "purple",
    }
    assert parse("http://example.com/") == {}
    assert parse("http://example.com/?") == {}
    assert parse("http://example.com/?name=Dima") == {"name": "Dima"}

    # function with tests of student
    test_to_parse()


def parse_cookie(query: str) -> dict:
    result = {}

    if query:
        list_of_pairs = query.split(";")

        for pair in list_of_pairs:
            # Split the query string into key-value pairs
            key_value = pair.split("=")
            if len(key_value) == 2:
                key, value = key_value
                result[key] = value
            elif len(key_value) == 1:
                pass
            else:
                key = key_value[0]
                value = "=".join(key_value[1:])
                result[key] = value

    return result


def test_to_parse_cookie():
    if __name__ == "__main__":
        # Test number 1
        assert parse_cookie("color=red;") == {"color": "red"}

        # Test number 2
        assert parse_cookie(" name = Oleg ; age = 30 ; ") == {
            "name": "Oleg",
            "age": "30",
        }

        # Test number 3
        assert parse_cookie("fruit=apple;price=10;") == {
            "fruit": "apple",
            "price": "10",
        }

        # Test number 4
        assert parse_cookie("x=1;y=2;") == {"x": "1", "y": "2"}

        # Test number 5
        assert parse_cookie("name=John;city=;note=Bold=man;") == {
            "name": "John",
            "note": "Some=text",
        }

        # Test number 6
        assert parse_cookie("item=apple;quantity=2;") == {
            "item": "apple",
            "quantity": "2",
        }

        # Test number 7
        assert parse_cookie("name=Bob") == {"name": "Bob"}

        # Test number 8
        assert parse_cookie("name%20with%20space=John%20Doe;age%2B=30;") == {
            "name with space": "John Doe",
            "age+": "30",
        }

        # Test number 9
        assert parse_cookie("set-up=?=punch-line=ПотомуЧтоЯНеВлюблен") == {
            "set-up": "ПочемуУМеняВЖивотеГусениццв?",
            "punch-line": "ПотомуЧтоЯНеВлюблен",
        }

        # Test number 10
        assert parse_cookie(
            "set-up=ПочемуУМеняВЖивотеГусениццв?=punch-line=ПотомуЧтоЯНеВлюблен"
        ) == {
            "set-up": "ПочемуУМеняВЖивотеГусениццв?",
            "punch-line": "ПотомуЧтоЯНеВлюблен",
        }


if __name__ == "__main__":
    assert parse_cookie("name=Dima;") == {"name": "Dima"}
    assert parse_cookie("") == {}
    assert parse_cookie("name=Dima;age=28;") == {"name": "Dima", "age": "28"}
    assert parse_cookie("name=Dima=User;age=28;") == {"name": "Dima=User", "age": "28"}
