# Viitteidenhallinta <br>
[Backlog](https://docs.google.com/spreadsheets/d/1ynXuHdp9rR2oDtbcrOBZir3f2yQD1G3NdnaW-2tr-l4/edit?gid=1#gid=1)

[![GHA_workflow_badge](https://github.com/Hillomunkit/Viitteidenhallinta/workflows/CI/badge.svg)](https://github.com/Hillomunkit/Viitteidenhallinta/actions)
[![codecov](https://codecov.io/github/hillomunkit/viitteidenhallinta/graph/badge.svg?token=KGOW38AQWE)](https://codecov.io/github/hillomunkit/viitteidenhallinta)

[Testikattavuusraportti](https://drive.google.com/file/d/1mEzOYKXCvCLl9-yTmF254uXwnXeWGIkW/view?usp=drive_link)


# Startup Tutorial

The app needs a PostgreSQL-database to work, we recommend using https://aiven.io.

## Step 1: Create a `.env` File

In the root of the app, create a `.env` file with the following variables:
```
DATABASE_URL=postgresql://xxx
TEST_ENV=true
SECRET_KEY=random_string
```
If you use aiven for the database, you can find the DATABASE_URL as SERVICE_URI in aiven. Note that it has to be formatted postgresql:// not postgres://.

## Step 2: Install dependencies and start the virtual environment
To install dependencies, run
```poetry install``` .
To start the virtual environment run
```poetry shell``` .

## Step 3: Create the database
To create the database, run ```python src/db_helper.py``` in the virtual environment

## Step 4: Running the application
To start the application, run ```python src/index.py``` . By default the app runs in localhost:5001.

## Step 5: Using the Application

The app starts empty. To add references:

  1. Click on **Lisää uusi viite**.
  2. Fill in the forms for:
       * Book (Teos)
       * Author (Kirjoittanut)
       * Year (Painos vuosi)
        
        (All fields are mandatory.)

  Click on the **Create** button to submit.

After submitting a reference, you can:
  * View the list of created references.
  * Delete any reference you no longer need.

# Definition of Done
### 1. User Stories
* Each user story is well-written and understandable
* Each user story has well-defined acceptance criteria that are agreed on by the team and the customer
  
### 2. Code Quality
* All code changes pass succesfully on the CI-server
* The code follows a shared coding standard (e.g. linting rules)
* The code is readable and maintainable by all team members

### 3. Visibility
* The customer can at any time access and view the code and the test results via the CI-server

### 4. Testing
* Newly implemented features have corresponding automated tests
* The codes test coverage is at a reasonable level
