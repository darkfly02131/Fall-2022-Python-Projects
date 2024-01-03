#!/usr/bin/env python3
#Zachary Lord

#Function to display a welcome message
def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")

#Function gets scores from the user
def get_scores(scores):
    score_total = 0
    counter = 0
    while True:
        score = input("Enter test score: ")
        if score == "x":
            break

            return scores
        else:
            score = int(score)
            scores.append(score)

         
        
#Function to process scores
def process_scores(scores):
    # calculate average score
    #average = score_total / count
                
    # format and display the result
    total = sum(scores)
    print("Score total:       ", str(total))
    minimum = min(scores)
    print('Low Scores:        ', minimum)
    maximum = max(scores)
    print('High Scores:       ', maximum)
    length = len(scores)
    print("Number of Scores:  ", len(scores))
    
   
    
def main():
    display_welcome()
    scores = []
    get_scores(scores)
    process_scores(scores)
    print("")
    print("Bye!")


if __name__ == "__main__":
    main()


