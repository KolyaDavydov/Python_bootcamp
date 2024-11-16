import json
import os


def test_files():
    assert os.path.isfile('../questions.json')
    assert os.path.isfile('../answers.json')


def test_answers():
    with open('../answers.json') as f:
        answers = json.loads(f.read())
    for answer in answers:
        assert answer['resp'] in range(12, 31)
        assert answer['heart_rate'] in range(60, 101)
        assert answer['blush'] in range(0, 7)
        assert answer['dilation'] in range(2, 9)
