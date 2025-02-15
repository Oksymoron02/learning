filename = 'odpowiedzi_z_ankiety.txt'

with open(filename, 'a', encoding='utf-8') as answers:
    print("Aby przerwać odpowiadanie wpisz 'q'.")
    while True:
        answer = input("Dlaczego lubisz programowanie? ")
        if answer == 'q':
            break
        else:
            answers.write(answer + "\n")