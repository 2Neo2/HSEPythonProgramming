# Task 1.
input_word = input()

letters_count = len(input_word)

if letters_count % 2 == 0:
    middle_letters = input_word[letters_count // 2 - 1:letters_count // 2 + 1]
else:
    middle_letters = input_word[letters_count // 2]

print(middle_letters)

#==============================
# Task 2.

boys = input("Введите имена юношей через запятую: ").split(",")
girls = input("Введите имена девушек через запятую: ").split(",")

boys = [boy.strip() for boy in boys]
girls = [girl.strip() for girl in girls]

if len(boys) != len(girls):
    print("Внимание, кто-то может остаться без пары!")
else:
    boys_sorted = sorted(boys)
    girls_sorted = sorted(girls)
    
    print("Идеальные пары:")
    for boy, girl in zip(boys_sorted, girls_sorted):
        print(f"{boy} и {girl}")
