import random
stages=['''
 |  |
 O  |
/|\ |
/ \ |
        
===================
''',
'''
 |  |
 O  |
/|\ |
/   |

===================
''',
'''
 |  |
 O  |
/|\ |
    | 

===================
''',
'''
 |  |
 O  |
/|  |
    | 

===================
''',
'''
 |  |
 O  |
/   |
    |

===================
''',
'''
 |  |
 O  |
    |
    |

===================
''',
'''
 |  |
    |
    |
    |

===================
''']
words=["orange","apple","banana","ball","biscuit","vollyball","football","certificate"]
word=random.choice(words)
output=[]
for i in range(len(word)):
    output+='_'
life=6
print("Hi! Welcome to Hangman Game")
print("\nHere go! Try to guess the word?")
print()
print(output)
print("\nThe word contains",len(word),"letters")
print("\nIn The Begining you have 6 life try to guess without losing life")
dead=False
while(dead==False):
    letter=input("\n\nEnter the guessing letter? ")
    for pos in range(len(word)):
        ch=word[pos]
        if(ch==letter):
            output[pos]=ch
    if letter not in word:
        life-=1
    print()
    print(output)
    print(stages[life])
    print("\nThe remaing life = ",life)
    print()
    if(life==0):
        dead=True
    if '_' not in output:
        dead=True
        print ("\n\nHurray ! You won")
        print ("\nThe correct word is",'"',word,'"')

