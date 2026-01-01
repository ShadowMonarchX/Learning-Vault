import pandas as pd

# Create a DataFrame to store the exam questions
exam_questions = pd.DataFrame(columns=['Question', 'Option A', 'Option B', 'Option C', 'Option D', 'Correct Answer'])

# Add some sample questions
question1 = {
    'Question': 'What is the capital of France?',
    'Option A': 'London',
    'Option B': 'Paris',
    'Option C': 'Berlin',
    'Option D': 'Rome',
    'Correct Answer': 'B'
}

question2 = {
    'Question': 'What is the largest planet in our solar system?',
    'Option A': 'Earth',
    'Option B': 'Jupiter',
    'Option C': 'Mars',
    'Option D': 'Saturn',
    'Correct Answer': 'B'
}

exam_questions = pd.concat([exam_questions, pd.DataFrame([question1, question2])], ignore_index=True)

# Display the exam questions
print("Exam Questions:")
print(exam_questions)
