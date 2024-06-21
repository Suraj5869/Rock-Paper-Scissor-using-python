import random
    
def computermove():
    b = random.randint(1, 3)
    return b
    
print("\n___Rock Paper Scissor___\n")
print('You have to choose the move from:\n1. Rock\n2. Paper\n3. Scissor\n')
x, y = 0, 0
print(f'Player = {0} vs Computer = {0}')

for i in range (1,10):

    a = input("\nEnter your move: ")
    
    if a == 'Rock' or a == 'rock':
        c = 1
    if a == 'Paper' or a == 'paper':
        c = 2
    if a == 'Scissor' or a == 'scissor':
        c = 3
        
    d = computermove()
    if d == 1:
        print('Computer chooses Rock\n')
    elif d == 2:
        print('Computer chooses Paper\n')
    else:
        print('Computer chooses Scissor\n')

    if (c == 1 and d == 2) or (c == 2 and d == 3) or (c == 3 and d == 1):
        print('Computer win the round', i)
        y = y+1
    if (c == 1 and d == 3) or (c == 2 and d == 1) or (c == 3 and d == 2):
        print('Player win the round', i)
        x = x+1
    if (c == d):
        print(f"Round {i} Draw")
    
    print ('Player = ', x)
    print('Computer =', y)

        
if x > y :
    print('Player win the match.')
elif x < y:
    print('Computer win the match.')
else:
    print("Match draw")