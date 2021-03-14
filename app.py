import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
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
def index():
    recipes = list(mongo.db.recipes.find())
    # Shows the first three recipes for mobile
    mobile_recipes = mongo.db.recipes.aggregate([{"$sample": {"size": 4}}])
    return render_template(
        "index.html", recipes=recipes, mobile_recipes=mobile_recipes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Only users can access their profile
    if not session.get("user"):
        return render_template("error_handle/404.html")

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        # Admin has acces to all recipes
        if session["user"] == "admin":
            user_recipe = list(mongo.db.recipes.find())
        else:
            # user sees own recipes
            user_recipe = list(
                mongo.db.recipes.find({"author": session["user"]}))

        return render_template(
            "profile.html", username=username, user_recipe=user_recipe)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/get_recipes")
def get_recipes():
    # sort the names of the breads list #
    recipes = list(mongo.db.recipes.find())
    flash("All menus")
    return render_template("get_recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("get_recipes.html", recipes=recipes)


@app.route("/cuisines")
def cuisines():
    return render_template("cuisines.html")


@app.route("/get_recipe/<recipe_id>")
def get_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # recipe id don't exist, show 404 error
    if not recipe:
        return render_template("error_handle/404.html")

    return render_template("get_recipe.html", recipe=recipe)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    # Only users can edit recipes
    if not session.get("user"):
        return render_template("error_handle/404.html")

    if request.method == "POST":
        vegan = "on" if request.form.get("vegan") else "off"
        recipe = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "img_url": request.form.get("img_url"),
            "simple_description": request.form.get("simple_description"),
            "vegan": vegan,
            "prep_duration": request.form.get("prep_duration"),
            "cook_duration": request.form.get("cook_duration"),
            "cuisine": request.form.get("cuisine"),
            "date_posted": request.form.get("date_posted"),
            "ingredients": request.form.get("ingredients"),
            "adult_plates": request.form.get("adult_plates"),
            "cook_direction": request.form.get("cook_direction"),
            "author": session["user"],
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    cuisines=  mongo.db.cusisines.find().sort("cuisine_name", 1)
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    # Only users can edit recipes
    if not session.get("user"):
        return render_template("error_handle/404.html")

    # Edit recipe to db
    if request.method == "POST":
        vegan = "on" if request.form.get("vegan") else "off"
        edits = {
            "category_name": request.form.get("category_name"),
            "recipe_name": request.form.get("recipe_name"),
            "img_url": request.form.get("img_url"),
            "simple_description": request.form.get("simple_description"),
            "vegan": vegan,
            "prep_duration": request.form.get("prep_duration"),
            "cook_duration": request.form.get("cook_duration"),
            "cuisine": request.form.get("cusine"),
            "date_posted": request.form.get("date_posted"),
            "ingredients": request.form.get("ingredients"),
            "adult_plates": request.form.get("adult_plates"),
            "cook_direction": request.form.get("cook_direction"),
            "author": session["user"],
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edits)
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_recipes"))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    # Delete recipe from db
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipes"))


@app.route("/get_categories")
def get_categories():
    # Only admin can access categories
    if not session.get("user") == "admin":
        return render_template("error_handle/404.html")

    # Find categories from db
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("get_categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    # Only admin can access categories
    if not session.get("user") == "admin":
        return render_template("error_handle/404.html")

    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
     # Only admin can access categories
    if not session.get("user") == "admin":
        return render_template("error_handle/404.html")

    if request.method == "POST":
        submit = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.update({"_id": ObjectId(category_id)}, submit)
        flash("Category Successfully Updated")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    # Only admin can access categories
    if not session.get("user") == "admin":
        return render_template("error_handle/404.html")

    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
