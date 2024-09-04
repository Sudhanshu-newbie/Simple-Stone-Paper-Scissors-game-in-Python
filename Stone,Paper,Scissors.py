import random
user=str(input("Enter your name:"))
game=1
point_user=0
point_com=0
while game==1:
    print(user,"choose your move","(Stone,Paper,Scissors)")
    move=str(input())
    option=["stone","paper","scissors"]
    compi=random.choice(option)
    print("computer's choise was",compi)
    if move.lower()=="stone" and compi=="stone":
        print("DRAW")
        print(user,":",point_user,"\n""Computer:",point_com)
    elif move.lower()=="paper" and compi=="paper":
        print("DRAW")
        print(user,":",point_user,"\n""Computer:",point_com)
    elif move.lower()=="scissors" and compi=="scissors":
        print("DRAW")
        print(user,":",point_user,"\n""Computer:",point_com)
    elif move.lower()=="stone" and compi=="paper":
        print("Computer Wins a point")
        point_com +=1
        print(user,":",point_user,"\n""Computer:",point_com)
    elif move.lower()=="stone" and compi=="scissors":
        print(user,"Wins a point")
        point_user +=1
        print(user,":",point_user,"\n""Computer:",point_com)
    elif move.lower()=="paper" and compi=="stone":
        print(user,"Wins a point")
        point_user +=1
        print(user,":",point_user,"\n""Computer:",point_com)
    elif move.lower()=="paper" and compi=="scissors":
        print("Computer Wins a point")
        point_com +=1
        print(user,":",point_user,"\n""Computer:",point_com)
    elif move.lower()=="scissors" and compi=="stone":
        print("Computer Wins a point")
        point_com +=1
        print(user,":",point_user,"\n""Computer:",point_com)
    elif move.lower()=="scissors" and compi=="paper":
        print(user,"Wins a point")
        point_user +=1
        print(user,":",point_user,"\n""Computer:",point_com)
    else:
        print ("invalid input")
    print ("if you want to stop playing type END else press enter to continue playing")
    state=str(input())
    if state.lower()=="end":
        game=0
    else:
        pass
print(user,"got",point_user,"points","\n","Computer got",point_com,"points")
if point_user==point_com:
    print("It's a DRAW")
elif point_user>point_com:
    print(user,"WON")
elif point_user<point_com:
    print("Computer WON")    
else:
    pass