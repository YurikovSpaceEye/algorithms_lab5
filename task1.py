def validate_input(text:str):
    data = []
    for char in text:
        if char == " ":
            continue
        elif char in ["(",")"]:
            if char == "(":
                data.append(1)
            else:
                data.append(-1)
        else:
            return None, False

    return data, True

def get_input():
    while True:
        text = input("Напишите скобочное выражение для проверки(например \"(()()))\"):\n")
        data, is_valid = validate_input(text)

        if not is_valid:
            continue

        return data, text

def validate_expression(data:list):
    state = 0
    for i, item in enumerate(data):
        state += item
        if state < 0:
            return False, i+1, 0

    if state != 0:
        return False, len(data), state
    return True, -1, 0

def program():
    data, text = get_input()
    is_valid, pos, state = validate_expression(data)

    if is_valid:
        print("Скобочная структура правильная")
    else:
        print("Скобочная структура не правильная.", end="")
        if state <= 0:
            print(f" Позиция символа нарушающего правильность: {pos}")
        else:
            print(f" Не закрыто скобок: {state}")

program()