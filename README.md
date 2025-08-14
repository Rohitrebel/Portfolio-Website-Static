# Portfolio Website - Static

## Overview

A personal portfolio website to showcase my projects, skills, and experience.
Built using HTML, CSS to create a clean and professional online presence.

## Live Demo

[Visit Website](https://portfolio-website-static-49ow.onrender.com/)

---

## Features

- Clean and modern UI.
- Smooth scrolling and animations.
- Sections for **Home**, **Projects**, **Resume/CV**, and **Contact**.
- Easy to customize and maintain.

---

## Technologies Used

- HTML5, CSS3
- Flexbox
- Python/Flask
- Jinja2 Engine
- **Deployment:** Render

---

## Project Structure

```
Portfolio-Website-Static/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Project dependencies
├── Procfile                # Deployment instructions (for Render)
│
├── templates/              # HTML templates
│   ├── index.html
│   ├── contact.html
│
├── static/                 # CSS, JS, and image files
│   ├── css/
│   ├── images/
│
└── README.md               # Project documentation

```

---

## Installation & Setup (Locally)

1. **Clone the repository**

   ```bash
   git clone https://github.com/Rohitrebel/Portfolio-Website-Static.git
   ```

2. **Navigate to the project folder**

   ```bash
   cd Portfolio-Website-Static
   ```

3. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   .venv\Scripts\activate
   ```

4. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

5. **To Run the Appliction Locally**

   ```bash
   python app.py
   ```

6. **Access the website**

   ```bash
   http://127.0.0.1:5000
   ```

---

## Deployment

You can deploy the portfolio website to:

- **Render** – For static or backend hosting

When deploying Flask apps, make sure to include:

Procfile with `web: gunicorn app:app`

requirements.txt with all dependencies

**Learning Outcomes**

- Setting up Flask routing

- Creating and serving HTML templates

- Adding and handling a contact form

- Understanding Jinja2 templating

- Deploying a Flask app to a cloud hosting platform

**Output**
![alt text](https://res.cloudinary.com/ddrbrwcvz/image/upload/v1755192423/Screenshot_3280_wpaduh.png)

---

⭐ _If you like this project, feel free to star the repo!_
