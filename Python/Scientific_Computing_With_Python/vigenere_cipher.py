import os

# Function to read from a text file
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Function to write to a text file
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# The Vigenère cipher function
def vigenere(message, key, direction=1, alphabet='abcdefghijklmnopqrstuvwxyz'):
    key_index = 0
    final_message = ''
    alphabet_length = len(alphabet)

    for char in message:
        # Preserve the original case of the character
        is_upper = char.isupper()
        char = char.lower()

        if char.isalpha():
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)].lower()
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % alphabet_length
            encrypted_char = alphabet[new_index]

            # Convert back to uppercase if the original was uppercase
            if is_upper:
                encrypted_char = encrypted_char.upper()

            final_message += encrypted_char
        else:
            # Append any non-letter character as is
            final_message += char
    
    return final_message

# Function to encrypt the content
def encrypt(message, key):
    return vigenere(message, key)

# Function to decrypt the content
def decrypt(message, key):
    return vigenere(message, key, direction=-1)

# Main function to handle file operations with user input
def main():
    # Prompt the user for encryption or decryption
    action = input("Do you want to (e)ncrypt or (d)ecrypt the file? ").strip().lower()
    
    # Prompt the user for input and output file paths and the encryption key
    input_file = input("Enter the path to the input file: ")
    output_dir = input("Enter the directory to save the output file: ")
    custom_key = input("Enter the encryption/decryption key: ")

    # Ensure the output directory ends with a slash
    if not output_dir.endswith(("\\", "/")):
        output_dir += os.sep

    # Generate an output file name based on the input file name
    if action == 'e':
        output_file_name = os.path.basename(input_file).replace('.txt', '_encrypted.txt')
    elif action == 'd':
        output_file_name = os.path.basename(input_file).replace('.txt', '_decrypted.txt')
    else:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
        return

    output_file = output_dir + output_file_name

    # Read the content from the input file
    text = read_file(input_file)

    # Perform the chosen action
    if action == 'e':
        result_text = encrypt(text, custom_key)
    else:
        result_text = decrypt(text, custom_key)

    # Write the result to the output file
    write_file(output_file, result_text)

    print(f'Resulting text has been saved to {output_file}')

# Run the main function
if __name__ == "__main__":
    main()
