import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["price"]
        response = openai.Completion.create(
        model="text-curie-001",
        prompt=generate_prompt(animal),
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """"suggest 3 best laptop under the given price

price: 50000
Names : 1. Asus VivoBook 14 (M413IA-EK997T),\n
        2. HP Pavilion x360 14 (db0044TU),\n
        3. Dell Inspiron 5593 (i5011-A5075GR-SL)\n
price: {}
Names:""".format(
        animal.capitalize()
    )
