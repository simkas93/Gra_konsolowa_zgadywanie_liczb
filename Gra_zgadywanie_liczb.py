import random

print("Witaj w grze 'Jaka to liczba'!")
print("\nMam na myśli pewną liczbę z zakresu od 1 do 100.")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")

the_number = random.randint(1, 100)
guess = int(input("Ta liczba to: "))
tries = 1

while guess != the_number:
    if guess > the_number:
        print("Twoja liczba jest za duża... zgaduj dalej")
    else:
        print("Twoja liczba jest za mała... zgaduj dalej")

    guess = int(input("Ta liczba to: "))
    tries += 1

print("Odgadłeś! Ta liczba to", the_number)
print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!\n")
