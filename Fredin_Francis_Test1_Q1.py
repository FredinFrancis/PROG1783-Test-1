print("** Fredin_Francis_8755328_Test1_Q1**")
print("\n")
print("Program to Convert Upper case to Lower Case or Vice-Versa")
print("\n")

# Receives input from user
word = str(input("Enter a word combination of Upper & Lower Case:- "))
i=0
while(i <= 0):
    l=word[i]
    i=i+1
#Defines the Characters of input word
    if((l >='a' and l <='z') or (l >='A' and l <='Z')):
        if(l== str.upper(l)):
            print("The Input Word is:-"+ word)
            print("The Converted Output:- " + str.lower(word))
        else:
            print("The Input Word is:- "+ word)
            print("The Converted Output:- " + str.upper(word))
    else:
        print(" Error Found !")