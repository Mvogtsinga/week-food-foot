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
 4. [ Features Left to Implement ](#features-left-to-implement)  
 5. [ Technology used ](#technology-used) 
 6. [ Testing ](#testing)  
 7. [ Bugs ](#known-bugs)  
 8. [ Deployment](#deployment)
 9. [ Resources ](#resources)  
 10. [ Credits and acknowledgements ](#credits-and-acknowledgements)


# UX
## Database planning 
![IMG-20240325-WA0030](https://github.com/Mvogtsinga/weekendfoodfoot/assets/152321059/38c54b06-f9d6-456d-b70a-154f4c40fab0)


## UX design


## Overview
## Design
Initial design planing
The first design of this project was to choice and appeling picture for the homepage and login features prototypes.
![home wff](https://github.com/Mvogtsinga/weekendfoodfoot/assets/152321059/d74240f8-4a5d-4364-b24d-fd2b182d3c6e)

![userlogin wff](https://github.com/Mvogtsinga/weekendfoodfoot/assets/152321059/8491c30e-b6b0-4453-a31b-d654bcfa7ac2)

![signup wff](https://github.com/Mvogtsinga/weekendfoodfoot/assets/152321059/0ef76d89-4f78-4716-bd44-3f61507c8e02)"

![reservation wff](https://github.com/Mvogtsinga/weekendfoodfoot/assets/152321059/b9f69e95-6988-4c44-b204-7e90d4b4f884)"

![menu wff](https://github.com/Mvogtsinga/weekendfoodfoot/assets/152321059/aaf7196f-a355-4eea-adc7-ba78e2ba61f6)"

# Agile Development
## Overview

I started this project alongside GitHub Projects with intention of planning and tracking the workflow to manage the expected workload. After setting out the epics for my project I broke them down into a set of user stories and smaller tasks, to help me monitor my progress and finish the website in time. Outside of user stories I also included a separate issues for creating each module of this README file, as I simply found it more motivating this way. To see the project's Kanban page please click [here](https://github.com/users/TulaUnogi/projects/3/views/1).

## User Stories

Initial stage of the project included stepping into the shoes of the future User. I thought about the features and functionality I would expect from the first use of the website and based on that I created a set of 12 User Stories. I labelled 10 of them as mandatory, as they provide the core functionality and source of important informations for the User. The remaining 2 Stories are labelled as NINTH- Nice To Have, Not Important, as they provide some improvements, but are not necessary for the User to enjoy the website's base functionality. 

The User Stories include the acceptance criteria and are broken down into smaller, bite- size tasks that I would tick on completion, so I could easily track my progress. During the coding session I would record the encountered bugs, issues and solutions related to the Story in the comments below. Once all of the tasks in the Issue are completed I would move the User Story form "In progress" to "Completed" card im my project's Kanban.

> List of Mandatory User Stories

1. [USER STORY: DEPLOYMENT](https://github.com/TulaUnogi/cat-beans-cafe/issues/16)
2. [USER STORY: ADMIN PANEL](https://github.com/TulaUnogi/cat-beans-cafe/issues/17)
3. [USER STORY: CREATE AN ACCOUNT](https://github.com/TulaUnogi/cat-beans-cafe/issues/18)
4. [USER STORY: EDITING PROFILE](https://github.com/TulaUnogi/cat-beans-cafe/issues/22)
5. [USER STORY: DELETING PROFILE](https://github.com/TulaUnogi/cat-beans-cafe/issues/23)
6. [USER STORY: TABLE BOOKING](https://github.com/TulaUnogi/cat-beans-cafe/issues/21)
7. [USER STORY: NAVBAR AND FOOTER](https://github.com/TulaUnogi/cat-beans-cafe/issues/20)
8. [USER STORY: ABOUT US](https://github.com/TulaUnogi/cat-beans-cafe/issues/19)
9. [USER STORY: MENU](https://github.com/TulaUnogi/cat-beans-cafe/issues/26)
10. [USER STORY: GOOGLE MAPS](https://github.com/TulaUnogi/cat-beans-cafe/issues/25)

> NINTH: Not Important, Nice To Have

11. [USER STORY: CAT CAROUSEL](https://github.com/TulaUnogi/cat-beans-cafe/issues/24)
12. [USER STORY: BOOKING CANCELLATION](https://github.com/TulaUnogi/cat-beans-cafe/issues/27)

##### [ Back to table of contents ](#table-of-contents)


# features-implemented

### Navbar and Footer:

- Navbar and footer are present on every page
- Navbar's content changes depending on user authentication, allowing access to profile and user bookings
- Footer includes café's opening times, social links and address to provide the necessary informations in an easy way.

### Index page:

- The homepage provides the links to booking and about us page.
- It can be accessed without signing in.

### About Us page:

- Main page includes a short information about the café and set of 4 cards with pictures and description.
- Each of the card includes the button, that triggers a fullscreen modal.
- The modals contain informations about the menu, contact details with embedded google maps, link to booking page and gallery with cat pictures (cat carousel).
- About Us page can be accessed without signing in.

### Authentication and profile management:

- User can sign up to create their profile 
- User can log in to their account and update their informations
- User can delete their account alltogether with all their data
- The authentication process is safe thanks to [Django-AllAuth](https://github.com/pennersr/django-allauth) and csrf tokens.

### Bookings:

- User can pass their data to create a booking.
- User can edit their selected booking.
- Currently the initial version of booking cancellation view has not been fully implemented. I decided to implement an automatic delete_booking view, that allows User to quickly remove their booking from the system.

### Responsiveness:

- Website is responsive thanks to Bootstrap and media queries applied.
- There's a hamburger navbar on small devices.

##### [ Back to table of contents ](#table-of-contents)

# feature left to implement

Features Left to Implement

- [USER STORY: BOOKING CANCELLATION] (https://wff-ba2fd89f325f.herokuapp.com/account/) - As I've mentioned the initial version of this model is left for now since customer can currently fully delete their booking. 

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

I was testing for responsiveness on an Ideapad laptop and a Samsung Galaxy A5 using the most up to date versions of Google Chrome, Mozilla Firefox and Opera versions. For more detailed testing I was using Google DevTools.

> Index page:

![Index page](static/images/readme-images/responsive-index.png)


> About Us page:

![Index page](static/images/readme-images/responsive-about.png)


> Sign Up page:

![Index page](static/images/readme-images/responsive-signup.png)


> Sign In page:

![Index page](static/images/readme-images/responsive-sign-in.png)



### Manual testing







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

- Images : Unsplash
- templates: code institute
  
  > Pictures

- [Chef_team](https://unsplash.com/photos/man-in-black-t-shirt-holding-stainless-steel-bowl-eBmyH7oO5wY) by <b>Sebastian Coman Photography </b> on Unsplash
- [Food_WFF](https://unsplash.com/photos/grilled-fish-dish-vBOxsZrfiCw) by <b>Mgg Vitchakorn</b> on Unsplash
- [Restaurant_WFF](https://unsplash.com/photos/black-pendant-lamp-turned-on-oMTlhdFUhdI) by <b>yMaria Orlova</b> on Unsplash
- [Servant](https://unsplash.com/photos/man-in-black-t-shirt-holding-stainless-steel-bowl-eBmyH7oO5wY) by <b>Stefan Schauberger</b> on Unsplash
- [Order_WFF](https://unsplash.com/photos/dish-on-white-ceramic-plate-N_Y88TWmGwA) by <b>Jay Wennington</b> on Unsplash

- Cat carousel pictures:
  1. [Fluffy black cat](https://pixabay.com/photos/couch-cat-pet-feline-animal-6654015/) by <b>Spike Summers</b> on Pixabay 
  2. [Calico cat](https://www.pexels.com/photo/calico-cat-1359300/) by <b>Cats Coming</b> on Pexels
  3. [Orange tabby cat](https://www.pexels.com/photo/adorable-animal-cat-close-up-208930/) by <b>Pixabay</b> on Pexels
  4. [Cat with a mouse toy](https://www.pexels.com/photo/cat-with-a-mouse-toy-3216568/) by <b>lil artsy</b> on Pexels
  5. [Two cosy tabby cats](https://www.pexels.com/photo/two-tabby-kittens-lying-down-1787414/) by <b>Cats Comin</b> on Pexels
  6. [Little kitten](https://www.pexels.com/photo/close-up-photo-of-orange-tabby-cat-2581153/) by <b>samer daboul</b> on Pexels
  7. [Christmas kitten](https://www.pexels.com/photo/close-up-photography-of-white-cat-besides-christmas-lights-735423/) by <b>Eftodii Aurelia</b> on Pexels


## Acknowledgements

- I would like to thank my Code Institute mentor for their support throughout the development of this project.
- I would like to thank the Code Institute Slack community for the moral support; it kept me going during periods of self doubt and imposter syndrome.
- I would like to thank my family, for believing in me, and allowing me to make this transition into software development.
- I would like to thank the Bootcamp crew, for supporting me in my career development change towards becoming a software developer.


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

##### [ Back to table of contents ](#table-of-contents)


