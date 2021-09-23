<h1 align="center"><img src="https://passion-4-painting.s3.eu-west-2.amazonaws.com/media/logo-m.png" style="margin: 0;" alt="image of site logo"></h1>

[View the live website here.](https://passion-4-painting.herokuapp.com/)

## Table of Contents

# Passion 4 Painting Overview

## Things to consider

1. Goods to sell that can be grouped into categories
2. Using Django as a framework.
3. The C.R.U.D functionality - site owners must be able to add, read, update and delete the products on the store.
4. A search function to locate products by name/ category or description .
5. The site must be user friendly and visually appealing.
6. A user can register on the site but does not have to in order to make a purchase.

# UX

## User stories



## Wireframes page designs

**Home page:**

<img src="media/wireframes/home_page.png" style="margin: 0;">

**Products page:**

<img src="media/wireframes/products_page.png" style="margin: 0;">

**Product details page:**

<img src="media/wireframes/product_details_page.png" style="margin: 0;">

**Shopping bag page:**

<img src="media/wireframes/shopping_bag_page.png" style="margin: 0;">

**Checkout page:**

<img src="media/wireframes/checkout_page.png" style="margin: 0;">

## Features

-   Responsive on all device sizes. For example:


## Error Handling

I created custom error pages so that if the user encounters a page that doesn't exist/deleted/forbidden etc, the stlye of the error page will match the rest of the site. This makes the site more professional.

- 404 Not Found
- 403 Forbidden
- 410 Gone
- 500 Internal Server Error

404 error page example



## Technologies Used

### Languages Used

In this project I used:
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [JQuery](https://jquery.com/) 
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [Django](https://www.djangoproject.com/) 

### Frameworks, Libraries & Programs Used

-   [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/) I used Bootstrap's framework for the styling and for responsivness on mobiles.
-   [Heroku](https://www.heroku.com/home) Heroku is where the site is deployed.
-   [Google Fonts:](https://fonts.google.com/) Google fonts were used to import the 'Satisfy' font into the style.css file which is used on all pages throughout the project.
-   [Font Awesome:](https://fontawesome.com/) Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
-   [GitHub:](https://github.com/) GitHub is used to store the projects code after being pushed from Git.
-   [Git:](https://git-scm.com/) Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
-   [Responsinator:](http://www.responsinator.com/) Responsinator was used to check the site was responsive across all devices.
-   [Am I Responsive](http://ami.responsivedesign.is/) Am I Responsive was used to demonstrate the site was responsive in the attached screenshots.
-   [Balsamiq:](https://balsamiq.com/) Balsamiq was used to create the wireframes during the design process.
-   [Lighthouse](https://developers.google.com/web/tools/lighthouse)
-   Chrome, Microsoft Edge & Firefox internet browsers.
-   Adobe Photoshop.

## Testing

### Manual Testing documentation


### Validators

I used the following services to validate every page of the project to ensure there were no syntax errors:

-   [W3C Markup Validator](https://validator.w3.org/) This validator doesnt like the Jinja templating - but if you run the code from the page source you can check for any non-jinja errors.
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
-   [JSHint](https://jshint.com/)
-   [PEP8 Online Check](http://pep8online.com/)

<img style="border:0;width:88px;height:31px"
        src="http://jigsaw.w3.org/css-validator/images/vcss-blue"
        alt="Valid CSS!" />



### Testing User Stories


### Further Testing

-   The Website was tested on Google Chrome, Microsoft Edge and FireFox browsers to check it loaded correctly.
-   The website was viewed on a variety of devices such as Desktop, Laptop and a variety of iPhones & Android phones to check it loaded correctly.
-   The website was tested on Responsinator to ensure responsiveness on all devices.
-   A large amount of testing was done to ensure that all pages were linking correctly. This was done by frequently moving from one page by clicking the button links for 
all pages on all devices.
-   A large amount of testing of the database C.R.U.D functions was completed during development. After every change the site was tested to ensure no new issues or bugs were located.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues, they reported a success on all fronts.
-   The website was tested on [Lighthouse](https://developers.google.com/web/tools/lighthouse) and achieved a high score on all issues:

    
    You can use the Lighthouse Tool on any webpage by right clicking on the site, then 'inspect', then the two arrow button '>>' and 'Lighthouse'. You can select to test the site 
    as a desktop version or mobile version and then click the blue 'Generate Report' which will provide you with the results in the screenshot provided above.

## Known Bugs

No bugs have been located at the time of Deployment.

## Deployment

### GitHub Pages

The repository for this project is stored on [GitHub](https://github.com/) and is deployed on [Heroku](https://www.heroku.com/).

In order to add to this project you will need:

- Python 3.8.3 or higher
- Git version control
- Code editor
- GitHub account
- MongoDB account

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Passion4film/Milestone-Project-3)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/Passion4film/Milestone-Project-3)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/Passion4film/Milestone-Project-3
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/Passion4film/Milestone-Project-3
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

8. Create a file called env.py for the environment variables, containing:

```console
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "<app secret key>")
os.environ.setdefault("MONGO_URI", "mongodb+srv://<username>:<password>@<cluster_name>-ofgqg.mongodb.net/<database_name>?retryWrites=true&w=majority")
os.environ.setdefault("MONGO_DBNAME", "<database name>")

```
9. **Ensure that env.py is listed in your .gitignore file so that the environment variables are are never made public**
10. The app can now be run locally using
```console
python3 app.py
```

## Deployment to Heroku 

If you have a Heroku account login [here](https://id.heroku.com/login) or create an account.

Before creating a Heroku application there are some files that need to be created to run the app:

* requirements.txt file (which lists the dependencies that are needed for the app) 
* Procfile (this is what Heroku looks for to know which file runs the app, and how to run it)

```console
pip3 freeze --local > requirements.txt
echo web: python app.py > Procfile
```

At Heroku.com you can choose to 'Create a New App' - the name must be unique, in lowercase letters and use dashes instead of spaces.

* Next, select the region closest (doesn't have to be exact - I chose Europe) to you then click 'Create App'.
* For this project I chose to setup 'Automatic Deployment' from my GitHub repository. 
* Make sure your GitHub profile is displayed, then add your repository name then click 'Search'. Once it finds your repo, click to connect to this app.
* DON'T click to Enable Automatic Deployment yet, otherwise you'll get unwanted application errors.

Since environment variables are within a hidden env.py file, Heroku won't be able to read those variables. Click on the 'Settings' tab for your app, and then click on 
'Reveal Config Vars', where we can securely tell Heroku which variables are required. Must match the details in the env.py file you have to create in github.

Make sure not to include any "quotes" for the key, or the value.


* Make sure all changes on GitHub have been added, commited and pushed to GitHub. 
* We can now safely 'Enable Automatic Deployment', as everything should be available on our repository.
* Click 'Deploy Branch'. Heroku will now receive the code from GitHub, and start building the app using the required packages. 
* When this is completed it will state: "Your app was successfully deployed." 
* Click "View" to launch your new app.

## Future maintainability


## Credits

### Content

Online tutorials:

* [For the content of the Health and Wellbeing page](https://ledgebay.com/benefits-of-paint-by-numbers/)

* [For the deletion confirmation model - for site admin only](https://www.tutorialrepublic.com/codelab.php?topic=bootstrap&file=delete-confirmation-modal)

* [For the image carousel on product details page - to show a pic of the kit that comes with the painting](https://www.tutorialrepublic.com/twitter-bootstrap-tutorial/bootstrap-carousel.php)


### Media

I created the logo, flavicon, error pages for the site using Adobe Photoshop.

[The logo base image](https://i.pinimg.com/originals/ca/20/d8/ca20d859c1ff063d9482a56d9be19574.jpg)

[The painting kit image](https://images.squarespace-cdn.com/content/v1/5ad8947d2714e5edb7bde89d/1592030962065-YG0VE9TB0QBLQPY8CRI4/DSC_7463.jpg?format=1000w)

[The featured image on the home page](https://www.stylist.co.uk/images/app/uploads/2021/01/26123624/paint-by-numbers-for-adults-crop-1611664653-1920x1006.jpg?w=1680&h=880&fit=max&auto=format%2Ccompress)

All the paintings 'on sale' are photos of my own paintings I have completed myself, from my home. I took all the photographs and edited/uploaded them accordingly.

## Acknowledgements

I received inspiration for this project from the Boutique Ado mini-project as part of the Code Institute course, example websites, Slack message boards as well as 
much appreciated help from my Mentor; Antonio Rodriguez.

**DISCLAIMER: This project is for educational purposes only, no materials/files are intended for any commercial use**

[Contents](#Table-of-Contents)