# Simple aiohttp Example

A basic Python example that uses aiohttp to make an HTTP GET request to Google.

## Setup

1. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the program:
   ```
   python main.py
   ```

## What it does

The program makes an asynchronous HTTP GET request to Google's homepage and prints:
- The HTTP status code
- The length of the returned HTML content
- A success message 