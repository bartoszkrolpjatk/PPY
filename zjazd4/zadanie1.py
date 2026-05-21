from random import choice

def get_user_input():
    def validate_input(to_validate):
        if to_validate != 'r' and to_validate != 's' and to_validate != 'p':
            raise ValueError("Invalid input")

    while True:
        try:
            res = input("Your move ([r]ock, [p]aper, [s]cissors) -> ")
            validate_input(res)
            break
        except ValueError:
            print("*** Enter \"r\" or \"p\" or \"s\". Try again...")
    return res

def generate_comp_choice():
    choices = ['r', 'p', 's']
    return choice(choices)

#rock > scissors > paper
# ^__________________|

ROUNDS = 5
TRANSLATE = dict(r='rock', s='scissors', p='paper')
GAME_RULES = {'r': 's', 's': 'p', 'p': 'r'} #key beats value

score = dict(user=0, comp=0, draw=0)
history = []

for _ in range(5):
    user = get_user_input()
    comp = generate_comp_choice()

    score_to_increment = 'user' if GAME_RULES[user] == comp else 'comp'
    if user == comp:
        score_to_increment = 'draw'
    score[score_to_increment] += 1

    c_tran = TRANSLATE[comp]
    u_tran = TRANSLATE[user]
    print(f"{u_tran} {c_tran}: winner: {score_to_increment}")

    history.append((u_tran, c_tran, score_to_increment))

print("SUMMARY")
print(f"{'user':<10}{'comp':<10}{'winner':<10}")
print("-" * 25)
for user_choice, comp_choice, winner in history:
    print(f"{user_choice:<10}{comp_choice:<10}{winner:<10}", end="")
    print()
print(f"The user won {score['user']} games, the computer {score['comp']}, and there was {score['draw']} draws")

