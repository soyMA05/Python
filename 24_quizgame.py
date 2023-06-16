def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("------------------------------")
        print(key)

def check_answer():
    pass

def display_score():
    pass

def play_again():
    pass

questions = {
    "Quien creo Python? " : "A",
    "Que anio fue creado Python" : "B"
}

options = [["A. Guido van Rossum", "B. Elons Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1986", "B. 1991", "C. 2000", "D. 2016"]]

new_game()