
# 🛒 GreatKart – Django E-commerce Platform

**GreatKart** is a feature-rich e-commerce web application built with Django. It offers a robust foundation for online shopping platforms, incorporating essential functionalities such as user authentication, product management, shopping cart, order processing, and more.

## 🚀 Features

- **User Authentication**: Secure registration, login, and profile management.
- **Product Catalog**: Organized product listings with categories and detailed views.
- **Shopping Cart**: Add, update, and remove items with real-time cart updates.
- **Order Management**: Seamless checkout process with order tracking.
- **Admin Dashboard**: Manage products, orders, and users efficiently.
- **Responsive Design**: Mobile-friendly interface for optimal user experience.

## 🛠️ Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, Bootstrap
- **Database**: SQLite (default), easily switchable to PostgreSQL or MySQL
- **Others**: Django Templates, Static Files Management

## 📸 Screenshots

*Include relevant screenshots here to showcase the application's interface.*

## 🧰 Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/mdjakariarahman/django-class-greatkart.git
   cd django-class-greatkart
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`.

## ⚙️ Configuration

- **Static Files**: Ensure static files are correctly configured in `settings.py`.
- **Media Files**: Set up media root and URL for handling user-uploaded content.
- **Email Backend**: Configure email settings for functionalities like password reset.

## 🧪 Testing

To run the test suite:
```bash
python manage.py test
```
Ensure all tests pass to confirm the application's integrity.

## 📦 Deployment

For deploying the application to a production environment:

- **Collect Static Files**
  ```bash
  python manage.py collectstatic
  ```

- **Configure Web Server**: Set up a web server like Nginx or Apache.
- **Use WSGI Server**: Deploy using Gunicorn or uWSGI.
- **Secure the Application**: Implement HTTPS and other security best practices.

*Consider using platforms like Heroku, AWS Elastic Beanstalk, or DigitalOcean for deployment.*

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙌 Acknowledgements

- Inspired by various Django e-commerce tutorials and projects.
- Special thanks to the Django community for continuous support and resources.
