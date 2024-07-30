first is I forked a repository original repository link is:
https://github.com/app-generator/django-black-dashboard

# Django Black Dashboard Project

This project is a modified version of the open-source Django Black Dashboard. The modifications include the addition of search functionality and API endpoints for user authentication.

## Added Functionality

1. **Search Functionality**: Implemented a search feature that allows users to search items in the database by name.
2. **User Authentication API**: Added endpoints for user registration, login, and profile retrieval using Django Rest Framework and dj-rest-auth.

## Running the Application Locally

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone hhttps://github.com/abhisheksinha567/django-black-dashboard.git
    cd your-repo-name
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Run the server**:
    ```bash
    python manage.py runserver
    ```

6. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Dockerization and Running with Docker

To build and run the Docker container for this project, follow these steps:

1. **Build the Docker image**:
    ```bash
    docker build -t my-django-app .
    ```

2. **Run the Docker container**:
    ```bash
    docker run -p 8000:8000 my-django-app
    ```

3. **Access the application**:
    Open your web browser and go to `http://127.0.0.1:8000/`.

## Deployment to Google Cloud Run

Since AWS Lambda setup is not complete, you can use Google Cloud Run for deployment. Follow these steps:

1. **Install Google Cloud SDK**:
    ```bash
    brew install --cask google-cloud-sdk
    ```

2. **Initialize Google Cloud SDK**:
    ```bash
    gcloud init
    ```

3. **Authenticate with Docker**:
    ```bash
    gcloud auth configure-docker
    ```

4. **Build and push Docker image**:
    ```bash
    docker build -t gcr.io/your-project-id/your-app-name .
    docker push gcr.io/your-project-id/your-app-name
    ```

5. **Deploy to Cloud Run**:
    ```bash
    gcloud run deploy your-app-name --image gcr.io/your-project-id/your-app-name --platform managed
    ```

## External Tools and Resources Used

- Django Rest Framework: For creating RESTful APIs.
- dj-rest-auth: For user authentication.
- Docker: For containerizing the application.
- Google Cloud SDK: For deploying to Google Cloud Run.

## Video Demonstration

[Link to your video demonstration]

---

## Pushing the Code to GitHub

1. **Initialize the Git repository** (if not already initialized):
    ```bash
    git init
    ```

2. **Add the files to the repository**:
    ```bash
    git add .
    ```

3. **Commit the changes**:
    ```bash
    git commit -m "Initial commit with added functionality and Dockerization"
    ```

4. **Add the remote repository**:
    ```bash
    git remote add origin https://github.com/your-github-username/your-repo-name.git
    ```

5. **Push the changes to GitHub**:
    ```bash
    git push -u origin master
    ```

# Django Project with Enhanced Functionalities

## Project Overview

This project is an open-source Django application with added functionalities, including a user authentication system, item management, and search capabilities. The project has been containerized using Docker, and is intended to be deployed on AWS Lambda. However, due to banking issues, deployment to AWS Lambda could not be completed. The application is demonstrated locally in the browser.

## Table of Contents

1. [Project Setup](#project-setup)
2. [Added Functionalities](#added-functionalities)
3. [Docker Containerization](#docker-containerization)
4. [Deployment](#deployment)
5. [API Endpoints](#api-endpoints)
6. [Running the Application](#running-the-application)
7. [Known Issues](#known-issues)

## Project Setup

### Prerequisites

- Python 3.10+
- Django 4.1.2
- Docker
- Google Cloud SDK (optional for deployment demonstration)

### Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/abhisheksinha567/django-black-dashboard.git
    cd your-forked-repository
    ```

2. **Create and Activate a Virtual Environment:**

    ```bash
    python -m venv env
    source env/bin/activate
    ```

3. **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Apply Migrations:**

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser:**

    ```bash
    python manage.py createsuperuser
    ```

## Added Functionalities

### 1. User Authentication

- **Registration Endpoint:**
  
  ```http
  POST /api/auth/registration/
Login Endpoint:

http
Copy code
POST /api/auth/login/
Logout Endpoint:

http
Copy code
POST /api/auth/logout/
2. Item Management
Add New Item (POST Request):

http
Copy code
POST /api/items/
Example Payload:

json
Copy code
{
  "name": "New Item",
  "description": "Description of the new item."
}
Retrieve All Items (GET Request):

http
Copy code
GET /api/items/
Retrieve a Single Item (GET Request):

http
Copy code
GET /api/items/<item_id>/
Update an Item (PUT Request):

http
Copy code
PUT /api/items/<item_id>/
Example Payload:

json
Copy code
{
  "name": "Updated Item",
  "description": "Updated description."
}
Delete an Item (DELETE Request):

http
Copy code
DELETE /api/items/<item_id>/
3. Search Functionality (if implemented)
Search Items:

http
Copy code
GET /api/items/search/?q=search_term
Docker Containerization
Dockerfile
A Dockerfile has been created to containerize the Django application. Here is the content:

dockerfile
Copy code
# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the app runs on
EXPOSE 8000

# Define the command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
Building and Running the Docker Container
Build the Docker Image:

bash
Copy code
docker build -t my-django-app .
Run the Docker Container:

bash
Copy code
docker run -p 8000:8000 my-django-app
Deployment
AWS Lambda Deployment
Deployment to AWS Lambda is currently not available due to banking issues. As an alternative, the application is demonstrated running locally.

Running the Application
Start the Django Development Server:

bash
Copy code
python manage.py runserver
Access the Application in a Browser:

Admin Interface:

http
Copy code
http://127.0.0.1:8000/admin/
API Endpoints:

Refer to the API Endpoints section for available endpoints.

Known Issues
django_browser_reload Middleware: The django_browser_reload middleware may cause issues if not properly configured. Ensure the django_browser_reload package is correctly installed and configured in your Django settings.
Conclusion
This project demonstrates the ability to work with existing Django applications, implement new features, and containerize them using Docker. Although AWS Lambda deployment is not available, the application runs successfully locally and showcases the added functionalities.

Feel free to explore and test the application using the provided endpoints.

For any questions or issues, please refer to the Django Documentation or reach out to me directly.
