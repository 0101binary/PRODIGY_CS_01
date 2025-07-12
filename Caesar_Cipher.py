def caesar_cipher(text, shift, mode='encrypt'):
    """
    Perform Caesar cipher encryption or decryption.
    
    Args:
        text (str): The text to encrypt or decrypt
        shift (int): The shift value (positive for encryption, negative for decryption)
        mode (str): 'encrypt' or 'decrypt'
    
    Returns:
        str: The encrypted or decrypted text
    """
    result = ""
    
    # Handle decryption by negating the shift
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Determine the base (a=97 for lowercase, A=65 for uppercase)
            base = ord('a') if char.islower() else ord('A')
            # Apply the shift and wrap around the alphabet
            shifted = (ord(char) - base + shift) % 26
            result += chr(base + shifted)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    
    return result

def validate_shift(shift_str):
    """
    Validate and convert shift input to integer.
    
    Args:
        shift_str (str): The shift value as string
    
    Returns:
        int: The validated shift value
    """
    try:
        shift = int(shift_str)
        return shift
    except ValueError:
        print("Error: Shift value must be an integer.")
        return None

def main():
    """
    Main function to run the Caesar cipher program.
    """
    print("=" * 50)
    print("           CAESAR CIPHER PROGRAM")
    print("=" * 50)
    print()
    
    while True:
        print("Choose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        print()
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            # Encryption
            message = input("Enter the message to encrypt: ")
            shift_input = input("Enter the shift value (positive integer): ")
            
            shift = validate_shift(shift_input)
            if shift is not None:
                encrypted = caesar_cipher(message, shift, 'encrypt')
                print(f"\nEncrypted message: {encrypted}")
                print(f"Shift value used: {shift}")
        
        elif choice == '2':
            # Decryption
            message = input("Enter the message to decrypt: ")
            shift_input = input("Enter the shift value (positive integer): ")
            
            shift = validate_shift(shift_input)
            if shift is not None:
                decrypted = caesar_cipher(message, shift, 'decrypt')
                print(f"\nDecrypted message: {decrypted}")
                print(f"Shift value used: {shift}")
        
        elif choice == '3':
            print("Thank you for using the Caesar Cipher program!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
        
        print("\n" + "-" * 50 + "\n")

def demo():
    """
    Demonstrate the Caesar cipher with example messages.
    """
    print("=" * 50)
    print("           CAESAR CIPHER DEMO")
    print("=" * 50)
    print()
    
    # Example messages
    messages = [
        "Hello, World!",
        "Python Programming",
        "Caesar Cipher Algorithm"
    ]
    
    shift = 3
    
    for message in messages:
        print(f"Original message: {message}")
        encrypted = caesar_cipher(message, shift, 'encrypt')
        print(f"Encrypted (shift={shift}): {encrypted}")
        decrypted = caesar_cipher(encrypted, shift, 'decrypt')
        print(f"Decrypted: {decrypted}")
        print("-" * 40)

if __name__ == "__main__":
    # Run demo first
    demo()
    print("\n" + "=" * 50 + "\n")
    
    # Run main program
    main() 