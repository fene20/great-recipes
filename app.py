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


@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    # list() converts Mongo Cursor Object to a list.
    # I.e. so commented out code cannot be read by Jinja
    recipes = list(mongo.db.recipes.find({"is_published": "yes"}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/generate_index", methods=["GET", "POST"])
def generate_index():
    if request.method == "POST":
        mongo.db.recipes.create_index([(
            "recipe_name", "text"), ("ingredients", "text")])
        flash("Search Index has been generated")
    recipes = list(mongo.db.recipes.find())
    return render_template("generate_index.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("recipes.html", recipes=recipes)


@app.route("/search_user/<username>", methods=["GET", "POST"])
def search_user(username):
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"created_by": username, "$text": {"$search": query}}))
    return render_template("my_recipes.html", username=username, recipes=recipes)


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


@app.route("/my_recipes/<username>", methods=["GET", "POST"])
def my_recipes(username):

    recipes = list(mongo.db.recipes.find())

    # Force attacker back to login if they try to force access
    # to someone else's Recipies by killing the session.
    if session["user"]:  # If session user cookie is true.
        return render_template("my_recipes.html", username=username, recipes=recipes)

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
        is_published = "yes" if request.form.get("is_published") else "off"
        recipe = {
            "cuisine_style": request.form.get("cuisine_style"),
            "recipe_name": request.form.get("recipe_name"),
            "picture": request.form.get("picture"),
            # Credit: Tutor support for .split()
            "ingredients": [i.strip() for i in request.form.get("ingredients").split(',')],
            "preperation_steps": [i.strip() for i in request.form.get("preperation_steps").split(',')],
            "tools_required": [i.strip() for i in request.form.get("tools_required").split(',')],
            "is_published": is_published,
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
        is_published = "yes" if request.form.get("is_published") else "off"
        submit = {
            "cuisine_style": request.form.get("cuisine_style"),
            "recipe_name": request.form.get("recipe_name"),
            "picture": request.form.get("picture"),
            "ingredients": request.form.get("ingredients"),
            "preperation_steps": request.form.get("preperation_steps"),
            "tools_required": request.form.get("tools_required"),
            "is_published": is_published,
            "created_by": session["user"]
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, submit)
        flash("Recipe Successfully Updated")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines = mongo.db.cuisines.find().sort("cuisine_style", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, cuisines=cuisines)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_cuisines")
def get_cuisines():
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_style", 1))
    # cuisines on LHS passed to temlpate, cuisines on RHS = list(mongo.db above
    return render_template("cuisines.html", cuisines=cuisines)


@app.route("/add_cuisine", methods=["GET", "POST"])
def add_cuisine():
    if request.method == "POST":
        cuisine = {
            "cuisine_style": request.form.get("cuisine_style")
        }
        mongo.db.cuisines.insert_one(cuisine)
        flash("New Cuisine Added")
        return redirect(url_for("get_cuisines"))

    return render_template("add_cuisine.html")


@app.route("/edit_cuisine/<cuisine_id>", methods=["GET", "POST"])
def edit_cuisine(cuisine_id):
    if request.method == "POST":
        submit = {
            "cuisine_style": request.form.get("cuisine_style")
        }
        mongo.db.cuisines.update({"_id": ObjectId(cuisine_id)}, submit)
        flash("Cuisine Successfully Updated")
        return redirect(url_for("get_cuisines"))

    cuisine = mongo.db.cuisines.find_one({"_id": ObjectId(cuisine_id)})
    return render_template("edit_cuisine.html", cuisine=cuisine)


@app.route("/delete_cuisine/<cuisine_id>")
def delete_cuisine(cuisine_id):
    mongo.db.cuisines.remove({"_id": ObjectId(cuisine_id)})
    flash("Cuisine Successfully Deleted")
    return redirect(url_for("get_cuisines"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)  # Set equals True for development only.
