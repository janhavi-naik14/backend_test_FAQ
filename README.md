# backend_test - FAQ API

This project provides an API for managing and querying FAQs (Frequently Asked Questions). It supports multilingual capabilities (English, Hindi, and Bengali).

## Table of Contents

- [Installation](#installation)
- [API Usage](#api-usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

Follow the steps below to set up the development environment and run the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/backend_test.git
   cd backend_test
Create a virtual environment (optional but recommended):

bash
Copy
Edit
python3 -m venv venv
Activate the virtual environment:

For macOS/Linux:
bash
Copy
Edit
source venv/bin/activate
For Windows:
bash
Copy
Edit
.\venv\Scripts\activate
Install the required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the application:

bash
Copy
Edit
python manage.py runserver
Your application should now be running locally at http://127.0.0.1:8000.

API Usage
The project exposes a simple API to retrieve FAQs. You can access the following endpoints:

Available Endpoints
GET /api/faq/: Fetch the list of FAQs in the default language (English).
GET /api/?lang=hi: Fetch the list of FAQs in Hindi.
GET /api/?lang=bn: Fetch the list of FAQs in Bengali.
API Examples
Fetch FAQ List (English)
bash
Copy
Edit
curl http://127.0.0.1:8000/api/faq/
Fetch FAQ List (Hindi)
bash
Copy
Edit
curl http://127.0.0.1:8000/api/?lang=hi
Fetch FAQ List (Bengali)
bash
Copy
Edit
curl http://127.0.0.1:8000/api/?lang=bn
Testing
To run tests for the project:

Ensure the virtual environment is activated.
Run the following command to execute tests:
bash
Copy
Edit
python manage.py test
The tests for the project are located in the tests.py file, and running the above command will execute all tests.

Contributing
We welcome contributions to this project! If you'd like to contribute, please follow these steps:

Fork the repository.
Clone your forked repository locally.
Create a new branch for your feature (git checkout -b feature-name).
Make your changes and commit them (git commit -am 'Add feature description').
Push the branch (git push origin feature-name).
Create a pull request from your branch to the main repository.
Please ensure all tests pass before submitting your pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

csharp
Copy
Edit

You can now copy and paste this directly into your `README.md` file.
