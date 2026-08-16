# SCT_CS_1 — Caesar Cipher Program

## Task
Task 1 of the SkillCraft Technology Cyber Security Internship.

A simple command-line tool that encrypts and decrypts text messages using
the Caesar Cipher technique — a classic substitution cipher where each
letter is shifted a fixed number of places in the alphabet.

## How It Works
- **Encryption:** each letter in the message is shifted forward by the
  given shift value (wrapping around from Z back to A).
- **Decryption:** the same shift is applied in reverse (a negative shift).
- Non-alphabet characters (spaces, numbers, punctuation) are left unchanged.
- Uppercase and lowercase letters are both supported and keep their case.

## Files
- `caesar_cipher.py` — the main program

## How to Run
```bash
python3 caesar_cipher.py
```

You'll be prompted to:
1. Choose `1` to encrypt or `2` to decrypt
2. Enter your message
3. Enter a shift value (e.g. `3`)

## Example
```
Enter choice (1 or 2): 1
Enter your message: Hello World
Enter shift value: 3
Encrypted message: Khoor Zruog
```

## Internship
SkillCraft Technology — Cyber Security Track
