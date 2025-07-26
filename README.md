TASK 1 : BMI CALCULATOR 
📌 Objective
The Advanced BMI Calculator is a Python-based desktop GUI application built using Tkinter. It allows users to calculate their Body Mass Index (BMI) and receive health-related advice based on their BMI category. This project is part of the Oasis Infobyte Internship - Task 1 and aims to combine basic data science, GUI design, and data visualization to offer a health-focused utility application.
________________________________________
🛠️ Tools & Technologies Used
•	Python 3.x
•	Tkinter (for GUI)
•	Matplotlib (for plotting BMI trends)
•	JSON (for storing historical data)
•	OS, datetime, and standard Python libraries
________________________________________
🔍 Features
	✅ Calculate BMI based on weight and height
	✅ Categorize BMI (Underweight, Normal, Overweight, Obese)
	✅ Health advice based on BMI category
	✅ Store user entries (Name, Age, Gender, BMI, Timestamp) in a local JSON file
	✅ Visualize BMI trend over time using line chart
	✅ Dark Mode toggle for better user experience
	✅ Input validation and error handling
	✅ Clear button to reset fields easily
________________________________________
🚀 How It Works
1.	User Input:
Enter your name, age, gender, weight (in kg), and height (in meters).
2.	BMI Calculation:
On clicking "Calculate BMI", the app:
   o	Computes BMI using the formula weight / (height ** 2)
   o	Categorizes it into standard BMI categories
   o	Shows advice based on the category
   o	Saves the data into a bmi_data.json file for future use
3.	Visualization:
Clicking "Show BMI Trend" plots a time-series chart of all recorded BMI values using matplotlib.
4.	Dark Mode:
Toggle the checkbox at the top to switch the entire interface to dark mode.
📈 Outcome
This project demonstrates the practical use of Python for health-related applications. It combines GUI development, data processing, data visualization, and user interaction — making it a great foundational project for desktop applications and data-driven systems.



TASK 2: RANDOM PASSWORD GENERATOR
📌 Objective
The Advanced Password Generator is a Python GUI application built using Tkinter that generates secure, customizable passwords based on user preferences. This tool allows users to control password length, character types, repetition, and similarity exclusions. It's designed to enhance password security for personal or professional use.
This project was completed as Task 2 of the Oasis Infobyte Internship.
________________________________________
🛠️ Tools & Technologies Used
•	Python 3.x 
•	Visual Studio Code (VS Code) – development environment
•	Tkinter – for the graphical user interface
•	String, Random, Pyperclip – for password logic and clipboard copy
•	MessageBox – for error and status alerts
________________________________________
🔍 Features
	✅ Generate random passwords of customizable length
	✅ Options to include:
        o	Letters (uppercase & lowercase)
        o	Numbers
        o	Symbols
        o	Exclude similar characters (like O, 0, l, 1)
        o	Avoid repeating characters
	✅ Password strength indicator (Weak / Moderate / Strong)
	✅ Copy generated password to clipboard
	✅ Clear fields with one click
	✅ Clean and intuitive interface

🚀 How It Works
1.	Choose Password Settings
Select length, character types, and any restrictions using the checkboxes and input field.
2.	Click Generate Password
The app creates a password using the selected options and displays its strength.
3.	Copy to Clipboard or Clear
Use the provided buttons to copy the password or reset the form.

📈 Outcome
This project demonstrates the implementation of secure password generation techniques with an interactive GUI. It highlights skills in user interface design, Python logic handling, and real-world application utility.



TASK 3: CHAT APPLICATION
📌 Objective
The Chat Application is a basic client-server model built using Python's socket and threading libraries. It enables multiple clients to connect to a server and exchange messages in real time via the command-line interface. This project demonstrates real-time communication and concurrent client handling.
This project was completed as Task 3 of the Oasis Infobyte Internship.
________________________________________
🛠️ Tools & Technologies Used
•	Python 3.x 
•	Visual Studio Code (VS Code) – as the IDE
•	socket – for establishing connections
•	threading – for handling multiple clients simultaneously
________________________________________
🔍 Features
	✅ Multi-client chat using TCP socket communication
	✅ Real-time message broadcasting
	✅ Server displays all received messages
	✅ Each client runs in its own thread
	✅ Proper error handling for disconnection or message failures	✅ Minimal command-line interface for easy testing
________________________________________
🚀 How to Run the Project
🖥️ 1. Start the Server
    python server.py
 The server will start and listen on port 5555.
________________________________________
💻 2. Start Clients
Open a new terminal for each client and run:
      python client.py
You can open multiple terminals to simulate multiple clients chatting together.
________________________________________
⚙️ How It Works
•	The server listens for incoming connections on port 5555.
•	When a client connects, it’s added to the list of active clients.
•	Every incoming message from a client is:
    o	Received and printed on the server
    o	Broadcast to all other connected clients
•	threading.Thread is used to handle each client independently, allowing multiple users to chat simultaneously.
Outcome :
The project resulted in the successful development of a real-time chat application using Python’s socket and threading modules. The server efficiently handles multiple client connections concurrently, enabling smooth and uninterrupted communication. Clients are able to send and receive messages instantly over a TCP connection, simulating a basic chat environment. This project effectively demonstrates the principles of network communication and multithreaded programming in Python
