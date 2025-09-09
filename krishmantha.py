import random
import time

def create_question(min_num, max_num):
    #Generate a simple addition question with numbers between min_num and max_num
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    operator = random.choice(["+", "-"])
    return str(num1) + " " + operator + " " + str(num2)

def ask_question(question):
     #Ask the question, measure response time, and check correctness.
    start_time = time.time()
    answer = input("What is " + question + "? ")
    end_time = time.time()
    try:
        correct_answer = eval(question)
        is_correct = int(answer) == int(correct_answer)
    except:
        is_correct = False
    response_time = int(end_time - start_time)
    return is_correct, response_time

print("Welcome to Krishmantha's Maths Test!")

difficulty = ""
# Get valid difficulty choice until user type either easy,medium or hard
while difficulty not in ["easy", "medium", "hard"]:
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()

# Set variables based on difficulty
if difficulty == "easy":
    questions = 5
    max_num = 10
elif difficulty == "medium":
    questions = 10
    max_num = 20
else:
    questions = 15
    max_num = 50

print("You have chosen " + difficulty + " mode with " + str(questions) + " questions.")

# Initialize variables
score = 0
correct_count = 0
total_response_time = 0
results_correctness = []
results_times = [] # To store (question, is_correct, response_time, points)

# Main question loop
for i in range(questions):
    print("\nScore: " + str(score))
    print("Question " + str(i + 1) + " of " + str(questions))

    #Determine number range for question
    if i == questions - 1: #Final question
        min_num = max_num
        question_max_num = max_num * 2
        print("Challenge question!")
    else:
        min_num = max_num // 2
        question_max_num = max_num
    # Generate and ask question
    question = create_question(min_num, question_max_num)
    is_correct, response_time = ask_question(question)

    results_correctness.append(is_correct)
    results_times.append(response_time)
    total_response_time += response_time
    # Calculate points and update totals
    if is_correct:
        points = max(1, 10 - response_time)
        print("Correct! You took " + str(response_time) + " seconds and earned " + str(points) + " points.")
        score += points
        correct_count += 1
    else:
        print("Incorrect. You took " + str(response_time) + " seconds and earned 0 points.")
        
# Print final results
print("\nFinal Score: " + str(score))
print("Percentage Correct: " + str(int((correct_count / questions) * 100)) + "%")
average_time = total_response_time // questions
print("Average Response Time: " + str(average_time) + " seconds")

# Breakdown section with "Question"
print("\nBreakdown")
print("Question   Correct   Time(s)")
print("-----------------------------")
for i in range(questions):
    if results_correctness[i]:
        result = "Yes"
    else:
        result = "No"
    print("Question " + str(i + 1) + "   " + result + "   " + str(results_times[i]))