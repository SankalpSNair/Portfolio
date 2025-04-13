# Portfolio Website

A beautiful and responsive portfolio website built with Django to showcase projects and skills, with a contact form that stores messages in a database.

## Features

- Responsive design that works on all devices
- Contact form with database storage for messages
- Admin interface to view and manage contact messages
- Sections for skills, projects, education, and more

## Technologies Used

- Django 5.0.6
- HTML5/CSS3
- JavaScript
- Bootstrap
- Boxicons
- Font Awesome

## Local Development

1. Clone the repository:
   ```
   git clone https://github.com/SankalpSNair/Portfolio.git
   cd Portfolio
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```
   python manage.py migrate
   ```

4. Create a superuser (for admin access):
   ```
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```
   python manage.py runserver
   ```

6. Visit http://127.0.0.1:8000 in your browser

## Deployment on Render

This project is configured for easy deployment on Render.com:

1. Push your code to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Use the following settings:
   - Build Command: `./build.sh`
   - Start Command: `gunicorn portfolio_project.wsgi:application`
   - Add environment variables as specified in render.yaml

## License

MIT
