# Wiki (Project 1) — CS50W

A Wikipedia-like online encyclopedia for [CS50W: Web Programming with Python and JavaScript](https://www.edx.org/learn/web-development/harvard-university-cs50-s-web-programming-with-python-and-javascript#ace-recommendation-card-component)

## Description

This project is a wiki-style web application that allows users to create, edit, search, and view encyclopedia entries written in Markdown. Entries are rendered dynamically into HTML, and users can browse all pages or search for specific content. The application was developed as part of CS50W to practice Django-based web development and core web programming concepts.

## Built with

- ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
- ![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
- ![CSS](https://img.shields.io/badge/css-%23663399.svg?style=for-the-badge&logo=css&logoColor=white)
- ![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)

## Features

- View encyclopedia entries rendered dynamically as HTML
- Browse a list of all available pages
- Search for entries by title or substring
- Create new entries written in Markdown   
- Edit existing entries  
- Access a random encyclopedia entry

## Dependencies

- Django — backend web framework
- markdown2 — used to convert Markdown content into HTML

## How to Run
> The following commands assume a Unix-like environment (Bash).

1. Make sure you have Python 3 installed.

2. Clone this repository and navigate into the project directory.

3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
5. Run the development server:
   ```bash
   python3 manage.py runserver
   ```
   
6. Open your browser and go to:
   ```
   http://127.0.0.1:8000/
   ```


