# VarzeshYar-Website (ورزش‌یار)
<p align="center">
  <img src="https://github.com/mehrnaz-jiryaie/VarzeshYar-Website/assets/160396302/e7314c2f-2201-4084-a7a8-5a469697e79d" alt="VarzeshYar logo">
  <br>
  VarzeshYar logo
</p>

---
## About
This website is a project for completing a bachelor's degree at [Bu-Ali Sina University](https://basu.ac.ir/en/) of Hamedaan.
## Requirements
- [Python](https://www.python.org/downloads/) 3.12
- Django 5
## Instructions
Clone the repository on your computer :
```bash
git clone https://github.com/mehrnaz-jiryaie/VarzeshYar-Website.git
```
If you already have other versions of Python and Django installed on your computer, creating a virtual environment is recommended, then installing the requirements to avoid version conflicts.

Create a virtual environment :
```python
python -m venv your-virtual-env-name
```
Activate your virtual environment :

(for Linux)
```bash
source my_env/bin/activate
```

(for windows)
```bash
your-virtual-env-name\Scripts\activate
```


This project has a ```requirements.txt``` file that includes all Django packages required to run the code. These can be installed with the command :
``` python 
pip install -r requirements.txt
```
Run the database migrations :
``` python
python manage.py migrate
```
Run the Django development server with the command:
```python
python manage.py runserver
```
when you run this command, it listens to the port number '8000' by default, if this doesn't work try another port number like '8001' like this :
``` python
python manage.py runserver 8001
```
Last but not least, open your browser and then follow the http://127.0.0.1:8000 URL. 

