<h1 align="center">Great Recipes Website</h1>

[View the live project here.](https://flask-great-recipes.herokuapp.com/home)

This is the website for the Great Recipes database. It is designed to be responsibe and accessible on a range of devices, making it easy to navigate for all users.

<h2 align="center"><img src="https://i.ibb.co/TYvTXz1/Example-CI.png"></h2>

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to easily understand the main purpose of the site.
        2. As a First Time Visitor, I want to be able to easily navigate throughout the site to find or add recipes.
        3. As a First Time Visitor, I want to look for testimonials to understand what users think of the website and the recipes. I also want to locate their social media links to see their followings on social media to determine what people think of the recipes.

    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to quickly finds recipes for the cuisine that I'm interested in. 
        2. As a Returning Visitor, I want to find community links.
               
        1. As a Returning Visitor, I want to find information about coding challenges. ,,,,,,,,,,,,,,,
        2. As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.,,,

    -   #### Frequent User Goals
        1. As a Frequent User, I want to add my own recipes.
        1. As a Frequent User, I want to check to see if there are any newly added recipes. ----- needs date.
        2. As a Frequent User, I want to check to see if there are any new blog posts.
        3. As a Frequent User, I want to sign up to the Newsletter so that I am emailed any major updates and/or changes to the website or organisation.,,,,,,,,,,,,,,,,,,

-   ### Design
    -   #### Colour Scheme
        -   The two main colours used are light blue and white.

    -   #### Typography
        -   The Montserrat font is the main font used throughout the whole website with Sans Serif as the fallback font in case for any reason the font isn't being imported into the site correctly. Montserrat is a clean font used frequently in programming, so it is both attractive and appropriate.

        was
        font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif;


    -   #### Imagery
        -   Imagery is important. The large, background hero image is designed to be striking and catch the user's attention. It also has a modern, energetic aesthetic.

        too late to add a hero image to home page.

*   ### Wireframes

    -   The reader has access to the Home, Register and Login Pages.

    -   Home Page Wireframe - [View](wireframe_and_database_design/great_recipes_home.pdf)
    -   Register Page Wireframe - [View](wireframe_and_database_design/great_recipes_register.pdf)
    -   Login Page Wireframe - [View](wireframe_and_database_design/great_recipes_login.pdf)


    -   The registered user has access to the Home and Add Recipe Pages. The Registered user can also Log out.
    -   Add Recipe Page Wireframe - [View](wireframe_and_database_design/great_recipes_add_recipe.pdf)


    -   The admin has access to the Home, Add Recipe and Manage Cuisine Pages. The admin can also Log out.
    
    Added. The Admin can also generate a search index.
    -   Manage Cuisine Wireframe - [View](wireframe_and_database_design/great_recipes_manage_cuisine.pdf)

    18th July. Add My Recipes so that users can click on the recipes they added without searching for them.

*   ### Database Design

    -   Database Design - [View](wireframe_and_database_design/QuickDBD-Recipe.png)


## Features

-   Responsive on all device sizes

-   Interactive elements

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Jinja2](https://en.wikipedia.org/wiki/Jinja_(template_engine))
-   [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [jQuery](https://en.wikipedia.org/wiki/JQuery)
-   [Markdown](https://en.wikipedia.org/wiki/Markdown)
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)


### Frameworks, Libraries & Programs Used

1. [Bootstrap 4.4.1:](https://getbootstrap.com/docs/4.4/getting-started/introduction/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Hover.css:](https://ianlunn.github.io/Hover/)
    - Hover.css was used on the Social Media icons in the footer to add the float transition while being hovered over.
1. [Photoshop:](https://www.adobe.com/ie/products/photoshop.html)
    - Photoshop was used to create the logo, resizing images and editing photos for the website.


1. [MaterializeCSS:](https://materializecss.com/)
    - Materialize is a framework was used to assist with the styling of the website.

1. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [Gitpod](https://www.gitpod.io/)
    - The Gitpod workspace was used to develop the HTML5, CSS3, Jinja2 and Python3 code.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the [wireframes](wireframe_and_database_design/) during the design process.
1. [Cloudinary:](https://cloudinary.com/)
    - Cloudinary was used create square images and to host the recipe images.
1. [mongoDB:](https://www.mongodb.com/)
    - mongoDB was used create the database to store the recipes, cuisines and user details.
1. [Flask:](https://www.mongodb.com/)
    - Flask is a python framework with Werkzeug and Jinja.


## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](https://github.com/)

html ok
css ok
js ok
python code all right

### Usernames and Passwords

-   username:timothy password:12345678
-   username:admin password:12345678

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    1. As a First Time Visitor, I want to easily understand the main purpose of the site and learn more about the organisation.

        1. Upon entering the site, users are automatically greeted with a clean and easily readable navigation bar to go to the page of their choice. Underneath there is a Hero Image with Text and a "Learn More" Call to action button.
        2. The main points are made immediately with the hero image
        3. The user has two options, click the call to action buttons or scroll down, both of which will lead to the same place, to learn more about the organisation.

    2. As a First Time Visitor, I want to be able to easily be able to navigate throughout the site to find content.

        1. The site has been designed to be fluid and never to entrap the user. At the top of each page there is a clean navigation bar, each link describes what the page they will end up at clearly.
        2. At the bottom of the first 3 pages there is a redirection call to action to ensure the user always has somewhere to go and doesn't feel trapped as they get to the bottom of the page.
        3. On the Contact Us Page, after a form response is submitted, the page refreshes and the user is brought to the top of the page where the navigation bar is.

    3. As a First Time Visitor, I want to look for testimonials to understand what their users think of them and see if they are trusted. I also want to locate their social media links to see their following on social media to determine how trusted and known they are.
        1. Once the new visitor has read the About Us and What We Do text, they will notice the Why We are Loved So Much section.
        2. The user can also scroll to the bottom of any page on the site to locate social media links in the footer.
        3. At the bottom of the Contact Us page, the user is told underneath the form, that alternatively they can contact the organisation on social media which highlights the links to them.

-   #### Returning Visitor Goals

    1. As a Returning Visitor, I want to find the new programming challenges or hackathons.

        1. These are clearly shown in the banner message.
        2. They will be directed to a page with another hero image and call to action.

    2. As a Returning Visitor, I want to find the best way to get in contact with the organisation with any questions I may have.

        1. The navigation bar clearly highlights the "Contact Us" Page.
        2. Here they can fill out the form on the page or are told that alternatively they can message the organisation on social media.
        3. The footer contains links to the organisations Facebook, Twitter and Instagram page as well as the organization's email.
        4. Whichever link they click, it will be open up in a new tab to ensure the user can easily get back to the website.
        5. The email button is set up to automatically open up your email app and autofill there email address in the "To" section.

    3. As a Returning Visitor, I want to find the Facebook Group link so that I can join and interact with others in the community.
        1. The Facebook Page can be found at the footer of every page and will open a new tab for the user and more information can be found on the Facebook page.
        2. Alternatively, the user can scroll to the bottom of the Home page to find the Facebook Group redirect card and can easily join by clicking the "Join Now!" button which like any external link, will open in a new tab to ensure they can get back to the website easily.
        3. If the user is on the "Our Favourites" page they will also be greeted with a call to action button to invite the user to the Facebook group. The user is incentivized as they are told there is a weekly favourite product posted in the group.

-   #### Frequent User Goals

    1. As a Frequent User, I want to check to see if there are any newly added challenges or hackathons.

        1. The user would already be comfortable with the website layout and can easily click the banner message.

    2. As a Frequent User, I want to check to see if there are any new blog posts.

        1. The user would already be comfortable with the website layout and can easily click the blog link

    3. As a Frequent User, I want to sign up to the Newsletter so that I am emailed any major updates and/or changes to the website or organisation.
        1. At the bottom of every page their is a footer which content is consistent throughout all pages.
        2. To the right hand side of the footer the user can see "Subscribe to our Newsletter" and are prompted to Enter their email address.
        3. There is a "Submit" button to the right hand side of the input field which is located close to the field and can easily be distinguished.

### Force URL defensive code testing

heroku url here

https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io - No need to force test reader URL.
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/home - No need to force test reader URL.
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/login - No need to force test reader URL.
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/register - No need to force test reader URL.
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/my_recipes/timothy - KeyError: 'user'


https://8080-teal-lobster-b2qs96iu.ws-eu15.gitpod.io/add_recipe/timothy works


https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/my_recipes/ - Great Recipes Error 404 page.
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/my_recipes - Great Recipes Error 404 page.
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/add_recipe/timothy - not protected!!
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/add_recipe/ - Great Recipes Error 404 page.
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/add_recipe - Great Recipes Error 404 page.

no login
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/my_recipes/admin
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/add_recipe/admin
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/edit_recipe/admin%2C%206108163bc80beeddeb309516
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/edit_recipe/admin
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/admin_recipes/admin
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/admin_recipes
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/cuisines/admin
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/add_cuisine/admin
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/add_cuisine
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/cuisines
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/generate_index/admin
https://8080-teal-lobster-b2qs96iu.ws-eu14.gitpod.io/generate_index

user login

whatever else is in app.py

Reader
- https://flask-great-recipes.herokuapp.com/
- https://flask-great-recipes.herokuapp.com/login
- https://flask-great-recipes.herokuapp.com/register

User
- http://flask-great-recipes.herokuapp.com/home
- http://flask-great-recipes.herokuapp.com/recipes (search)
- http://flask-great-recipes.herokuapp.com/my_recipes/timothy
- http://flask-great-recipes.herokuapp.com/edit_recipe/timothy%2C%206106ee4ae19c3957347e8e59
- http://flask-great-recipes.herokuapp.com/add_recipe/timothy

admin
- http://flask-great-recipes.herokuapp.com/home
- http://flask-great-recipes.herokuapp.com/my_recipes/admin
- http://flask-great-recipes.herokuapp.com/my_recipes/admin (search)
- http://flask-great-recipes.herokuapp.com/add_recipe/admin
- http://flask-great-recipes.herokuapp.com/admin_recipes/admin
- http://flask-great-recipes.herokuapp.com/cuisines/admin
- http://flask-great-recipes.herokuapp.com/add_cuisine/admin
- http://flask-great-recipes.herokuapp.com/generate_index/admin

- http://flask-great-recipes.herokuapp.com/
- http://flask-great-recipes.herokuapp.com/home
- http://flask-great-recipes.herokuapp.com/recipes
- http://flask-great-recipes.herokuapp.com/generate_index <>
- http://flask-great-recipes.herokuapp.com/search
- http://flask-great-recipes.herokuapp.com/search_user <>
- http://flask-great-recipes.herokuapp.com/register
- http://flask-great-recipes.herokuapp.com/login
- http://flask-great-recipes.herokuapp.com/my_recipes <>
- http://flask-great-recipes.herokuapp.com/admin_recipes <>
- http://flask-great-recipes.herokuapp.com/logout <>
- http://flask-great-recipes.herokuapp.com/add_recipe <>
- http://flask-great-recipes.herokuapp.com/edit_recipe <> <>
- http://flask-great-recipes.herokuapp.com/delete_recipe <> <>
- http://flask-great-recipes.herokuapp.com/cuisines <>
- http://flask-great-recipes.herokuapp.com/add_cuisine <>
- http://flask-great-recipes.herokuapp.com/edit_cuisine <> <>
- http://flask-great-recipes.herokuapp.com/delete_cuisine <> <>









### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop, iPhone7, iPhone 8 & iPhoneX.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.



### Known Bugs

-   On some mobile devices the Hero Image pushes the size of screen out more than any of the other content on the page.
    -   A white gap can be seen to the right of the footer and navigation bar as a result.
-   On Microsoft Edge and Internet Explorer Browsers, all links in Navbar are pushed upwards when hovering over them.

## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits

### Code

-   This project was based on the Code Institute Data Centric Development Mini Project.

-   The full-screen hero image code came from this [StackOverflow post](https://stackoverflow.com)

-   [Bootstrap4](https://getbootstrap.com/docs/4.4/getting-started/introduction/): Bootstrap Library used throughout the project mainly to make site responsive using the Bootstrap Grid System.

-   [MDN Web Docs](https://developer.mozilla.org/) : For Pattern Validation code. Code was modified to better fit my needs and to match an Irish phone number layout to ensure correct validation. Tutorial Found [Here](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input/tel#Pattern_validation)

### Content

-   All content was written by the developer.

-   Psychological properties of colours text in the README.md was found [here](http://www.colour-affects.co.uk/psychological-properties-of-colours)

### Media

-   All Images were created by the developer.

### Acknowledgements

-   My Mentor for continuous helpful feedback.
-   Tutor support at Code Institute for their support.

### TBD

-   Add date that recipe was created to support listing new recipies first.
-   Add hero image of nice looking recipe to the home page.
-   Add favicon.

### BUGS
-   Small bug. saving cuisine style as cuisine name in the DB. changed all references from cuisine_name to cuisine_style.
-   Small bug. Recipies.html showing no results found. Had {% if tasks|length > 0 %} instead of {% if recipes|length > 0 %}
-   Small bug. my_recipes.html had same code as recipies.html but was not listing the recipes. Added recipes = list(mongo.db.recipes.find()) yo my_recipies in app.py.
    Was not connecting to the DB.
-   Small bug. Collapsed search bar was being displayed on my_recipe.html. changed search to
recipes = list(mongo.db.recipes.find({"created_by": username, "$text": {"$search": query}}))
so nothing would be passed to my_recipes.html if there was no result found.

-   edit_recipe.html Bug. Ingredients were not being displayed on screen in one column. The 2nd and third elements were indented.
-   https://stackoverflow.com/questions/45719062/jinja-docx-template-avoiding-new-line-in-nested-for/45719723
-   detailed {{ '\n' -}} solution.
-   {% if not loop.last %}{{ '\n' }}{% endif %} prevented the last CR.
-   
-   Bug. Materialize pop up was deleting the first recipe not the one selected. Used variable insteaf of href="#modal1"
Added data-target="{{ recipe._id }} to Modal trigger
Added id="{{ recipe._id }}" to modal structure.

        existing_cuisine = mongo.db.cuisines.find_one(
            {"cuisine_style": request.form.get("cuisine_style").lower()})
        if existing_cuisine:
            flash("Cuisine already exists")
            return redirect(url_for("get_cuisines"))

            

                    existing_cuisine = mongo.db.cuisines.find_one(
            {"cuisine_style": request.form.get("cuisine_style").lower()})
        if existing_cuisine:
            flash("Cuisine already exists")
            return redirect(url_for("get_cuisines"))

            Allows the creation of Thai followed by thai but not thai followed by Thai.

           Credit  https://www.tutorialspoint.com/list-all-values-of-a-certain-field-in-mongodb




                   new_style = request.form.get("cuisine_style").lower()

        # Credit tutorialspoint
        db_styles = mongo.db.cuisines.distinct("cuisine_style")

        for style in db_styles:
            if style.lower() == new_style:
                flash("Cuisine already exists")
                return redirect(url_for("get_cuisines"))

use .distinct() function

        New code converts both database cuisine_style and form cuisine_style to lowercase and compares that.

not needed for new recipe as there can be multiple recipies with the same name.
/* Footer code from Materialize */

defensive code in my_recipes
Getting Key Error user when forcing URL https://8080-teal-lobster-b2qs96iu.ws-eu13.gitpod.io/my_recipes/timothy while logged out.

Rearranged code to put session["user"] variable after if session:

Forcing URL for logout when not logged in gives a key error. So add defensive code.


https://8080-teal-lobster-b2qs96iu.ws-eu13.gitpod.io/search_user/jack
gives pymongo.errors.OperationFailure
so add defensive programming.

edit recipe has an id passed to it so not likely to be forced. But someone may share their url with a recipe id in it so add extra defensive programming to be sure.

bug
TypeError: 'NoneType' object is not iterable
reset button on all recipes page would not work. tracked down to null element in Mongo DB.

Edit recipe cancel button did not work.
werkzeug.routing.BuildError
werkzeug.routing.BuildError: Could not build url for endpoint 'edit_recipe' with values ['recipe_id']. Did you forget to specify values ['username']?

Due to commented out code in recipres.html.
                            <!-- {% if session.user|lower == recipe.created_by|lower %}
                                <a href="{{ url_for('edit_recipe', recipe_id=recipe._id) }}" class="btn-small light-blue lighten-1">Edit</a>
                                <a href="{{ url_for('delete_recipe', recipe_id=recipe._id) }}" class="btn-small red text-shadow">Delete</a>
                            {% endif %}                        -->

Edit recipe save edits button did not work.
TypeError: 'NoneType' object is not iterable
null in database ingredients, i.e. not an array.

Coud not edit a recipe and save it again with no changes.
AttributeError: 'NoneType' object has no attribute 'split'
ingredients (but not preperation_steps or tools) in edit_recipe.html was declared as an array with id/name/for="ingredients[]"

Credit stack overflow. Hide icons on small devices.
https://stackoverflow.com/questions/58232219/how-do-i-remove-font-awesome-icons-on-my-responsive-navbar-when-in-desktop-versi


Error 404 Tutor support
https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/


42px margin left on searh window in all_recipes.html
Tried new class on input and label - did not work.
Tutor support #input-field worked.

cuisine and recipe name not wrapping with col s12
Tutor support added 

.collapsible-header {
  display: flex;
  flex-direction: row;
}

and

  .collapsible-header {
    flex-direction: column;
  }


after.

small bug. recipe edit and delete buttons above the footer bar.
Add

footer {
  z-index: 1;
}