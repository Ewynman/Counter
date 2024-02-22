def calculate_count(card):
    if card in ['2', '3', '4', '5', '6']:
        return 1
    elif card in ['10', 'J', 'Q', 'K', 'A']:
        return -1
    else:
        return 0

def main():
    num_decks = int(input("Enter the number of decks: "))
    num_of_cards = num_decks * 52

    while True:
        remaining_decks = num_of_cards / 52
        
        num_players = int(input("Enter number of players (1-7) or enter 0 to stop: "))
        
        if num_players == 0:
            print("Exiting the program.")
            break
        
        if num_players < 1 or num_players > 7:
            print("Invalid number of players. Please enter a number between 1 and 7.")
            continue

        player_counts = {f"Player {i+1}": 0 for i in range(num_players)}
        player_hands = {f"Player {i+1}": [] for i in range(num_players)}
        dealer_cards = []

        # Dealing cards to players and dealer
        print("\nOkay, let's start:")
        print(f"{num_players} players, enter each player's first card:")

        for i in range(num_players):
            card = input(f"Enter player {i+1} first card: ").upper()
            player_hands[f"Player {i+1}"].append(card)
            num_of_cards -= 1

        dealer_card = input("Enter dealer card: ").upper()
        dealer_cards.append(dealer_card)
        num_of_cards -= 1

        # Second cards
        print("\nNow, enter second cards for each player:")
        for i in range(num_players):
            card = input(f"Enter player {i+1} second card: ").upper()
            player_hands[f"Player {i+1}"].append(card)
            num_of_cards -= 1

        print("\nInitial counts:")
        for player, hand in player_hands.items():
            hand_value = sum(calculate_count(card) for card in hand)
            print(f"{player}: {hand_value}")
            player_counts[player] += hand_value
        print(f"Dealer: {sum(calculate_count(card) for card in dealer_cards)}")

        # Player's turn
        for i in range(num_players):
            player = f"Player {i+1}"
            while True:
                hand = player_hands[player]
                hand_value = sum(calculate_count(card) for card in hand)
                decision = input(f"\n{player}'s turn, do you want to hit? (Yes/No) {hand_value}: ").lower()
                if decision == 'no':
                    break
                elif decision == 'yes':
                    card = input("Enter card: ").upper()
                    player_hands[player].append(card)
                    num_of_cards -= 1
                    hand_value = sum(calculate_count(card) for card in player_hands[player])  # Recalculate hand total
                    print(f"{player} count: {hand_value}")  # Display player's total count
                    print("Do you want to hit?")
                else:
                    print("Invalid input! Please enter 'Yes' or 'No'.")


        # Dealer's turn
        dealer_count = sum(calculate_count(card) for card in dealer_cards)

        # Asking for dealer's second card
        dealer_second_card = input("Enter dealer's second card: ").upper()
        dealer_cards.append(dealer_second_card)
        num_of_cards -= 1
        dealer_count += calculate_count(dealer_second_card)

        while True:
            decision = input("\nDoes the dealer want to hit? (Yes/No): ").lower()
            if decision == 'no':
                break
            elif decision == 'yes':
                card = input("Enter card: ").upper()
                num_of_cards -= 1
                dealer_count += calculate_count(card)
                print(f"Dealer count: {dealer_count}")
            else:
                print("Invalid input! Please enter 'Yes' or 'No'.")

        # Calculate total count for the table
        total_count = sum(player_counts.values()) + dealer_count

        # Update remaining number of decks
        remaining_decks = num_of_cards / 52
        print(remaining_decks)
        print(num_of_cards)

        true_count = total_count / remaining_decks

        print("\nRound end:")
        for player, count in player_counts.items():
            print(f"{player} count: {count}")
        print(f"Dealer count: {dealer_count}")
        print(f"Running count: {total_count}")
        print(f"True Count: {true_count}")

if __name__ == "__main__":
    main()
