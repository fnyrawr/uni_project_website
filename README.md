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
- [x] Implement Blog entry functionalities `@Florian`
- [ ] Implement Leaderboard functionalities
  - [x] Page (POST and GET) `@Florian`
  - [x] Creating Score entries in Unity `@Adrian`
  - [ ] Sending data between Unity and Page `@Adrian`
  - [x] Sorting data in Leaderboard `@Florian`
  - [x] Admins can delete entries `@Florian`
- [ ] Implement Adminuser views
  - [X] View users 
  - [ ] Edit profile
  - [ ] View own blogposts
- [ ] Fill page with contents `@Florian (Design and Page)` `@Zainab (Text)`
- [ ] Test website functionalities `@everyone`

##### Needed commands to get page running
- pip install django
- pip install djangorestframework
- pip install Pillow (needed for profile pictures)
- python -m venv ./venv (creating virtual environment)
- venv\Scripts\activate
- python manage.py runserver

###### after changes you may run
- python manage.py makemigrations
- python manage.py migrate
