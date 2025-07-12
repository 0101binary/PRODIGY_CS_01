# Caesar Cipher Program

A Python program that implements the Caesar cipher algorithm for encrypting and decrypting text messages.

## Features

- **Encryption**: Encrypt messages using a specified shift value
- **Decryption**: Decrypt messages using the same shift value
- **Input Validation**: Validates shift values to ensure they are integers
- **Case Preservation**: Maintains uppercase and lowercase letters
- **Non-alphabetic Characters**: Preserves spaces, punctuation, and numbers
- **User-Friendly Interface**: Interactive menu-driven program
- **Demo Mode**: Includes demonstration with example messages

## How the Caesar Cipher Works

The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of positions down or up the alphabet. For example, with a shift of 3:

- A becomes D
- B becomes E
- C becomes F
- ...
- X becomes A
- Y becomes B
- Z becomes C

## Usage

### Running the Program

```bash
python caesar_cipher.py
```

### Program Options

1. **Encrypt a message**: Enter a message and shift value to encrypt
2. **Decrypt a message**: Enter an encrypted message and shift value to decrypt
3. **Exit**: Close the program

### Example Usage

```
Original message: Hello, World!
Shift value: 3
Encrypted message: Khoor, Zruog!

Encrypted message: Khoor, Zruog!
Shift value: 3
Decrypted message: Hello, World!
```

## Program Structure

- `caesar_cipher(text, shift, mode)`: Core encryption/decryption function
- `validate_shift(shift_str)`: Validates and converts shift input
- `main()`: Main program loop with user interface
- `demo()`: Demonstrates the cipher with example messages

## Features Explained

### Case Preservation
The program maintains the original case of letters:
- "Hello" with shift 3 becomes "Khoor"
- "WORLD" with shift 3 becomes "ZRUOG"

### Non-alphabetic Characters
Spaces, punctuation, and numbers remain unchanged:
- "Hello, World! 123" with shift 3 becomes "Khoor, Zruog! 123"

### Shift Validation
The program validates that shift values are integers and provides clear error messages for invalid input.

## Security Note

The Caesar cipher is a very basic encryption method and should not be used for securing sensitive information. It's primarily used for educational purposes and simple text obfuscation.

## Requirements

- Python 3.x
- No additional dependencies required

## Running the Demo

The program starts with a demonstration showing:
- Original messages
- Encrypted versions with shift=3
- Decrypted versions to verify the algorithm

This helps users understand how the cipher works before using the interactive menu. 