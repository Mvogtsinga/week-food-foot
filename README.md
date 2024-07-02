![logowwf](https://github.com/Mvogtsinga/weekendfoodfoot/assets/152321059/0afe3128-79f2-43a7-9e0c-38750440edb7)

# Welcome to WEEKENDFOODFOOT Restaurant <br>
### A restaurant website <br>

A responsive,restaurant website with registration and table booking system with different formats for customers.create as a final Project Portfolio during the Full stack Software Developer-Skills Bootcamp at Code Institute.
[Link to the live site here](https://https://week-food-foot-d23c617ce819.herokuapp.com/)

-By Aubin KOENIGSSOHN-

## Table of contents 

 1. [ UX ](#ux)
 2. [ Agile Development ](#agile-development)
 3. [ Features implemented ](#features-implemented)
 4. [ Technology used ](#technology-used)
 5. [ Testing ](#testing)
 6. [   Bugs ](#known-bugs)
 7. [  Deployment](#deployment)
 8. [ Resources ](#resources)
 9. [ Credits and acknowledgements ](#credits-and-acknowledgements)


# UX
## Database planning 
### Data Structure
![Data_Schema_Planing_WFF](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/40ead94d-67b9-4b91-aefb-0824294f15b5)
- I used a lucidchart to have a clear orientation about the structure of the database.
- The diagram is a guide to show the types and relationships between data stored.

### Data models
> UserProfile model

- During the evolution of the project the data models looks as follows::

| Key | Name | Field |
|--|--|--|
| PrimaryKey | client | OnetoOneField  |
| x | user_name | Charfield |
| x | first_name | Charfield |
| x | last_name | Charfield |
| x | email | Emailfield |

---

> Reservation's model

| Key | Name | Field |
|--|--|--|
| ForeignKey | client_reservation | ForeignKey  |
| x | reservation_day | DateField |
| x | reservatin_time | CharField |
| x | tables_option | CharField |
| x | table_reservation  | TextField |
| x | date_reservation | DateTimeField |
| x | confirmation | IntegerField |
| x | slug | AutoSlugField |

---

## UX design


### Overview

#### Design

> Initial design planning

Before starting to code, I chose to take some time to imagine the design of the home page of a restaurant and a Logo.
I wanted my website to look professional and modern. playing with somes colours like yellow, black, white and orange seems perfect for my project.
![Home_WFF](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/f8f7c0be-e463-4070-8592-48edcea2a137)

> Homepage

![Home_WFF](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/78d9f5a2-2f6d-4e12-bef1-b0f335d10bab)

> Sign up_page

![Sign_Up_WFF](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/fc4ba4c1-b7f1-4b85-a1bc-5dfb272c1a2c)

> UserLogin_page

![UserLoginPortal_sWFF](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/5d3eadc6-f9dd-4b61-83bc-9ff153d764f1)

>Menu_page

![Menu_sWFF](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/92fd112d-ce6c-4a3c-930a-0cc656c305f9)

> Reserves_table_page

![Services_sWFF](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/8cf3cec7-9d73-42db-a369-4f3ce83df84a)

> Admin_page

![Admin_page](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/3ee00cee-aafd-4f04-a441-79d8491c8fcd)


#### Site User

- Priority for someone in the restaurant area
- A football's fan looking for a place to enjoy footballs game and food
- someone who prefers to arrange their reservations online rather than over person or phone
  
#### Goals for the website

- To allow customer to see the menu before visiting the restaurant
- To allow customer to plan and book a table in advance
- To safely store the reservations data and make it available for the superuser to approve or decline it in an easy way

### Wireframes

I used the wireframe [Balsamiq](https://www.balsamiq.com) to have a clear view about the futur website as next stage of UX design planning.I wanted to have a realistic overview of my future website and make it easy for the user to navigate throughout the different pages.I plan to build the website like this:

> Login page
![Login_wireframe](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/a2a425be-a004-406e-8a56-a2cf19317e50)

> Sign_Up page
![Sign_up_Formular_wiref](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/1ac92b0a-9fd0-42a3-81f1-98f1a4d3dd12)

> Home page
![menu_food_page_wireframe](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/c63423e6-38a2-4dad-b826-2ce48bd20667)

> Reserve_table page
![reserve_table_page_wireframe](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/714aa37d-ad8c-48f0-bbd4-973e24b7199b)

> Menu_foods page
![menu_food_page_wireframe](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/79928812-54a6-48fb-ada1-b4a18d463d75)

> Account page
![account_page_wireframe](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/fd5dccf8-3817-4b8c-b642-f8a8610d937a)


# Agile Development
## Overview

I initiated this project in conjunction with GitHub Projects with the goal of organizing and monitoring the workflow to effectively handle the anticipated workload. Once I outlined the epics for my project, I further divided them into a series of user stories and smaller tasks to facilitate tracking my advancement and completing the website on schedule. In addition to user stories, I created individual issues for developing each module of this README file, as I found this approach to be more inspiring. To view the project's Kanban page, please click [here](https://github.com/users/Mvogtsinga/projects/9).

## User Stories

Initial stage of the project included stepping into the shoes of the future User. I thought about the features and functionality I would expect from the first use of the website and based on that I created a set of 8 User Stories. I labelled it  as important, as they provide the core functionality and source of essential informations for the User.base functionality. 

The User Stories include the acceptance criteria and are broken down into smaller, bite- size tasks that I would tick on completion, so I could easily track my progress. During the coding session I would record the encountered bugs, issues and solutions related to the Story in the comments below. Once all of the tasks in the Issue are completed I would move the User Story form "In progress" to "Completed" card im my project's Kanban.


> List of Important User Stories

1. [USER STORY: LOGIN](https://github.com/users/Mvogtsinga/projects/9?pane=issue&itemId=69389784)
2. [USER STORY: SUPERUSER PANEL](https://github.com/Mvogtsinga/week-food-foot/issues/2)
3. [USER STORY: CREATE AN ACCOUNT](https://github.com/users/Mvogtsinga/projects/9?pane=issue&itemId=69395450)
4. [USER STORY: RESERVATION CANCELLATION](https://github.com/users/Mvogtsinga/projects/9?pane=issue&itemId=69391821)
5. [USER STORY: BOOK A TABLE](https://github.com/users/Mvogtsinga/projects/9?pane=issue&itemId=69394094)
6. [USER STORY: NAVBAR AND FOOTER](https://github.com/Mvogtsinga/week-food-foot/issues/1)
7.  [USER STORY: MENU](https://github.com/Mvogtsinga/week-food-foot/issues/3)
8.  [ USER STORY: DEPLOYMENT](https://github.com/users/Mvogtsinga/projects/9?pane=issue&itemId=69402617)


##### [ Back to table of contents ](#table-of-contents)


# features-implemented

- [USER STORY: LOGIN](https://github.com/users/Mvogtsinga/projects/9?pane=issue&itemId=69389784)
- [USER STORY: SUPERUSER PANEL](https://github.com/Mvogtsinga/week-food-foot/issues/2)
- [USER STORY: CREATE AN ACCOUNT](https://github.com/users/Mvogtsinga/projects/9?pane=issue&itemId=69395450)
- [USER STORY: RESERVATION CANCELLATION](https://github.com/users/Mvogtsinga/projects/9?pane=issue&itemId=69391821)
- [USER STORY: BOOK A TABLE](https://github.com/users/Mvogtsinga/projects/9?pane=issue&itemId=69394094)
- [USER STORY: NAVBAR AND FOOTER](https://github.com/Mvogtsinga/week-food-foot/issues/1)
- [USER STORY: MENU](https://github.com/Mvogtsinga/week-food-foot/issues/3)
- [ USER STORY: DEPLOYMENT](https://github.com/users/Mvogtsinga/projects/9?pane=issue&itemId=69402617)


### Navbar and Footer:

- Navbar and footer are present on every page
- Navbar's content changes depending on user authentication, allowing access to user reservations
- Footer includes restaurants location, social links,sitemap, reservations buttonm and a copyright notice to provide the necessary informations in a simpler way.

### Index page:

- The homepage provides the links to reservation and restaurant page.
- It can  be accessed without signing in.

### Home page:

- Main page includes a short information about the restaurant  set of  cards with pictures and description.
- Each of the card includes the button, that triggers a fullscreen modal.
- The modals contain informations about the menu, 
- Home page can be accessed with signing in.

### Authentication and profile management:

- User can sign up  
- User can log in to their account and update their informations
- User can delete their account alltogether with all their data
- The authentication process is safe thanks to [Django-AllAuth](https://github.com/pennersr/django-allauth) and csrf tokens.

### Reservations:

- User can pass their data to create a reservation.
- User can edit their selected reservation.

### Responsiveness:

- Website is responsive thanks to Bootstrap and media queries applied.
- There's a hamburger navbar on small devices.

##### [ Back to table of contents ](#table-of-contents)

# Technology used 

The site has been built with the following tech and tools:

- Html - for page structure
- CSS - for custom styling
- Python - for the backend
- Javascript - for timeout in messages
- Django - framework used to build this project
- Jinja - templating language rendering logic within html documents
- Bootstrap 5 - front end framework used by me alongside Django, helps with fast and efficient styling
- Heroku PostgreSQL - used as the database
- Font Awesome - for social media icons
- Google Fonts- currently only for the hero image font
- GitHub - for storing the code and for the projects Kanban
- Heroku - for hosting and deployement of this project
- Cloudinary - hosting the static files 
- Git - version control tool

##### [ Back to table of contents ](#table-of-contents)



# Testing

### Responsiveness

I was testing for responsiveness on an AsusVivoBook laptop, a iPhone 14 ProMax and a Samsung Galaxy A5 using the most up to date versions of Google Chrome and Mozilla versions. For more detailed testing I was using Google DevTools.

> Index page:
- AsusVivoBook and Samsung galaxy ![Login_responsiveness_Computer_phone](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/b010092c-42d6-47d0-a0b0-ebd40c12bf32)
- iPhone 14 ProMax ![Responsiveness_iPhoneProMax14_login](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/f833d28c-8063-4df5-84ad-30d8cd63fe0a)
- iPad air ![Lopgin_iPad air ](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/9360ee42-d564-4a8a-9eba-a94c427a8d7d)



> Contact page:

- ![Contact_responsiveness_Phone](https://github.com/Mvogtsinga/week-food-foot/assets/152321059/7b7bdea7-de37-4db5-a0d6-1e403e5a8b44)


> Sign Up page:

![Index page](static/images/readme-images/responsive-signup.png)


> Sign In page:

![Index page](static/images/readme-images/responsive-sign-in.png)



### Manual testing

#### Account Registration Tests
| Test |Result  |
|--|--|
| User can create account | Pass |
| Messages are displaying | Pass |
| Messages are dismissable by button | Pass |



---

#### User Navigation Tests

| Test | Result  |
|--|--|
| User can easily navigate to Reservation | Pass |
| User can access Home page| Pass|
| User access their account page|Pass|
| User can access the card content in Home|Pass|
| SuperUser can access admin page|Pass|



---

#### Account Authorisation Tests

| Test | Result  |
|--|--|
| Only Superuser can access admin page |Pass|
| Non authorised user can not book a table | Pass |
| Non authorised user won't access account page| Pass|



---

#### Reservations Tests

| Test |Result  |
|--|--|
|User can make a reservation | Pass |
|User can view all of their reservations | Pass |
|User can delete their reservation | Pass |
|User can edit reservation | Pass |
|User can make more than one reservation | Pass |
|User can delete their account | Pass |
|User can change their information | Pass |
|User can see the confirmation information | Pass |



---

#### Admin Tests

| Test |Result  |
|--|--|
|Items display correctly on front-end when updated / added |Pass|
|Admin can confirm or decline bookings |Pass|


##### [ Back to table of contents ](#table-of-contents)

---
 
# Known bugs 

- I observed one blue submit button- it is automatically generated by crispy forms and somehow the form settings did not applied to this button. It's a small bug of low priority for me at the current stage.
- There's small image clipping during the  transitions on smaller screens.
- No error message displaying when passing wrong login details
- The function that was supposed to prevent booking dates in the past is currently preventing nothing, unfortunately... You may be brave and try to trick the system into timetravelling, but Admin will always see what day the booking was made on anyway and won't accept such a silly tricks!


##### [ Back to table of contents ](#table-of-contents)

---

# Deployment

#### The deployment stage of the website should follow the steps below:

> Create the Heroku app

- Sign up / Log in to Heroku
- In Heroku Dashboard page select 'New' and then 'Create New App'
- Name a project - I decided on the week-food-foot (the app's name must be unique)
- Select EU as that was my region in the moment of creating the app
- Select "Create App"
- In the "Deploy" tab choose GitHub as the deployment method
- Connect your GitHub account/ find and connect your GitHub repository

> Set up enviroment variables

- In the Django app editor create env.py in the top level
- In env.py import os
- In env.py set up necessary enviroment variables:
  - add a secret key using: os.environ['SECRET_KEY'] = 'your secret key'
  - for the database variable the line should include os.environ['DATABASE_URL']= 'Paste the database link in here'
  - in settings.py replace value of SECRET_KEY variable with os.environ.get('SECRET_KEY')
  - in settings.py change the value of DATABASES variable to 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
- In Django app's settings.py on top of the file add:
```
from pathlib import Path
import os
import dj_database_url
if os.path.isfile('env.py'):
    import env
```
- Navigate to the "Settings" tab in Heroku.
- Open the "Config Vars" section and add DATABASE_URL as Key and the database link from app's env.py as Value
- Add SECRET_KEY for the Key value and the secret key value from env.py as the Value
- In the terminal migrate the models over to the new database connection
- In settings.py add the STATIC files settings as follows:
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
```
- Change the templates directory in settings.py to: TEMPLARES_DIR = os.path.join(BASE_DIR, 'templates')
- In TEMPLATES variable change the 'DIRS' key to look like this: 'DIRS': [TEMPLARES_DIR],
- Add Heroku to the ALLOWED_HOSTS list (the format will be your-app-name.herokuapp.com, you can copy it from the Domains section in Settings tab in your Heroku app)
- If you haven't done that up to this point, then create in your Django app's code editor new top level folders: static and templates
- Create a new file on the top level directory - Procfile, remembering to use a capital letter
- Within the Procfile add following:
```
web: guincorn PROJECT_NAME.wsgi
``` 
- In the terminal, add the changed files, commit and push to GitHub

> Heroku deployment

- In Heroku, navigate to the Deployment tab and deploy the branch manually 
- Heroku will display a build log- watch the build logs for any errors
- Once the build process is completed Heroku displays 'Your App Was Successfully Deployed' message and a link to the app to visit the live site


#### Forking the repository

By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository. You can do this with following steps:

- Log in to GitHub or create an account
- Enter this [repository link](https://github.com/Mvogtsinga/week-food-foot)
- Select "Fork" from the top of the repository
- A copy of the repository should now be created in your own repository

#### Create a clone of this repository

Creating a clone enables you to make a copy of the current version of this repository to run the project locally. To do this follow steps below:

- Navigate to https://github.com/Mvogtsinga/week-food-foot
- Click on the <>Code button at the top of the list of files
- Select the "HTTPS" option on the "Local" tab and copy the URL it provides to the clipboard
- Navigate to your code editor and in the terminal change the directory to your chosen location 
- Type "git clone" and paste the GitHub repository's link
- Press enter and git will clone the repository for you

##### [ Back to table of contents ](#table-of-contents)




# resources

-  [Code Institute Full Stack Development course materials](https://codeinstitute.net/global/full-stack-software-development-diploma/?sitelink=FullStackDiploma-IRL&utm_term=code+institute&utm_campaign=CI+-+IRL+-+Search+-+Brand&utm_source=adwords&utm_medium=ppc&hsa_acc=8983321581&hsa_cam=14304747355&hsa_grp=128775288209&hsa_ad=635725005315&hsa_src=g&hsa_tgt=kwd-319867646331&hsa_kw=code+institute&hsa_mt=e&hsa_net=adwords&hsa_ver=3&gad_source=1&gclid=Cj0KCQiAgqGrBhDtARIsAM5s0_l13h8fkiqZeHnw16zshbX6svuL8YJNrw6G-RFdq03RQybQXLSoZiYaAjGqEALw_wcB) 
- [Django documentation](https://www.djangoproject.com/)
- [Crispy forms docs](https://django-crispy-forms.readthedocs.io/en/latest/)
- [Bootstrap docs](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Stack overflow](https://stackoverflow.com/)
- [Slack](https://slack.com/intl/en-ie/)
  
##### [ Back to table of contents ](#table-of-contents)



# Credits and acknowledgements

## Credits

- Images : Unsplash, Freepik,Postermywall
- templates: code institute
  
  > Pictures

- [Chef_team](https://unsplash.com/photos/man-in-black-t-shirt-holding-stainless-steel-bowl-eBmyH7oO5wY) by <b>Sebastian Coman Photography </b> on Unsplash
- [Food_WFF](https://unsplash.com/photos/grilled-fish-dish-vBOxsZrfiCw) by <b>Mgg Vitchakorn</b> on Unsplash
- [Restaurant_WFF](https://unsplash.com/photos/black-pendant-lamp-turned-on-oMTlhdFUhdI) by <b>yMaria Orlova</b> on Unsplash
- [Servant](https://unsplash.com/photos/man-in-black-t-shirt-holding-stainless-steel-bowl-eBmyH7oO5wY) by <b>Stefan Schauberger</b> on Unsplash
- [Order_WFF](https://unsplash.com/photos/dish-on-white-ceramic-plate-N_Y88TWmGwA) by <b>Jay Wennington</b> on Unsplash
- [VIP](https://www.freepik.com/free-photo/restaurant-table-with-white-lace-table-cloth-blue-napkins_6317252.htm#fromView=search&page=1&position=26&uuid=a1c58395-9bb8-4675-81ba-f5068179abde) by <b>images</b> on Freepik
-  [Extra Famille](https://www.freepik.com/free-photo/modern-restaurant-with-various-places_7873940.htm#fromView=search&page=1&position=24&uuid=a1c58395-9bb8-4675-81ba-f5068179abde) by <b>image</b> on Freepik
-   [Couple](https://www.freepik.com/free-photo/view-beautifully-decorated-round-table-with-natural-fir-branch-candle-two-flutes-plates-against-classic-sofa-modern-apartment_10909128.htm#fromView=search&page=1&position=10&uuid=a1c58395-9bb8-4675-81ba-f5068179abde) by <b>image</b> on Freepik
-   [Chefs_Team](https://www.freepik.com/free-photo/close-up-chef-cooking-restaurant-kitchen_13273109.htm#fromView=search&page=1&position=2&uuid=c6b0e69d-0517-4c20-bdc0-674e6b168763) by <b> image</b> on Freepik
- [Menu_WFF](https://fr.postermywall.com/index.php/art/template/22ed5dc89be68d06ae5171599c95a1a9/restaurant-menu-design-template) by <b> image</b> on Postermywall
- [Chefs_Team](https://www.freepik.com/free-photo/close-up-chef-cooking-restaurant-kitchen_13273109.htm#fromView=search&page=1&position=2&uuid=c6b0e69d-0517-4c20-bdc0-674e6b168763) by <b> image</b> on Freepik
  
     
  > Template

[Code Institute](https://github.com/Code-Institute-Org/gitpod-full-template)


## Acknowledgements

- I would like to thank my Code Institute mentor for their support throughout the development of this project.
- I would like to thank the Code Institute Slack community for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my family, for believing in me, and allowing me to make this transition into software development.
- I would like to thank the Bootcamp crew, for supporting me in my career development change towards becoming a software developer.


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

##### [ Back to table of contents ](#table-of-contents)


