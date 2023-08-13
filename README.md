![Screenshot](./static/images/home1.png?raw=true "Screenshot")
# MyNews

MyNews is an Blog API where you can create posts and update people about your new endeavors. Also, others users can also comment on your posts!

## Features

#### **Publish your recent endeavors!**
https://github.com/paulo-ads/MyNewsDjango/assets/116691517/c98a0a1c-466b-439e-b458-49d2ac830d63
#
#### **Read and comment posts!**
https://github.com/paulo-ads/MyNewsDjango/assets/116691517/300384b2-6ade-480a-8be2-7f1cf48fe387

## How to run it locally
**Make sure you have Python 3 installed on your machine*


**The post creation is made through the Administration tool! The default superuser's credentials are:*
```bash
User: admin
Password: admin
```

#### Clone the project:
```bash
git clone https://github.com/paulo-ads/MyNewsDjango.git
```
#### Create a virtual environment:
```bash
python -m venv venv
```
#### Activate the virtual environment:
**On windows systems*:
```bash
venv\Scripts\activate
```
**On MacOS and Linux systems*:
```bash
source venv/bin/activate
```
#### Install the dependencies:
```bash
pip install -r requirements.txt
```
#### Start the server:
```bash
python manage.py runserver
```

#### Per default, the server will start on the port 8000
**You can access it on http://localhost:8000/*

## Stack
**Frontend:** Bulma

**Backend:** Django
