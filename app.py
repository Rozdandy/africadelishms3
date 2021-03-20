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

# -------------------------------------------------- CONFIGURATION #
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
def index():
    """ HOMEPAGE """
    recipes = list(mongo.db.recipes.find())
    mobile_recipes = mongo.db.recipes.aggregate([{"$sample": {"size": 4}}])
    # Shows the first three recipes for mobile
    return render_template(
        "index.html", recipes=recipes, mobile_recipes=mobile_recipes)


# ------------------------------------------------------------- USERS #
@app.route("/register", methods=["GET", "POST"])
def register():
    """ REGISTER FOR NEW UNSERS"""
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # sign up new user in db
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
    """ LOGIN """
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
    """ USERS PROFILE """
    # Only users can access their profile
    if not session.get("user"):
        return render_template("error_handle/404.html")

    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        # Admin has acces to all recipes
        if session["user"] == "admin":
            uza = list(mongo.db.recipes.find())
        else:
            # user sees own recipes
            uza = list(
                mongo.db.recipes.find({"author": session["user"]}))

        return render_template("profile.html", username=username, uza=uza)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """            LOGOUT """
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# ------------------------------------------------------------- RECIPES #
@app.route("/get_recipez/<category>")
def get_recipez(category):
    """             ALL RECIPES AND CATEGORIES OF RECIPES """
    if category == "all":
        recipes = list(mongo.db.recipes.find())
    elif category == "breakfast":
        recipes = list(mongo.db.recipes.find({"category_name": "breakfast"}))
    elif category == "lunch":
        recipes = list(mongo.db.recipes.find({"category_name": "Lunch"}))
    elif category == "dinner":
        recipes = list(mongo.db.recipes.find({"category_name": "Dinner"}))
    elif category == "appetizer":
        recipes = list(mongo.db.recipes.find({"category_name": "Appetizer"}))
    elif category == "dessert":
        recipes = list(mongo.db.recipes.find({"category_name": "Dessert"}))
    elif category == "drink":
        recipes = list(mongo.db.recipes.find({"category_name": "Drinks"}))
    elif category == "anytime":
        recipes = list(mongo.db.recipes.find({"category_name": "Anytime"}))
    else:
        recipes = mongo.db.recipe.find({"$text": {"$search": category}})
    return render_template(
        "get_recipez.html", recipes=recipes, category=category)


@app.route("/search", methods=["GET", "POST"])
def search():
    """       SEARCH FOR RECIPES """
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("get_recipez.html", recipes=recipes)


@app.route("/get_recipe/<recipe_id>")
def get_recipe(recipe_id):
    """               GETTING  RECIPE-PAGE """
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    # recipe id don't exist, 404 error message
    if not recipe:
        return render_template("error_handle/404.html")

    return render_template("get_recipe.html", recipe=recipe)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """            TO CREATE NEW RECIPES """
    # Only users can add recipes
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
            "cuisine_name": request.form.get("cuisine_name"),
            "date_posted": request.form.get("date_posted"),
            "ingredients": request.form.get("ingredients"),
            "adult_plates": request.form.get("adult_plates"),
            "cook_direction": request.form.get("cook_direction"),
            "author": session["user"],
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("get_recipez", category='all'))

    categories = mongo.db.categories.find().sort("category_name", 1)
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_name", 1))
    return render_template(
        "add_recipe.html", cuisines=cuisines, categories=categories)


@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    """                    EDIT EXISTING RECIPES """
    # Only users can edit recipes
    if not session.get("user"):
        return render_template("error_handle/404.html")

    # recipe to Edit
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
            "cuisine_name": request.form.get("cuisine_name"),
            "date_posted": request.form.get("date_posted"),
            "ingredients": request.form.get("ingredients"),
            "adult_plates": request.form.get("adult_plates"),
            "cook_direction": request.form.get("cook_direction"),
            "author": session["user"],
        }
        mongo.db.recipes.update({"_id": ObjectId(recipe_id)}, edits)
        flash("Recipe Successfully Updated")
        return redirect(url_for("get_recipez", category='all'))

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_name", 1))
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template(
        "edit_recipe.html",
        recipe=recipe, categories=categories, cuisines=cuisines)


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """                  TO DELETE RECIPES """
    # Delete recipe from db
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Successfully Deleted")
    return redirect(url_for("get_recipez", category='all'))


@app.route("/cusines")
def cuisines():
    cuisines = list(mongo.db.cuisines.find().sort("cuisine_name", 1))
    return render_template("cuisines.html", cuisines=cuisines)


@app.route("/get_categories")
def get_categories():
    # categories can only accessed by admin
    if not session.get("user") == "admin":
        return render_template("error_handle/404.html")

    # Find categories from db
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template(
        "get_categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """             TO ADD CATEGORIES """
    # Only admin can add categories
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
    """             EDIT CATEGORIES """
    #  Only admin can edit categories
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
    return render_template(
        "edit_category.html", category=category)


@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    """             TO DELETE CATEGORIES """
    # Only admin can delete categories
    if not session.get("user") == "admin":
        return render_template("error_handle/404.html")

    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Successfully Deleted")
    return redirect(url_for("get_categories"))


# ----------------------------------- ERROR FUNCTIONALITIES
@app.errorhandler(404)
def not_found(e):
    return render_template("error_handlers/404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("error_handlers/500.html"), 500


@app.errorhandler(403)
def forbidden(e):
    return render_template("error_handlers/403.html"), 403


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=False)
