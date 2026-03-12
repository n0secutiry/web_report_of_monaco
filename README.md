# Monaco 2018 Racing Web Report API

This is a RESTful API that provides detailed reports and statistics for the 2018 Monaco Formula 1 qualifying race. 

The application processes raw start and finish time data to calculate the exact lap time for each driver. It allows users to view race rankings, sort results, and retrieve specific information about drivers, their teams, and vehicles.

## Features
* Retrieve a complete list of drivers sorted by their lap times (ascending or descending).
* Access detailed profiles of individual drivers, including their car models and team names.
* View interactive API documentation via Swagger UI.
* Database integration for data storage and querying.

## Tech Stack
* Python 3
* Flask
* Flask-RESTful
* SQLAlchemy
* Flasgger

## Installation & Setup

1. Clone the repository:
```bash
git clone https://github.com/n0secutiry/web_report_of_monaco.git
cd monaco-2018-report
```

2. Create venv and download requirements
```bash
python -m venv venv
venv/scripts/activate
pip intall -r requirements.txt
```

3. Run server
```bash
python run.py
```
