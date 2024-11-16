import json
import pandas as pd


def main_logic():
    with open('answers.json') as f:
        answers = json.loads(f.read())
    value_correct_answers = 0
    for i in answers:
        if i['answer']:
            value_correct_answers += 1
    df_answers = pd.DataFrame(answers)
    print('\n\033[33mВаши ответы:')
    print(df_answers)
    mean_answer = df_answers.mean().to_dict()
    if mean_answer['answer'] > 0.5:
        status = "\033[32m\nПоздравляю!!! ты человек\033[0m\n"
    else:
        if mean_answer['resp'] > 20 or mean_answer['heart_rate'] > 80 or mean_answer['blush'] > 3 or mean_answer['dilation'] > 5:
            status = "\033[32m\nПоздравляю!!! ты человек\033[0m\n"
        else:
            status = "Похоже что ты андроид..."
            
    print(status)


if __name__ == '__main__':
    main_logic()
