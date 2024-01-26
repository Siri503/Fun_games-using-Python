import random
stages = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    ''',
    '''
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    '''
]

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
print(logo)
stages.reverse()
word=["dhanush","sanjay","siri","yasaswini","chandrika","priyanka","sarojini","laxmi_varhan","jaswanth","harshita"]
cho=random.choice(word)
print(cho)
k=6
li=[]
for i in range(len(cho)):
    li.append('_')
while '_' in li and k>0:
    guess=input("enter the letter:")
    # print(list)s
    for i in range(len(cho)):
        if guess==cho[i]:
            li[i]=guess
    if guess not in cho:
        k-=1
        print(stages[k])
    else:
        print(li)
    
if '_' not in li:
    print("You won")
else:
    print("Lose")
