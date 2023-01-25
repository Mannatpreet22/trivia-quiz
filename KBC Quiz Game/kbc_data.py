import classes

questions_text = [
    "Which is the largest country in the world?",
    "How many days are there in a leap year?",
    "Which one of these four birds has the longest beak and feet?",
    "What is the national currency of the United States of America (USA)?",
    "Guido van Rossum in 1991 designed which language?",
    "Finish the sequence: 9, 18, 27, _?",
    "Which one is the first fully supported 64-bit operating system?",
    "Which animal is called the king of the jungle?",
    "what time corresponds to 23:23 hours ?",
    "Which team has won most number of IPL matches ?",
    "Which is the largest planet in our Solar system?",
    "How many continents are there in the world?",
    "How many years are there in one Millenium?",
    "ipad is manufactured by?",
    "Who founded Microsoft?",
]

first_option = [
    "India",
    "354",
    "Heron",
    "Euro",
    "Javascript",
    "36",
    "Windows 7",
    "Elephant",
    "11:23PM",
    "KKR",
    "Earth",
    "8",
    "100 years",
    "Google",
    "Monty Ritz",
]

second_option = [
    "USA",
    "366",
    "Parrot",
    "Peso ",
    "Python",
    "34",
    "Linux",
    "Lion",
    "11.11PM",
    "CSK",
    "Uranus",
    "5",
    "50 years",
    "Microsoft",
    "Danis Lio",
]

third_option = [
    "China",
    "365",
    "Crow",
    "Dollar",
    "Java",
    "30",
    "Mac",
    "Tiger",
    "7:23PM",
    "MI",
    "Mars",
    "7",
    "500 years",
    "Amazon",
    "Bill Gates",
]

fourth_option = [
    "Russia",
    "420",
    "Pigeon",
    "Yen",
    "C++",
    "37",
    "Windows XP",
    "Cow",
    "9.11PM",
    "RCB",
    "Jupiter",
    "6",
    "1000 years",
    "Apple",
    "Jeff Bezos",
]

correct_answers = [
    "Russia",
    "366",
    "Heron",
    "Dollar",
    "Python",
    "36",
    "Linux",
    "Lion",
    "7:23PM",
    "MI",
    "Jupiter",
    "7",
    "1000 years",
    "Apple",
    "Bill Gates",
]

questions = []

for i in range(len(questions_text)):
    questions.append(
        classes.Question(
            questions_text[i],
            first_option[i],
            second_option[i],
            third_option[i],
            fourth_option[i],
            correct_answers[i],
        )
    )
