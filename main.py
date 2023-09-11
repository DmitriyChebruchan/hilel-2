def parse(url):
    result = {}

    if '?' in url:
        query_string = url.split('?')[1]

        # Split the query string into key-value pairs
        pairs = query_string.split('&')

        for pair in pairs:
            key_value = pair.split('=')
            if len(key_value) == 2:
                key, value = key_value
                # Only include non-empty values
                if value:
                    result[key] = value

    return result


def test_to_parse():
    url = "https://example.com/?param1=value1"
    assert parse(url) == {"param1": "value1"}

    url = "https://example.com/?param1=value1&param2=value2&param3=value3"
    assert parse(url) == {"param1": "value1", "param2": "value2", "param3": "value3"}

    url = "https://example.com/?param1=&param2=value2&param3="
    assert parse(url) == {"param2": "value2"}

    url = "https://example.com/?param1=valueWithSpaces&param2=value-special"
    assert parse(url) == {"param1": "valueWithSpaces", "param2": "value-special"}

    url = "https://example.com/?param1=value1&param1=value2&param1=value3"
    assert parse(url) == {"param1": "value3"}

    url = "https://example.com/"
    assert parse(url) == {}

    url = "https://example.com/?"
    assert parse(url) == {}

    url = "https://example.com/?param1=helloworld"
    assert parse(url) == {"param1": "helloworld"}

    url = "https://example.com/?key1=123&key2=456"
    print(parse(url))
    assert parse(url) == {"key1": "123", "key2": "456"}

    url = "https://example.com/?param1=&param1=value2"
    assert parse(url) == {"param1": "value2"}


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    test_to_parse()


def parse_cookie(query: str) -> dict:
    return {}


if __name__ == '__main__':
    assert parse_cookie('name=Dima;') == {'name': 'Dima'}
    assert parse_cookie('') == {}
    assert parse_cookie('name=Dima;age=28;') == {'name': 'Dima', 'age': '28'}
    assert parse_cookie('name=Dima=User;age=28;') == {'name': 'Dima=User', 'age': '28'}
