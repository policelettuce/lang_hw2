def recognize(str1):
    state = 1                           #starting state
    for i in range(len(str1)):
        if state == 1 and str1[i] == "a":
            state = 2
        elif state == 1 and str1[i] == "b":
            state = 3
        elif state == 1 and str1[i] == "c":
            state = 4
        elif state == 2 and str1[i] == "b":
            state = 1
        elif state == 3 and str1[i] == "c":
            state = 1
        elif state == 4 and str1[i] == "b":
            state = 5
        else:
            return -1

    if state == 5:
        return 0
    else:
        return -1




if __name__ == '__main__':
    while True:
        print("Введите предложение, или 0, чтобы выйти: ")
        str1 = input()
        if str1 == "0":
            break
        res = recognize(str1)
        if res == 0:
            print("Успех! Предложение принадлежит языку")
        else:
            print("Предложение не принадлежит языку")
