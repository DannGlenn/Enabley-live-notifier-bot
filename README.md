# Enabley live session notifier

A simple quality of life bot.  
Meant to automatically login to Enabley,  
and recognize when Enabley live session is on and alert the user.   
Currently runs on Windows using Chrome browser.  

## Installation and Setup

1. Install and create a virtual environment (recommended):  

Install:
```bash
pip install virtualenv
```
Create:
```bash
python -m virtualenv myenv
```
Activate
```bash
.\myenv\Scripts\activate
```
2. Install requirements using the `requirements.txt` file provided:
```bash
pip install -r requirements.txt
```

3. Make sure your Google Chrome version is up to date (Version 107 or higher)

## Configuration

1. Enter your enabley username and password in `/src/__init__.py` at the proper consts for auto login  
also, set the desired interval between checks, 10 seconds will usually suffice
```bash
PASSWORD = 'your password'
USERNAME = 'your e-mail'
REFRESH_EVERY = 10 #seconds
```

2. Run the App:
```bash
py .\main.py
```

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](/LICENSE.txt)