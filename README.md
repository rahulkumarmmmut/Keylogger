# Keylogger

This Python-based KeyLogger is designed as an educational tool to demonstrate the workings of software that can capture and log keystrokes on a computer. It's built with an emphasis on safety, flexibility, and usability, incorporating advanced features such as inactivity detection and thread-safe operations. This project is intended strictly for educational purposes, to understand the mechanisms behind keylogging software and enhance cybersecurity awareness.


## Functionalities
1. Keystroke Logging: Captures and logs every keystroke, including alphanumeric characters and special keys, with customized handling for each.

2. Automatic Flush: Automatically writes the buffered keystrokes to a file at configurable intervals, ensuring data persistence.

3. Inactivity Detection: Utilizes a separate thread to monitor user inactivity, automatically shutting down after a specified timeout period to prevent indefinite running.

4. Thread-Safety: Ensures safe concurrent execution with threading.Lock, preventing data corruption and ensuring consistent behavior in a multi-threaded environment.
Customizable Settings: Allows users to set their desired intervals for data flushing and inactivity timeouts, accommodating various use cases.

5. Robust Error Handling: Implements comprehensive error handling for file operations and key processing to gracefully handle exceptions.

## Usage
Ensure you have Python installed on your system and install the required dependencies:
```Python
pip3 install pynput
```
To start the keylogger, simply execute the script:
```Python
python3 Keylogger_Advanced.py
```
The keylogger will run in the background, logging all keystrokes to log.txt. To stop the keylogger, press the escape key.

## Ethical Usage Notice
This KeyLogger is intended solely for educational purposes, to demonstrate and teach the principles behind such software. It is crucial to use this tool responsibly and ethically, with explicit consent from all parties involved. Unauthorized use of this KeyLogger to spy on individuals without their consent is strictly prohibited and may violate privacy laws.

## License

MIT License

Copyright (c) 2024 Rahul Kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
