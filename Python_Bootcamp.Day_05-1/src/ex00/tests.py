import requests


def test() -> None:

    response = requests.get('http://localhost:8888/?species=Cyberman')
    print('Link: http://localhost:8888/?species=Cyberman')
    print('HTTP Header: ')
    print(response.headers)
    print(f'Content: {response.content.decode()}')
    print('----------------------------')
    print()
    assert response.content == b'{"credentials": "John Lumic"}'

    response = requests.get('http://localhost:8888/?species=Judoon')
    print('Link: http://localhost:8888/?species=Judoon')
    print('HTTP Header: ')
    print(response.headers)
    print(f'Status code: {response.status_code}')
    print(f'Content: {response.content.decode()}')
    print('----------------------------')
    print()
    assert response.status_code == 200
    assert response.content == \
        b'{"credentials": "Shadow Proclamation Convention 15 Enforcer"}'

    response = requests.get('http://localhost:8888/?species=Some')
    print('Link: http://localhost:8888/?species=Some')
    print('HTTP Header: ')
    print(response.headers)
    print(f'Status code: {response.status_code}')
    print(f'Content: {response.content.decode()}')
    print('----------------------------')
    print()
    assert response.status_code == 404
    assert response.content == b'{"credentials": "Unknown"}'

    response = requests.get('http://localhost:8888')
    print('Link: http://localhost:8888')
    print('HTTP Header: ')
    print(response.headers)
    print(f'Status code: {response.status_code}')
    print(f'Content: {response.content.decode()}')
    print('----------------------------')
    print()
    assert response.status_code == 404
    assert response.content == b'{"credentials": "Unknown"}'

    print('\033[32mТЕСТЫ ПРОЙДЕНЫ УСПЕШНО!\033[0m')


if __name__ == '__main__':
    test()
