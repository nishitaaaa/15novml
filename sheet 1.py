#Q2
print (5**9)
print (3//2)
print (7//3)
print (7/3)
print (6 == 6)
a = 20; a+= 30; a%=3;
print(a)
print (True * False)
print (True & False)
print (True and False)
print (((6>3) and (7<4) or (18==3)) and (9>3))
print (True is False)
# print (False in ‘False’)    this shows error
print (((True == False) or (False > True)) and (False <= True))


#Q3
s1 = "Nice to have it"                                   
s2 = " here"
print(s1+s2)


#Q4
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print (a[3][1][2][0])


#Q5
a.insert(0,s1)
a+=[s2]
print(a)


#Q6
numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 
687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 
742, 717, 958,743, 527]



for i in numbers:
    if i== 237:
        print(i)
        break
    elif i % 2 == 0:
        print(i)
            

#Q7
color_list_1 = set(["White", "Black", "Red"]) 
color_list_2 = set(["Red", "Green"])

print ( color_list_1-color_list_2)

n=eval(input('enter the number:'))
n2= str(n)*2
n3= str(n)*3
n4= int(n+int(n2)+int(n3))
print(n4)

#Q11
a=eval(input('enter the list:'))
a.split(',')
sorted(a)
print(a)

#Q12
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],
'Marks': [57,87,67,79]}
d1=d['Marks']
l=max(d['Marks'])
j=0
for i in range(len(d1)):
    if(d1[i]==l):
        j=i

d2=d['Student']
print(d2[j])

#Q13
s=input("Enter a string:")
l=0
d=0
for i in s:
    if i.isalpha():
        l=l+1
    if i.isdigit():
        d=d+1
print("LETTERS ",l)
print("DIGITS ",d)





        
