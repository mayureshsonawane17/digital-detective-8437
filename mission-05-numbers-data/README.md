Mission 5 


Task 5.1 — Convert numbers by hand

| Convert decimal 13 to binary. | 13 / 2 = 6 rem 1, 6 / 2 = 3 rem 0, 3 / 2 = 1 rem 1, 1 / 2 = 0 rem 1. Reading remainders bottom to top gives 1101. (Check: 8 + 4 + 1 = 13). Answer: 1101 |
| Convert decimal 25 to binary. | 25 / 2 = 12 rem 1, 12 / 2 = 6 rem 0, 6 / 2 = 3 rem 0, 3 / 2 = 1 rem 1, 1 / 2 = 0 rem 1. Reading remainders bottom to top gives 11001. (Check: 16 + 8 + 1 = 25). Answer: 11001 |
| Convert binary 1010 to decimal. | (1 x 2^3) + (0 x 2^2) + (1 x 2^1) + (0 x 2^0) = 8 + 0 + 2 + 0 = 10. Answer: 10 |
| Convert binary 1101 to decimal. | (1 x 2^3) + (1 x 2^2) + (0 x 2^1) + (1 x 2^0) = 8 + 4 + 0 + 1 = 13. Answer: 13 |
| Convert hexadecimal A to decimal. | In hexadecimal, A represents the value 10. Positional value: 10 x 16^0 = 10. Answer: 10 |
| Convert hexadecimal 1F to decimal. | In hexadecimal, 1 is in the 16s place and F is 15 in the 1s place: (1 x 16^1) + (15 x 16^0) = 16 + 15 = 31. Answer: 31 |
| Convert binary 1111 to hexadecimal. | Positional sum: (1 x 8) + (1 x 4) + (1 x 2) + (1 x 1) = 15. In base 16, 15 is written as F. Answer: F |

---

Task 5.2 — Verify using Python

| bin(13) | '0b1101' | Yes, matches 1101 |
| bin(25) | '0b11001' | Yes, matches 11001 |
| int('1010', 2) | 10 | Yes, matches 10 |
| int('1101', 2) | 13 | Yes, matches 13 |
| int('A', 16) | 10 | Yes, matches 10 |
| int('1F', 16) | 31 | Yes, matches 31 |
| hex(0b1111) | '0xf' | Yes, matches F |

---

Task 5.3 — Build a small number converter

I created number_converter.py which prompts the user for a decimal number, converts it using bin() and hex(), and prints both representations.

Test runs recorded:

| Test number | Binary output | Hexadecimal output |
| :--- | :--- | :--- |
| 10 | 0b1010 | 0xa |
| 42 | 0b101010 | 0x2a |
| 255 | 0b11111111 | 0xff |

Explanation of conversion functions:
- bin(): Takes an integer argument and converts it into its binary string representation prefixed with '0b'.
- hex(): Takes an integer argument and converts it into its lowercase hexadecimal string representation prefixed with '0x'.

---

Task 5.4 — How is text stored?

1. ASCII decimal codes:
   - Uppercase letter A: 65 (verified with ord('A'))
   - Lowercase letter a: 97 (verified with ord('a'))

2. Why computers need an encoding standard:
   Computers can only store electrical charge patterns representing binary 0s and 1s; they have no concept of letters or symbols. An encoding standard like ASCII or Unicode provides an agreed-upon dictionary that maps every letter, number, and punctuation mark to a specific numeric binary code so systems can reliably save, transmit, and read text without misinterpretation.

3. Example of a non-ASCII character:
   The Indian Rupee symbol (₹, Unicode U+20B9) or the Euro currency symbol (€) is not part of basic 7-bit ASCII, which only covers English characters from 0 to 127. These symbols require modern UTF-8 encoding.
