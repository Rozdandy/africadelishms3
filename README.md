<img src="static/testing/test.png">


### **Website links:** 

*my github link*: [Rozdandy](https://github.com/Rozdandy/africadelishms3)


*Website Link*:

[Afric & delish](https://afric-delish.herokuapp.com/)

 There are about 55 countries on the African continent with a population estimated of 1.3 billion. Inspite of the numerous diverse cultures and ethnicities, the African cuisine or recipes is the least pronounced one among other continents of the world. For instance, here in the Netherlands, the African shops and restaurants that sell her recipes are very few in comparison to the asian continents. Does it mean other continents are not very aware of the African uncountable, tasty, relish, healthy, and energtic African recipes? In other instances, due to the diverse cultures and ethnicities, many indegenous African people are not aware of the various food recipes that available to them from other groups.

Therefore, Afric & delish is an online foodbook where users can surf other African recipes, able to register and also submit their country's cuisine. Afric & delish is a recipe website for people who love to explore continental dishes right in their homes. It avail the opportunity for gourmets and epicures to search for tasty, and palatable different African recipes to prepare for their maximum enjoyment. The concept of the foodbook would allow users to explore the available menus, create theirs, edit or update them and also delete them if they are not needed again. The concept of the   CREATE, READ, UPDATE and DELETE (CRUD) are the crux of the lecture for Milestone three Project at Code Institute, which this project would be built upon.


# **UX (USER EXPERIENCE)**

## Project objectives

This milestone project is a Data Centric Development module of [Code Institute](https://courses.codeinstitute.net/program/FullstackWebDeveloper)  classes. The aim is to "build an application that allow users to brows, store and access African recipes", using the CRUD operations.
In order to demonstrate these skills, I have decided to build this Afric & delish website, where Africans could perform the CRUD operations in order to furnish the site with different cuisnes in their countries for other people to emulates the methodologies of the same recipe.


## User stories

As a user, I would like to:
 

 *  view the site in any type of devices (mobile, tablet, desktop).
 *  view all recipes as a visitor.
 *  register to be a member and a regular user.
 *  be able to log in after registering
 *  view my own profile.
 *  add my recipes.
 *  see instructions on how to add a recipe.
 *  edit or update my recipes.
 *  delete my recipes that are not needed again.
 *  be able to log out.
 *  be able to search for recipes by names or description.
 *  see all the different categories of the recipes.
 *  know the particular African country which the recipe belongs to.
 *  recieve feedback if scuccessfully performed any of the CRUD operations.
 *  recieve an error message for perform the activities that is not within the scope of the website or there is an issue with database.


#### *Admin Objectives:*

In addition to the aforementioned user objectives above, as an Admin, i would like:

 *  be able add new categories and recipes.
 *  edit categories and recipes, in order to update them.
 *  delete categories, and recipes, in order to regulate and coordinates them.

### Developer objectives

 As a developer, to be able to demonstrate learnt skills in terms of:

 * providing a simple platform where users could perform CRUD operations.
 * good use of Jinja templating, Python, non-relational database MongoDb
 * good use materialize library combine with JavaScript knowledge.
 * how to make the website lives by deploying to Heroku.


## Design

The concept behind this site is just to enable individual culture and nations across Africa to showcase the various meal recipes in their countries for other people to reciprocate the methodologies. 

#### Fonts

[Google Fonts!](https://fonts.google.com/) Two main fonts were used for the whole sites:

* Supermercado for the body with fall back on san serif.
* Langar for the headers with fall back on san serif.


#### **Colour Scheme**

The developer used [eggradients](https://www.eggradients.com/shades-of-green-color) to choose colors when building the website. Particularly, the follwoing colors were used which are bright to make the site more appealling to sight:

 * #d32f2f (red color)
 * #455a64  (blue-grey color)
 * #263238  (blue-grey color )
 * #ba68c8 (purple color)
 * #69f0ae (green color)


 ## **Wireframe**

 [Balsamiq App](https://balsamiq.com/) was used for the design architechture and  the site mockups. Although, there were some minor changes in the design but mostly the layout on the app gave the guidance, a step by step guard to build the final website. Below is the link to the wireframe for the desktop and mobile device.

**View all**

 * [Wireframe](wireframe/ms3mockup.pdf)
        

# **FEATURES**

  **Existing Features**

### Register Account

* The registeration page allow intended users to register for free to create their own account. For security reason, there is a built-in authorization and    authentication  to check certain criteria to be met before an   account is validated. All passwords are hashed for further securities.

### Log In

* This is for users that registered, more authentication and authorization was embedded to check that the hashed passwords and username if they matched in the database.

### Log Out

* To enable users to log out of their accounts with a click of the button.

### View All Recipes

* On the All Recipes link on the Navbar, which will open All recipes page when clicked, it displays all the available recipes on the website.


### Search Recipes

* A user may want to search for a certain recipe by their name or by their description.

### Submit recipe

### Edit or Update Recipe



## Future Features to be Implemeneted

 * Pagination
 * Google login
 
 * To bind recipes to national related country
 * Lazy loading images
 * Prevent duplicate subscribers
 * User profiles with description, avatar, post list
 * Page loading animation
 * Subscription letters
 * Functionl emails
 * Admin console
 * Contact form and admin to be able to see all recieved messages directly in the admin console
 * Recipe image url validation
 * Sort recipes by tag, cousine, cook or prep time, even more specific dietary needs
 * Recipe Comments





# **TECHNOLOGY USED**

*The follwoing Technologies, Frameworks, and Libraries were used to build the project*  

### Tools  

* **Git**: It was used for version control which uses the Gitpod terminal to commit to Git and Push codes to GitHub
* **GitHub**:         [GitHub](https://github.com/) Developer used GitHub as a project repository to save.
* **Gitpod**:         [GitHub](https://www.gitpod.io/) The project used the Gitpod IDE as my workspace to develop the website. It is linked to GitHub repository to store data when coding.
* **Icons**:          [Font Awesome](https://fontawesome.com/) Social Media Icons were taken from this site.
* **Balsamiq**:       [Balsamiq](https://balsamiq.com/) The site was used to create the wireframes during the design stage of the project.

 ## Front-End Technologies

* [**HTML**](https://developer.mozilla.org/en-US/docs/Web/HTML): HTML/HTML5 the language used to create and as the markup text to add content to the website.  
* [**CSS**](https://developer.mozilla.org/en-US/docs/Web/CSS): It provides the styling for the website.
* [**jQuery 3.4.0**](https://jquery.com/) Used as the main JavaScript functionality.
* [materialize](https://materializecss.com/getting-started.html) Used to design the  mobile-first responsive layout for the website, forms and accordion.


## Back-End Technologies
*  Flask

    * [**Flask 1.0.2**](https://flask.palletsprojects.com/en/1.1.x/): A microframework used in python.
    * [**Jinja 2.10**](https://jinja.palletsprojects.com/en/2.10.x/):  Used for templating with Flask.
    * [**Werkzeug 0.16**](https://werkzeug.palletsprojects.com/en/0.16.x/): Used for password hashing, authentication, and authorization.

* Python

    * [**Python 3.6.7**](https://flask.palletsprojects.com/en/1.1.x/): The main back-end programming language.
    * [**MongoDB Atlas**](https://www.mongodb.com/): Used to store database in the cloud.
    * PyMongo
    
* Heroku

    * [**Heroku**](https://www.heroku.com/): Used to launch website.

* **CSS validator**:  [CSS validator](https://jigsaw.w3.org/css-validator/) The site was used to test for the validity of my CSS code. 
* **HTML validator**: [HTML validator](https://validator.w3.org/) The site was used to test for the validity of my HTML code.
* **Hover.css**:      [Hover.css](https://ianlunn.github.io/Hover/) The site was used on the navigation bar links and Social Media icons in the footer to create an hovering effects.
* **Balsamiq**:       [Balsamiq](https://balsamiq.com/) The site was used to create the wireframes during the design stage of the project.
* **freeformatter**:  [freeformatter](https://www.freeformatter.com/html-formatter.html) The site was used to format HTML.
* **Lighthouse**:     [Balsamiq](https://developers.google.com/web/tools/lighthouse/?utm_source=devtools) To audit the site perfomance and accessibility.
* **Am I Responsive?**:[Am I Responsive?](http://ami.responsivedesign.is/) It was used to test the responsiveness of the site and to take screenshot of devices.



# TESTING

***Sites Validation***

* [HTML-Validator](https://validator.w3.org/#validate_by_input"):  The site does not really understand the Jinja templating syntaxes, such as the {% for %} {% endfor %} which resulted in many errors but outside that, all the codes worked perfectly.


* [Jshint](https://jshint.com/): When using the tool some warnings were flagged which mainly were the use of ES6 (use 'esversion: 6'). But the codes work perfectly however, i have taken note of that for next project.
[Javascript test](static/testing/jsms3.png).


* The [CSS validator](https://jigsaw.w3.org/css-validator/) was without any issues [CSS test](static/testing/cssms3.png).

* The [PEP*](http://pep8online.com/checkresult) was without any issues [PEP8 test](static/testing/pep8.png).


* Furthermore, the website was tested on the following: It works perfectly in them.

      * Systems: Macbook Pro Laptop, HP laptop, and Lenovo laptop.
      * Browsers: Chrome, Opera, Edge, Firefox, Safari
      * Phones and Tabs: iPad Pro, different Iphone series and androids


## **Testing user stories from UX section**

#### First-time visitors goals:

1. As a visitor, I want to be able to view the site in all modern devices, such as the desktop, tablet and mobile etc.

      * The visitor can visite the website on computer, laptop, tablet and phone.

2  Able to see all recipes as a visitor

    * The vistors can navigate through the site form the homepage with the navbar. 
    * The navbar is at the top of the site. They niew the whole recipes by click on the "View all categories" link in the navbar
    * There is a hamburger menu for the mobile view to aid navigations.
    * From the "View all categories" link , they can click on categories such breakfast menu, lunch etc.

3  Register to be a member and a regular user
    
    * The visitor can navigate to the register page by clicking on the "register" link on the navbar. 
    * There on the page, intended user can register.

4  To be able to log in after registeration

    * A user who has registered can easily log in from the navbar at the top of the site from any page by clicking on the "log in" link.
    * The page will open, Therefore, user can log in fully.


5. Able to search for recipes by names or description

    * This operation could be performed by both regular users and non-regulars
    * This can be achieved by clicking the "View All categories" button on the navbar.
    * There on the page the user can easily use the search engine to check for any particular recipe.


6. Able to search for recipes by names or description

    * This operation could be performed by both regular users and non-regulars
    * This can be achieved by clicking the "View All categories" button on the navbar.
    * There on the page the user can easily use the search engine to check for any particular recipe either by name or description.


7. Able to search for recipes categories

    * This operation could be performed by both regular users and non-regulars
    * This can be achieved by clicking the "View All categories" button on the navbar.
    * From the drop-downs, they can click on any category and the related recipes will be opened.



8. Able to know the particular African country which the recipe belongs to.

    * This operation could be performed by both regular users and non-regulars
    * This can be achieved by clicking on a particular recipe.
    * The information about the recipe is revealed which include the nationality of such cuisine


#### User/member goals:

9. View my own profile

    * Once a user, and has login, he/she is automatically taken to their profile page.
    * There, they can see all their recipes that they have posted and may want to post more by click on a CTA button.

10. Add my recipes

    * As as a user, he/she can post recipes, the option to post recipes is only available to users on the navbar.
    * A user can click on the link on the navbar and the page will open.
  

11.  To see instructions on how to add a recipe

    * Once the user click on the link "Add Recipe" from the navbar, the form will opened.
    * The input form is easy and direct to fill, and they can submit after filling in all the requirements by hitting the   green "ADD RECIPE" button.


12. To able to edit or update their recipes

    * This can be achieved when a user click on their posted recipes.
    * There is an option to edit at the bottom of the page for the said recipe.
    * When they click on the edit button, it takes them to form which is already pre-selected for the said recipe.
    * They choose to edit in order to update or just cancel to leave the recipe.


13.  To be able to delete my recipes that are not needed again

    * This can be achieved when a user click on their posted recipes.
    * There is an option to delete sitting next to the edit button at the bottom of the page for the said recipe.
    * When they click on the delete button, it wipes off immediately.


14. To be able to log out

    * This can be achieved when a registered user click on log out button on the navbar.
    * THis button is only available to users that logged in.



14. To be able recieve feedback if they scuccessfully performed any of the CRUD operations

    * User recieve feedback in form flash messages for certain action carried out such as; registeration, login, logout, poste recipes etc.


15. To be able to recieve an error message for perform the activities that is not within the scope of the website or there is an issue with database.

    * User either gets 404/ or 405 message performing functionalities tat is not within the scope of the site.


#### *Admin Objectives:*

In addition to the aforementioned above, The Admin can:

 16. To able be able add new categories and recipes
    
    * Just like any other users, the admin is able to perfom all the functionalities above which include, adding categories and recipes.
    * Only the admin can:

        * Add, edit categories and recipes, for the site.
        * Delete categories, and recipes, in order to regulate unappropriate submissions.

    * Those operations can be performed, when the recorgnize admin log in
    * The admin profile has access to all posted recipes by users and categories unlike users' that have access to their individual posted recipes in their profiles


### Developer objectives
    By building the website, the following skills were demonstrated by the developer:

 * Able to perform the CRUD operations using python, jinja, MongoDb etc.
 * good use of Jinja templating, Python, non-relational database MongoDb
 * good use of materialize library combine with JavaScript knowledge.
 * how to make the website lives by deploying to Heroku.



## **Manual Testing**

#### **1. Register Account:**

Most of the features in the site are based on securities measures and are built on Defensive programming.

* The registeration page allow intended users to register for free to create their own account. 
* In the site and at the top is the navbar, user can click on register link on the navbar and it will navigate them to the page.
* The intended user's username has to be between 5-15 which could be characters or numbers or combined.
* The password has to be between 5-20 characters and must contain at least one capital letter, lowercases and atleast a number.
* Attempt to use username/password that is not compliant with the specified requirements and you will get; (match the requested format) tooltips.

#### **Login

 This is to enable registered user to access the pages and their profiles
    
    * User trying to brut force their ways in with wrong credentials will get: "Incorrect Username and/or Password"
    * Similarly, user submit an empty form will get tooltip pop-up like:  "Fill out this field"

#### Post recipe

 This to enable users to submit recipe to their sites and thier profiles

* On the navbar is the "Add Recipe" link, a user click on it takes them to the input form.
* A user trying to submit an empty form or uncompleted form will recieve a tooltip pointer to the uncoompleted fields.
* After filling all the fields completely, user can click the "Add Recipe" green button to submit.
* After flash message will show for scuccessfully submissions.


#### Edit or Update Recipe

 This feature is to enable users to update or editing an existing recipes posted by them 

    * On the website user can click on the recipes posted by them from their profile page.
    * Also, they click on the recipe created by them on the main page.
    * The recipe will open on another page to reveal it information.
    * At the bottom of the page there is blue " edit" button, when they click on it, it will take them to the pre-selected fields.
    * A user trying to submit an empty form or uncompleted form will recieve a tooltip pointer to the uncompleted fields.
    * After filling or changing the the desired fields, user can click the blue "Edit" button to submit.


#### Delete recipe

    This operation can only be carried out by users that have posted recipes to their names.

  A 
    * On viewing a specific recipe posted by a user, to bottom of the page is red "Delete" button.

    * A click on it will instantly remove the recipe completely.

    * Users only see the "EDIT and DELETE" buttons of the recipes posted by them.



B   * A user can also delete a recipe from their Profile page.

    * On the accordion on their profile page, their are the "DELETE and EDIT" buttons.

    * When a user click on the red delete button, there is a pop-up dialogue modal that will ask, if user is sure they want to delete the said recipes.

    * User can either choose to delete or cancel


####  Logout

        This can only be carried out by those were already log in

        * On the navbar is the logout option for the users.
        * click on it will log them out and will reidrect to login page.


## Bugs and resolves

Most of the errors encoountered were syntaxes errors, especially in using Jinja templating to carryout for loops operations, the one that was most prominent was a floating footer in 404/.html pages and some other pages with less data contents. Below is example of one of the images;

 [bug](static/testing/floatresult.png)

## Resolves

All the floats were resolved by applying this css code form materialise library

 body {
    display: flex;
    min-height: 100vh;
    min-width: 100vh;
    flex-direction: column;
  }

  main {
    flex: 1 0 auto;
  }



# **DEPLOYMENT**

The website was developed using both GitPod and using Git push to store them in GitHub, while [Heroku](https://dashboard.heroku.com/apps) is use to launch the site to the internet. 

### Steps to Deploy: Local Deployment;

*Requirements*
* [Python3](https://www.python.org/downloads/) to run the application backend.
* [PIP](https://pip.pypa.io/en/stable/installing/) to install all required packages.     
* [GIT](https://www.atlassian.com/git/tutorials/install-git) for push and version control.
* [MongoDB](https://www.mongodb.com/) database to store data on MongoDB Atlas.  

The project need to be clone locally by the following steps:

1. Browse the repository link [africadelishms3](https://github.com/Rozdandy/africadelishms3) 
to clone the project by clicking the green Clone or download button and downloading the project.

2.  Or by entering the following into the Git CLI terminal: https://github.com/Rozdandy/africadelishms3.git
3.	Open Githpod workspace, that is Git Bash.
4.	Using the command line, type git clone, and then paste the URL you copied above
5.	Press Enter. Your local clone will be created
6.  Navigate to the correct file location after unzipping the files and cd <path to folder>

#### Using the local copy

* Sign up and create a cluster and a database with MongoDB.
* Create the the afriq_delish DB and the collections  in the mongodb which are: categories, recipes, and users.

     *                    RECIPES

                _id: <ObjectId>

                recipe_name: <string>
                category_name: <string>
                simple_description: <string>
                prep_duration: <string>
                ingredients: <array>
                adult_plate: <string>
                ingredient_name: <array>
                cook_directions: <array>
                cook_duration: <string>
                cuisine: <string>
                img_url: <string>
                author: <ObjectId>
                date_posted: <string>


    *            USERS

                _id: <ObjectId>
                username: <string>
                user_password: <string>


    *             Categories

                _id: <ObjectId>
                category_name: <string>


* Create a .env file, in which your MONGO_URI and SECRET_KEY values, are included and hidden
* Install all requirements from the requirements.txt file using this command:
        sudo -H pip3 -r requirements.txt
* Add your .env file to .gitignore
* Ensure to to change the last line from debug=False to debug=True in your app.py
* Run the app locally by typing: flask run
* The app should be running on localhost server which you can copy link past on browser.



### Steps to Remote Deployment:

    * In Heroku, create an app with unique name.

    * Ensure to have created a requirements.txt file so Heroku can install the required dependencies to run the app.
            i.e  sudo pip3 freeze --local > requirements.txt
    * Create your Procfile file, Heroku need to know the type of application that is being deployed, and how to run it.
                 echo web: python run.py > Procfile

     * Link that app to the GitHub repository by going to the "Deploy" link in the main app menu.
     * Connect GitHub as the Deployment Method, and select Enable Automatic Deployment.

    * Click on Settings tab, click to add the corresponding Config Variables as present in your files


            * IP : 0.0.0.0
            * PORT : 8080
            * MONGO_URI : <your Mongo DB link>
            * SECRET_KEY : <your created secret key>

    * If steps are carefully done the app will successfully deployed to Heroku and running on a live server.
           



# CREDITS

## contents


**References:**


* Special thanks to Tim Nelson lecture videos, many of the codes on registeration, authorization, authentication many more I assisted me in completing this project.
* Also the materialise theme from http://swarnakishore.github.io/MaterialSliderTheme/


## Media

All of the images in the site were supplied drom the sources below.

* Game background Image:
    *   https://www.pikrepo.com/flrcm/lasagna-on-top-of-white-ceramic-plate
    *   https://www.pikrepo.com/ftfhq/assorted-foods-on-table
    *   https://www.pikrepo.com/nuzcs/local-thai-food-buffet
    *   https://www.pikrepo.com/frive/roasted-steak-with-sliced-tomato-on-white-plate

* Images: 
  
    * https://www.pikrepo.com/fnuon/gray-curved-road-beside-arrow-left-signage-under-white-cloud-blue-skies#google_vignette
    * https://www.pikrepo.com/fomjf/brown-wooden-fence-near-trees-covered-in-snow
    * https://www.pikrepo.com/frdlf/red-leaf-tree-digital-wallpaper
    * Among others are google images





















