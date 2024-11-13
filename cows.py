from random import randrange

def guess_number():
    number = randrange(1000,9999)
    return number


def check_num(num):
    masiv = [str(i) for i in str(num)]
    for i in range(len(masiv)):
        for j in range(len(masiv)):
            if masiv[i] == masiv[j] and i != j:
                return None
    return masiv

def take_input():
    num = 0
    while num < 1000 or num > 9999:
        num = int(input("Введите число от 1000 до 9999: "))
    masiv = [str(i) for i in str(num)]
    print(masiv)
    return masiv
    
def count_bulls_and_cows(g_sp, u_sp):
    bulls = 0
    cows = 0
    for i in range(len(g_sp)):
        print(g_sp, u_sp)
        if g_sp[i] == u_sp[i]:
            bulls += 1
        for j in range(len(u_sp)):
            if g_sp[i] == u_sp[j] and i != j:
                cows += 1
    mas = [bulls,cows]
    return mas

def main():
    guess_num = check_num(guess_number())
    while guess_num == None:
        guess_num = check_num(guess_number())
        print(guess_num)

    win = False
    while not win:
        user_num = take_input()
        bulls_and_cows = count_bulls_and_cows(guess_num, user_num)
        print(f"Быков: {bulls_and_cows[0]}\n Коров: {bulls_and_cows[1]}")
        if count_bulls_and_cows(guess_num, user_num)[0] == 4:
            win = True
    print("Ты победил!")

main()