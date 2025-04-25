from gtts import gTTS

text = """
Hello doston!
Aaj hum Python programming language ko bilkul scratch se leke file handling tak samjhenge. Chaliye shuru karte hain.

Step 1: Python kya hai?
Python ek simple aur beginner-friendly programming language hai. Isme syntax bahut hi easy hota hai, aur isse aap automation, web development, data science sab kuch kar sakte ho.

Step 2: Variables and Data Types
Variable matlab ek container jisme data store hota hai.
Example: name equals Ajay, age equals 25.
Common data types: int, float, str, bool, list, tuple, dictionary.

Step 3: Conditional Statements
Agar kuch condition true hai, to kuch kaam karo — else kuch aur karo.
Example: if age greater than or equal to 18, then print "You are adult", else print "You are minor".

Step 4: Loops (for and while)
Loop ka use repeat karne ke liye hota hai.
Example: for i in range 5, print i.

Step 5: Functions
Function ek tarah ka reusable code block hota hai.
Example: def greet function, print "Hello, welcome to Python".

Step 6: File Handling
Python mein hum file create, read, write kar sakte hain using open function.
Modes: r for read, w for write, a for append, r plus for read and write.
Example: with open file dot txt in read mode as f, read data and print.
Similarly, for writing use w mode and write Hello World.

Important: with open ka use karne se file automatically close ho jaati hai.

Bas itna hi!
Yeh tha Python ka ek basic se lekar file handling tak ka journey. Practice karte rahiye, aur aap Python ke expert ban jaayenge.
"""

audio = gTTS(text=text, lang='en', slow=False)
audio.save("python_basics_to_file_handling.mp3")

print("🎧 Audio file 'python_basics_to_file_handling.mp3' created successfully!")
