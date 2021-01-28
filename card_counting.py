#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Card counting value (BlackJack) | ----\n", fg("red")))

# user interaction
cards = [i for i in input("Given cards: ").upper().split(", ")]

# list of possible cards
possible_cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

# function
def calculate_value(list_of_cards):
    # check if input is valid
    if any([i for i in list_of_cards if not i in possible_cards]):
        return exit("\nInvalid Input\n")

    # card counter
    value_counter = 0

    for card in list_of_cards:
        if card in possible_cards[:5]:
            value_counter += 1
        elif card in possible_cards[8:]:
            value_counter -= 1

    return value_counter

value = calculate_value(cards)

if value > 0:
    value = stylize(value, fg("green"))
    print(f"\nValue of the cards: {value}\n")
elif value < 0:
    value = stylize(value, fg("red"))
    print(f"\nValue of the cards: {value}\n")
else:
    print(f"\nValue of the cards: {value}\n")
