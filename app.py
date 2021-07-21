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
env = env  # Get's rid of 'env' imported but unused error

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    # list() converts Mongo Cursor Object to a list.
    # I.e. so commented out code cannot be read by Jinja
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # else
        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)  # Insert a dictionary

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        # Pass user cookie to username in userrecipes template
        return redirect(url_for("my_recipes", username=session["user"]))

    return render_template("register.html")


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
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
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


@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    # Force attacker back to login if they try to force access
    # to someone else's Recipies by killing the session.
    if session["user"]:  # If session user cookie is true.
        return render_template("my_recipes.html", username=username)

    # If not true or does not exist.
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")  # Remove session cookie.
    return redirect(url_for("login"))


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        # Add is_published logic here and to edit recipe below.
        recipe = {
            "cuisine_style": request.form.get("cuisine_style"),
            "recipe_name": request.form.get("recipe_name"),
            "picture": request.form.get("picture"),
            # Change to 'request.form.getlist()' to read ingredients array etc.
            "ingredients": request.form.get("ingredients"),
            "preperation_steps": request.form.get("preperation_steps"),
            "tools_required": request.form.get("tools_required"),
            "is_published": "yes",
            "created_by": session["user"]
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    # IF POST above . . . . else GET here.
    cuisines = mongo.db.cuisines.find().sort("cuisine_style", 1)
    return render_template("add_recipe.html", cuisines=cuisines)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        # Add is_published logic here and to add recipe above.
        # recipe = {} changed to submit = {} as recipe =
        # mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)}) is used below
        submit = {
            "cuisine_style": request.form.get("cuisine_style"),
            "recipe_name": request.form.get("recipe_name"),
            "picture": request.form.get("picture"),
            # Change to 'request.form.getlist()' to read ingredients array etc.
            "ingredients": request.form.get("ingredients"),
            "preperation_steps": request.form.get("preperation_steps"),
            "tools_required": request.form.get("tools_required"),
            "is_published": "yes",
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines = mongo.db.cuisines.find().sort("cuisine_style", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, cuisines=cuisines)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # Set equals True for development only.
