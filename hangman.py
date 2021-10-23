import random
score=10
tries=0
encrypted=''
list=["saaho","dilwale","thor","dangal","housefull4"]
word=random.choice(list)
n=len(word)
for i in range(n):
 encrypted=encrypted+"*"
print(encrypted,end="")
while score>0:
    guess=input("user input section")
    if(len(guess)==1 and guess in word):
      times=word.count(guess)
      score=score+(2*times)
      print(score)
      for j in range(n):
       if word[j] in guess:
        encrypted=encrypted[:j]+guess+encrypted[j+1:]
        print(encrypted)
        
    elif(len(guess)==1 and guess not in word):
        score-=3
        print(score)
        print("sorry Letter is Not Present")
    elif(len(guess)==n and guess in word):
        score=20
        print("jackpot",str(score))
    else:
        print("tu jaa ree")
