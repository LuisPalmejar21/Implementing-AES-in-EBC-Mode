# Our Implementation of AES in ECB Mode
## Library Used 
**PyCryptodome** 

Referred documentation for the implementation link:
https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#ecb-mode

## How to Run the Implementation
**Running the implementation requires installation of PyCryptodome.**

1. Navigate in terminal until you reach the folder: "AES in ECB Mode".

2. To install PyCryptodome while in the current directory, enter the provided command in the terminal:
`pip install pycryptodome`

3. After installing PyCryptodome, Run the implementation by typing in `py AES.py` in terminal, then the terminal will prompt you: "Enter your message:".

4. After entering the message, the terminal will output the ciphertext and the decrypted text.
## Design Decisions
For our implementiation of AES in ECB mode, we depend on the PyCryptodome library to do the encryption and decryption.

For encryption and decryption, we first created an ECB object using this specified PyCryptodome function:

`AES.new(key, AES.MODE_ECB)`

After creating an ECB object, we encyrpt an ECB object and encode it during encryption using these specified PyCryptodome functions:

`cipher.encrypt(padded_text)`

`base64.b64encode(ctext)`

During decryption, we decode an ECB object and decrypte it using these specified PyCryptodome functions:

`base64.b64decode(ciphertext)`

`cipher.decrypt(decoded)`

`unpad(padded_text, AES.block_size)`

We prompt a user to enter a message when a user runs the program. After entering the message,
 the code outputs the ciphertext and the decrypted message.
 If the decrypted message matches with the input message a user types in, our encryption/decryption implementation is working correctly.

## Sample Inputs/Outputs

### Sample Input 1:
Enter your message: test<br> 
The ciphertext is: b'b+27owOL51LilVcK1dZAqQ=='<br>
The decrypted message is: test

### Sample Input 2:
Enter your message: I lov3 Crypt0gt@phy!!!<br> 
The ciphertext is: b'rxK/rsA/DiXSb9dhGWgwPWZdRZuNXDNsvUUqs3/vNqo='<br>
The decrypted message is: I lov3 Crypt0gt@phy!!!
