import random;


def guess_number(x):

    print("¡Welcome to the Game!");
    print("Your goal is to guess the generated number by the computer");

    random_number = random.randint(1, x);

    prediction = 0;

    while prediction != random_number:
        prediction = int(input(f"Guess a number between 1 and {x}: "));

        if prediction < random_number:
            print("Tray again. This number is small");
        elif prediction > random_number:
            print("Try again. This number is big");
    
    print(f"Congratulations! You guessed the number {random_number} correctly ");


guess_number(10);