# How to deploy on `Render`
# Django Black Dashboard Project

This project is a modified version of the open-source Django Black Dashboard. The modifications include the addition of search functionality and API endpoints for user authentication.

## Added Functionality

1. **Search Functionality**: Implemented a search feature that allows users to search items in the database by name.
2. **User Authentication API**: Added endpoints for user registration, login, and profile retrieval using Django Rest Framework and dj-rest-auth.

## Running the Application Locally

To run this project locally, follow these steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-github-username/your-repo-name.git
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

Replace `your-github-username` and `your-repo-name` with your actual GitHub username and repository name. 

Feel free to adjust the `README.md` content to better fit your specific project and changes. Let me know if you need further assistance with any of the steps!
