import json
from logic import main_logic


def get_questions() -> dict:
    with open('questions.json') as f:
        questions = json.loads(f.read())
    return questions


def validator(output, begin, end):
    while True:
        try:
            answer: int = int(input(output))
        except ValueError:
            print('\033[33mОщибка ввода. Введите целое число в диапазоне от ', begin, ' до ', end, '\033[0m')
            continue
        if begin <= answer <= end:
            return answer
        else:
            print('\033[33mОщибка ввода. Введите целое число в диапазоне от ', begin, ' до ', end, '\033[0m') 
        

def get_answer(num, answers, question):
    # print('Введите ваш вариант ответа на вопрос: ')
    answer = (validator('\033[33mВведите ваш вариант ответа на вопрос (1-3): \033[0m', 1, 3) ==
              question['correct_answer'])
    resp = validator('\033[33mВведите частоту дыхания (12-30): \033[0m', 12, 30)
    heart_rate = validator('\033[33mВведите частоту сердцебиения (60-100): \033[0m', 60, 100)
    blush = validator('\033[33mВведите вашу степень покраснения (0-6): \033[0m', 0, 6)
    dilation = validator('\033[33mВведите ваш размер зрачков в мм (2-8): \033[0m', 2, 8)
    
    answers.append(dict(id=num, answer=answer, resp=resp, heart_rate=heart_rate, blush=blush, dilation=dilation))


def write_answers(answers):
    with open('answers.json', 'w') as f:
        f.write(json.dumps(answers, indent=2))
        

def start_test():
    answers = []
    questions = get_questions()
    for count, question in enumerate(questions, start=1):
        print("\033[H\033[J")
        print('''\033[32mЭто эмпатический тест Войт-Кампфа, основанный на вопросах и ответных реакциях, может определить
         кто вы: человек или репликант
Всего в тесте 10 вопросов. Твоя реакция так же имеет значение,
поэтому после каждого ответа на вопрос введите реакцию своего организма в терминал: 
    - частота дыхания
    - частота сердцебиения
    - степень твоего покраснения
    - размер зрачков\033[0m''')
        print('\033[34m\nВопрос №', count, ': ',  question['question'], '\033[0m')
        for num, answer in enumerate(question['options'], start=1):
            print(num, ' - ', answer)
        get_answer(count, answers, question)
        write_answers(answers)


def start():
    start_test()
    main_logic()


if __name__ == '__main__':
    start()
