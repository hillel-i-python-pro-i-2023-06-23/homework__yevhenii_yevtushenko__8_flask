import csv
import pathlib

import requests
from flask import Flask

from modules.config import FILES_INPUT_DIR
from modules.services.genetate_user import generate_users

app = Flask(__name__)


@app.route("/")
def hello_world():  # put application's code here
    return "Hello World!"


@app.route("/get-content/")
def read_file(file_path: pathlib.Path = None):
    content = ""
    if file_path is None:
        file_path = FILES_INPUT_DIR.joinpath("test.txt")
    with open(file_path) as file:
        for line in file:
            content += line

    return content


@app.route("/generate-users/")
def show_users():
    users = generate_users(100)
    users_formatted = []
    for user in users:
        user_formatted = f"<li><b>{user.name}</b> - <span>{user.email}</span></li>"
        users_formatted.append(user_formatted)
    _temp = "\n".join(users_formatted)
    return f"<ol>{_temp}</ol>"


@app.route("/space/")
def response():
    url = "http://api.open-notify.org/astros.json"
    data = requests.get(url).json()
    names = [person["name"] for person in data["people"]]
    output_str = f"Total in cosmos:{len(names)}"
    return output_str


@app.route("/mean/")
def read_csv_file(url: str = "https://drive.google.com/uc?export=download&id=13nk_FYpcayUck2Ctrela5Tjt9JQbjznt"):
    with requests.get(url) as data:
        csv_reader = csv.DictReader(data.text.splitlines())
        temp_weight = []
        temp_height = []

        for row in csv_reader:
            temp_weight.append(float(row["Weight(Pounds)"]) * 0.453592)
            temp_height.append(float(row["Height(Inches)"]) * 2.54)

        return (
            f"Average Height (cm): {sum(temp_height) / len(temp_height):.2f}"
            f"Average Weight (kg): {sum(temp_weight) / len(temp_weight):.2f}"
        )


if __name__ == "__main__":
    app.run()
