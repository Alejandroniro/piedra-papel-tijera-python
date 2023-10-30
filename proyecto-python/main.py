import random

def get_user_choice():
    user_choice = input("Elige piedra, papel o tijera: ").lower()
    if user_choice in ['piedra', 'papel', 'tijera']:
        return user_choice
    else:
        print("Opción no válida. Por favor, elige piedra, papel o tijera.")
        return get_user_choice()

def get_computer_choice():
    options = ['piedra', 'papel', 'tijera']
    return random.choice(options)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Empate"
    elif (user_choice == 'piedra' and computer_choice == 'tijera') or (user_choice == 'tijera' and computer_choice == 'papel') or (user_choice == 'papel' and computer_choice == 'piedra'):
        return "¡Ganaste!"
    else:
        return "La computadora gana."

def main():
    print("Bienvenido al juego de Piedra, Papel o Tijera.")
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"Tú elegiste: {user_choice}")
        print(f"La computadora eligió: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "¡Ganaste!":
            user_score += 1
        elif result == "La computadora gana.":
            computer_score += 1

        print(f"Marcador: Tú ({user_score}) - Computadora ({computer_score})")
        play_again = input("¿Quieres jugar de nuevo? (s/n): ").lower()
        if play_again != 's':
            break

if __name__ == '__main__':
    main()