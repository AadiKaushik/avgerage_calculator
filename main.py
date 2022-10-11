
#m1= int(input('Enter the marks obtained :-  '))
#m2= int(input('Enter the marks obtained :-  '))
#m3= int(input('Enter the marks obtained :-  '))
#m4= int(input('Enter the marks obtained :-  '))
#m5= int(input('Enter the marks obtained :-  '))

#avg_score = ()/5
#print(f'Your average score is :- {avg_score}')

total = 0 
print('Enter marks for all the five subjects :- ')

for i in range(6):
    score = int(input())
    total += score

avg = total/6
print(f'Marks obtained are :- {avg}')