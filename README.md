### Informational website for the Semesterproject
##### ToDo
- [x] Create repository `@Florian`
- [x] Get base Django page running `@Florian`
- [x] Implement Login / Logout `@Florian`
- [x] Create base page design (styling) `@Florian`
- [x] Implement basic functionalities for
  - [x] About `@Florian`
  - [x] Download `@Florian`
  - [x] How to play `@Florian`
  - [x] Blog `@Florian`
  - [x] Leaderboard `@Florian`
  - [x] Questions `@Florian`
  - [x] Surveys `@Florian`
- [x] Implement Blog entry functionalities `@Florian`
- [x] Implement Leaderboard functionalities
  - [x] Page (POST and GET) `@Florian`
  - [x] Creating Score entries in Unity `@Adrian`
  - [x] Sending data between Unity and Page `@Adrian`
  - [x] Sorting data in Leaderboard `@Florian`
  - [x] Admins can delete entries `@Florian`
- [x] Implement Adminuser views
  - [x] View users `@Florian`
  - [x] View Questions `@Florian`
  - [x] View Surveys `@Florian`
    - [x] View Survey Entries `@Florian`
    - [x] View Survey average ratings `@Florian`
      - [x] Diagrams with matplotlib `@Florian`
    - [x] View only reviews `@Florian`
    - [x] View only wishes `@Florian`
- [x] Fill page with contents `@Florian`

##### Needed commands to get page running
- pip install django
- pip install djangorestframework
- pip install Pillow (needed for profile pictures)
- pip install matplotlib
- pip install seaborn
- python -m venv ./venv (creating virtual environment)
- venv\Scripts\activate
- python manage.py runserver

###### after changes you may run
- python manage.py makemigrations
- python manage.py migrate
