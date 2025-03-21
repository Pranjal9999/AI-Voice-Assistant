#Voice Assistant in Python

This is a simple AI-powered voice assistant built using Python. It can perform various tasks such as searching Wikipedia, opening websites, telling the time, and more.

Features

Greet the user based on the time of day

Recognize voice commands using speech_recognition

Perform searches on Wikipedia

Open popular websites like YouTube, Google, and Instagram

Open applications like VS Code

Fetch the current time

Speak responses using pyttsx3

Send emails using smtplib

Installation

Prerequisites

Make sure you have Python installed (Python 3.x recommended).

Install Required Packages

Run the following command to install the necessary dependencies:

pip install pyttsx3 speechRecognition wikipedia playsound

Usage

Run the script using:

python voice_assistant.py

After starting, the assistant will listen for commands and execute them accordingly.

Configuration

To enable email functionality, update the sendEmail function with your Gmail credentials. It is recommended to use App Passwords for security.

server.login('your-email@gmail.com', 'your-app-password')

Contributing

Feel free to fork this repository and submit pull requests with improvements.
