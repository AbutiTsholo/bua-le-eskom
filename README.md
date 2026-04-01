# Bua le Eskom 

**Bua le Eskom** (meaning "Speak to Eskom" in Setswana) is a community-centred 
electricity fault reporting web application designed for residents of Mahikeng 
and surrounding villages in the North West Province of South Africa.

## About the Project

This project was developed as part of the NHCI63110 Human-Computer Interaction 
assignment at Sol Plaatje University. It addresses a real service delivery 
challenge — residents in Mahikeng frequently experience electricity outages but 
have no reliable way to report faults, track resolution progress, or receive 
advance warning of planned outages.

## The Problem

Existing platforms like the MyEskom Customer App are unreliable, inaccessible 
to basic phone users, and provide vague feedback. This leaves community members 
like students, teachers, and small business owners without a dependable channel 
to communicate with Eskom.

## The Solution

Bua le Eskom provides:
-  Simple fault reporting through a guided step-by-step form
-  Real-time outage notifications (push alerts for smartphones, SMS for basic phones)
-  A community fault map showing reported faults in the user's area
-  Plain-language fault tracking: Received → Assigned → In progress → Resolved
-  An inclusive design supporting users of all ages and digital literacy levels

## Built With

- Python 3.12
- Django 5.x
- HTML & CSS
- SQLite (default Django database)

## Project Structure
```
bua_le_eskom/
├── bua_le_eskom/        # Main project settings and URLs
│   ├── settings.py
│   ├── urls.py
├── reports/             # App 1 — fault reporting and home screen
│   ├── views.py
│   └── templates/
│       └── reports/
│           ├── home.html
│           └── report_fault.html
├── notifications/       # App 2 — outage notifications
│   ├── views.py
│   └── templates/
│       └── notifications/
│           └── notifications.html
├── manage.py
└── README.md
```

## How to Run Locally

1. Clone the repository:
```
git clone https://github.com/AbutiTsholo/bua-le-eskom.git
cd bua-le-eskom
```

2. Create and activate a virtual environment:
```
python -m venv venv
venv\Scripts\activate
```

3. Install Django:
```
pip install django
```

4. Run migrations:
```
python manage.py migrate
```

5. Start the development server:
```
python manage.py runserver
```

6. Open your browser and go to:
- Home screen: http://127.0.0.1:8000
- Report a Fault: http://127.0.0.1:8000/report/
- Notifications: http://127.0.0.1:8000/notifications/

## Designed For

- **Keitumetse** — a university student who needs reliable outage warnings 
  to plan her online studies
- **Mrs Diphoko** — a 52-year-old small business owner in Goedgevonden who 
  needs a simple, accessible way to report faults from a basic phone

## Academic Context

- **Module:** Human-Computer Interaction (NHCI63110)
- **Institution:** Sol Plaatje University
- **Assignment:** Chapters 1 & 2 — Interaction Design Lifecycle

## Author

AbutiTsholo — Sol Plaatje University
