# Caesar_cipher_algorithm-
A simple Python implementation of the **Caesar Cipher encryption technique** that can encrypt and decrypt messages containing letters and numbers.

📌 Features
* Encrypt text using a shift value
* Decrypt encrypted text
* Supports **uppercase and lowercase letters**
* Supports **numeric digit shifting (0–9)**
* Keeps **spaces and special characters unchanged**

⚙️ How It Works

The Caesar Cipher shifts characters by a fixed number (shift value).

Example with shift = 3:

A → D
B → E
C → F

For numbers:

1 → 4
2 → 5
3 → 6

Alphabet characters wrap around using **modulo 26**, and numbers wrap using **modulo 10**.

📂 Project Structure
caesar-cipher/
│
├── caesar_cipher.py
└── README.md
▶️ Usage

1. Clone the repository
git clone https://github.com/Ghanshyam-Bind/Caesar_cipher_algorithm-.git

3. Navigate to the project folder
cd caesar-cipher

4. Run the Python script
python task1.py

💻 Example

Input:
Enter your message: i am 23 years old boy

Enter shift value: 3

Type E'encrypt' or D'decrypt': encrypt

Output:
Result: l dp 56 bhduv rog erb

Decrypting with the same shift:

Result: i am 23 years old boy


🛠 Requirements

* Python 3.x

📚 Concepts Used

* Caesar Cipher Encryption
* ASCII manipulation using `ord()` and `chr()`
* Modulo arithmetic
* String processing in Python

⚠️ Note

This project is for **educational purposes only**. The Caesar Cipher is a basic encryption method and **not secure for real-world applications**.

👨‍💻 Author
Ghanshyam Bind
