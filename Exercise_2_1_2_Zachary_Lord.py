#!/usr/bin/env python3
#Zachary Lord

# display a welcome message
print("Enter 3 test scores")
print("======================")

# get scores from the user

#scores
score_one= int(input('Enter test score: '))
score_two= int(input('Enter test score: '))
score_three= int(input('Enter test score: '))

            

# calculate average score
average_score = round(score_one + score_two + score_three)
average_score = round(average_score / 3)
total_score= round(score_one + score_two + score_three)          
# format and display the result
print("======================")
print('Your Scores:   \t',score_one, score_two, score_three)
print("Total Score:\t", total_score)
print("Average Score:\t", average_score)
print()


