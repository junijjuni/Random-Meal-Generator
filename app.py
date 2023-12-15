from flask import Flask, render_template, request, jsonify
import requests
import random

app = Flask(__name__)

def get_random_meal(diet, cuisine, meal_type):
    url = f"https://www.themealdb.com/api/json/v1/1/random.php"
    params = {
        "c": cuisine,
        "d": diet,
    }

    if meal_type:
        params["t"] = meal_type

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        meal = data["meals"][0]
        meal_name = meal["strMeal"]
        meal_image = meal["strMealThumb"]
        meal_ingredients = [meal[f"strIngredient{i}"] for i in range(1, 21) if meal[f"strIngredient{i}"]]
        return {"name": meal_name, "image": meal_image, "ingredients": meal_ingredients}
    else:
        return None
    
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_random_meal", methods=["POST"])
def get_random_meal_route():
    diet_option = request.form.get("diet_option")
    cuisine_type = request.form.get("cuisine_type")
    meal_type = request.form.get("meal_type")  # Get the selected meal type

    meal_info = get_random_meal(diet_option, cuisine_type, meal_type)
    if meal_info:
        return jsonify(meal_info)
    else:
        return jsonify({"error": "Could not find a meal with the given options."})


if __name__ == "__main__":
    app.run(debug=True)