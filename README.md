# 🚀 Job Portal Application

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0%2B-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)

A comprehensive, full-featured **Job Portal** built with **Django** that bridges the gap between job seekers and recruiters. This platform offers a seamless experience for users to find their dream jobs and for recruiters to find the perfect talent.

---

## 🌟 Key Features

### 👨‍🎓 For Job Seekers (Students)
*   **User Registration & Login**: Secure signup and login functionality.
*   **Profile Management**: Update personal details, skills, education, and upload **Resume** & **Profile Photo**.
*   **Job Search**: Browse the latest job openings with detailed descriptions.
*   **Easy Application**: Apply to jobs with a single click, including a custom **Cover Letter**.
*   **Application Tracking**: Track the status of your applications (Pending, Accepted, Rejected) in real-time via the **"My Applications"** dashboard.
*   **Resume Preview**: View your uploaded resume directly from the dashboard.

### 👨‍💼 For Recruiters
*   **Recruiter Onboarding**: Sign up and wait for Admin approval to start posting jobs.
*   **Job Management**: Post new jobs, edit existing listings, and manage job details.
*   **Applicant Management**: View all applications for a specific job.
*   **Candidate Review**: View candidate profiles and resumes.
*   **Status Updates**: Accept or Reject applications with a simple click.
*   **Company Branding**: Upload and manage company logos.

### 🛡️ For Administrators
*   **Dashboard**: Overview of total users, recruiters, and jobs.
*   **User Management**: View and delete user accounts.
*   **Recruiter Approval**: Review pending recruiter registrations and Approve/Reject them.
*   **System Control**: Full control over the platform's data.

---

## 🛠️ Tech Stack

*   **Backend**: Django (Python)
*   **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
*   **Database**: SQLite (Development) / PostgreSQL (Production ready)
*   **Static Files**: WhiteNoise
*   **Deployment**: Ready for Render / Heroku

---

## 📸 Screenshots

| Home Page | Job List |
|:---:|:---:|
| *(Add screenshot here)* | *(Add screenshot here)* |

| Application Form | Recruiter Dashboard |
|:---:|:---:|
| *(Add screenshot here)* | *(Add screenshot here)* |

---

## 🚀 Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites
*   Python 3.x installed
*   Git installed

### Installation

1.  **Clone the repository**
    ```bash
    git clone https://github.com/yourusername/Job-Portal-Application.git
    cd Job-Portal-Application
    ```

2.  **Create a Virtual Environment**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Migrations**
    ```bash
    python manage.py migrate
    ```

5.  **Create a Superuser (Admin)**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the Server**
    ```bash
    python manage.py runserver
    ```

7.  **Access the App**
    *   Open your browser and go to `http://127.0.0.1:8000/`

---

## ☁️ Deployment

This project is configured for easy deployment on platforms like **Render**.

1.  Push your code to GitHub.
2.  Create a new Web Service on Render.
3.  Connect your repository.
4.  Use the following commands:
    *   **Build Command**: `pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate`
    *   **Start Command**: `gunicorn jobportal.wsgi`

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### 📬 Contact

If you have any questions or suggestions, feel free to reach out!

*   **Email**: info@jobportal.com
*   **GitHub**: [Your Profile](https://github.com/yourusername)
