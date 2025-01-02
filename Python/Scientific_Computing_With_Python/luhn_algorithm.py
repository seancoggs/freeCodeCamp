def calculate_luhn_sum(card_number):
    sum_of_digits = 0
    for i, digit in enumerate(reversed(card_number)):
        digit = int(digit)
        if i % 2 == 1:
            digit *= 2
            if digit >= 10:
                digit = (digit // 10) + (digit % 10)
        sum_of_digits += digit
    return sum_of_digits % 10 == 0

def validate_card_number(card_number):
    card_number = card_number.replace(" ", "").replace("-", "")
    if calculate_luhn_sum(card_number):
        print("VALID!")
    else:
        print("INVALID!")

# Example usage:
card_number = input("Enter a card number: ")
validate_card_number(card_number)