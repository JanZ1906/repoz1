text_1 = input("Podaj tekst 1: ")
text_2 = input("Podaj tekst 2: ")

is_valid = True

if len(text_1) == len(text_2):

    tmp_dict = {}

    for i in text_1:
        if i in tmp_dict:
            tmp_dict[i] = tmp_dict[i] + 1
        else:
            tmp_dict[i] = 1

    for j in text_2:
        if (j not in tmp_dict) or (tmp_dict[j] <= 0):
            is_valid = False
            break
else:
    is_valid = False

if is_valid:
    print("Teksty są anagramami.")
else:
    print("Teksty nie są anagramami.")
