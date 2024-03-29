import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
# This allows us to properly render MongoDB documents by their unique ID
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")  # Landing Page
@app.route("/home")
def home():
    # list() converts Mongo Cursor Object to a list.
    # I.e. so commented out code cannot be read by Jinja
    return render_template("home.html")


# Credit Tutor support
# https://flask.palletsprojects.com
# Error 404 page
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error404.html'), 404


# Published recipes Page, available to all Readers/Users.
@app.route("/recipes")
def recipes():
    # list() converts Mongo Cursor Object to a list.
    # I.e. so commented out code cannot be read by Jinja
    recipes = list(mongo.db.recipes.find({"is_published": "yes"}))
    return render_template(
        "all_recipes.html", username="guest", recipes=recipes, access="pub")


# Generate Mongo DB search Index. Admin function only.
@app.route("/generate_index/<username>", methods=["GET", "POST"])
def generate_index(username):
    block_force_url_admin(username)
    if request.method == "POST":
        mongo.db.recipes.create_index([(
            "recipe_name", "text"), ("ingredients", "text")])
        flash("Search Index has been generated")
    recipes = list(mongo.db.recipes.find())
    return render_template("generate_index.html", recipes=recipes)


# Search published recipes search. Available to all Readers/Users.
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find(
        {"is_published": "yes", "$text": {"$search": query}}))
    return render_template(
        "all_recipes.html", username="guest", recipes=recipes, access="pub")


# User search of the recipies that they created.
@app.route("/search_user/<username>", methods=["GET", "POST"])
def search_user(username):
    block_force_url(username)
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find(
        {"created_by": username, "$text": {"$search": query}}))
    return render_template(
        "all_recipes.html", username=username, recipes=recipes, access="my")


# Site register function. Available to all Readers.
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # acts as else
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)  # Insert the register dictionary

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        # Pass user cookie to username in userrecipes template
        return redirect(url_for("my_recipes", username=session["user"]))

    return render_template("register.html")


# Site log in function. Available to all Users.
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        # If true - if found
        if existing_user:
            # ensure hashed password matches user input
            # is DB password hash = log in form password hash
            password = request.form.get("password")
            if check_password_hash(existing_user["password"], password):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "my_recipes", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# User function to list their recipes
@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    block_force_url(username)
    recipes = list(mongo.db.recipes.find(
        {"created_by": session["user"]}))
    return render_template(
        "all_recipes.html", username=username, recipes=recipes, access="my")


# Admin function to list all recipes in the Database
@app.route("/admin_recipes/<username>", methods=["GET", "POST"])
def admin_recipes(username):
    block_force_url_admin(username)
    recipes = list(mongo.db.recipes.find())
    return render_template(
        "all_recipes.html", username=username, recipes=recipes, access="all")


# Admin function to search all recipes in the Database
@app.route("/search_admin_recipes/<username>", methods=["GET", "POST"])
def search_admin_recipes(username):
    block_force_url_admin(username)
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template(
        "all_recipes.html", username=username, recipes=recipes, access="all")


# Logout function available to Users.
@app.route("/logout/<username>")
def logout(username):
    block_force_url(username)
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")  # Remove session cookie.
    return redirect(url_for("home"))


# Add recipe function available to Users.
@app.route("/add_recipe/<username>", methods=["GET", "POST"])
def add_recipe(username):
    block_force_url(username)
    if request.method == "POST":
        is_published = "yes" if request.form.get("is_published") else "off"
        recipe = {
            "cuisine_style": request.form.get("cuisine_style"),
            "recipe_name": request.form.get("recipe_name"),
            "picture": request.form.get("picture"),
            # Credit: Tutor support for .split() suggestion
            "ingredients": [i.strip() for i in request.form.get(
                "ingredients").split(';')],
            "preparation_steps": [i.strip() for i in request.form.get(
                "preparation_steps").split(';')],
            "tools_required": [i.strip() for i in request.form.get(
                "tools_required").split(';')],
            "is_published": is_published,
            "created_by": username
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("recipes"))

    # IF POST above . . . . else GET here.
    cuisines = mongo.db.cuisines.find().sort("cuisine_style", 1)
    return render_template("add_recipe.html", cuisines=cuisines)


# Edit recipe function available to Users.
@app.route("/edit_recipe/<username>, <recipe_id>", methods=["GET", "POST"])
def edit_recipe(username, recipe_id):
    block_force_url(username)
    if request.method == "POST":
        # Add is_published logic here and to add recipe above.
        # recipe = {} changed to submit = {} as recipe =
        # mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}) is used below
        is_published = "yes" if request.form.get("is_published") else "off"
        submit = {
            "cuisine_style": request.form.get("cuisine_style"),
            "recipe_name": request.form.get("recipe_name"),
            "picture": request.form.get("picture"),
            # Credit: Tutor support for .split() suggestion
            "ingredients": [i.strip() for i in request.form.get(
                "ingredients").split(';')],
            "preparation_steps": [i.strip() for i in request.form.get(
                "preparation_steps").split(';')],
            "tools_required": [i.strip() for i in request.form.get(
                "tools_required").split(';')],
            "is_published": is_published,
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")
        return redirect(url_for('my_recipes', username=session['user']))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines = mongo.db.cuisines.find().sort("cuisine_style", 1)
    return render_template(
        "edit_recipe.html", username=username, recipe=recipe,
        cuisines=cuisines)


# Delete recipe function available to Users.
@app.route("/delete_recipe/<username>, <recipe_id>")
def delete_recipe(username, recipe_id):
    block_force_url(username)
    mongo.db.recipes.delete_one({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for('my_recipes', username=session['user']))


# List Cuisines. Admin function only.
@app.route("/cuisines/<username>")
def cuisines(username):
    # Redirect user if there is a force URL without a session
    block_force_url_admin(username)
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_style", 1))
    # cuisines on LHS passed to temlpate, cuisines on RHS = list(mongo.db above
    return render_template(
        "cuisines.html", username=username, cuisines=cuisines)


# Add Cuisine. Admin function only.
@app.route("/add_cuisine/<username>", methods=["GET", "POST"])
def add_cuisine(username):
    block_force_url_admin(username)
    if request.method == "POST":
        # check if cuisine already exists in db
        new_style = request.form.get("cuisine_style").lower()

        # Credit tutorialspoint
        db_styles = mongo.db.cuisines.distinct("cuisine_style")

        for style in db_styles:
            if style.lower() == new_style:
                flash("Cuisine already exists")
                return redirect(url_for("cuisines", username=username))

        cuisine = {
            "cuisine_style": request.form.get("cuisine_style")
        }
        mongo.db.cuisines.insert_one(cuisine)
        flash("New Cuisine Added")
        return redirect(url_for("cuisines", username=username))

    return render_template("add_cuisine.html")


# Edit Cuisine. Admin function only.
@app.route("/edit_cuisine/<username>, <cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(username, cuisine_id):
    block_force_url_admin(username)
    if request.method == "POST":
        submit = {
            "cuisine_style": request.form.get("cuisine_style")
        }
        mongo.db.cuisines.update({"_id": ObjectId(cuisine_id)}, submit)
        flash("Cuisine Successfully Updated")
        return redirect(url_for("cuisines", username=username))

    cuisine = mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("edit_cuisine.html", cuisine=cuisine)


# Delete Cuisine. Admin function only.
@app.route("/delete_cuisine/<username>, <cuisine_id>")
def delete_cuisine(username, cuisine_id):
    block_force_url_admin(username)
    mongo.db.cuisines.delete_one({"_id": ObjectId(cuisine_id)})
    flash("Cuisine Successfully Deleted")
    return redirect(url_for("cuisines", username=username))


# Prevent force URL of functions developed for Users.
def block_force_url(block_username):
    if session.get('user'):
        if block_username != session["user"]:
            return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


# Prevent force URL of functions developed for Admin.
def block_force_url_admin(block_username):
    if session.get('user'):
        if block_username != session["user"]:
            return redirect(url_for("home"))
        if block_username != "admin":
            return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)  # Set equals True for development only.
