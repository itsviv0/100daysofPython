from flask import Flask
import random


app = Flask(__name__)
random_number = random.randint(0, 9)
print(random_number)


@app.route("/")
def home_page():
    return (
        "<h1>Guess a number between 0 and 9</h1>"
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'
    )


@app.route("/<int:guess>")
def user_guess(guess):
    if guess < random_number:
        return (
            '<h1 style="color: green">Too low, try again.</h1>'
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZDRraW1jNjQ5em90czNvNnZjbjltd3N2d3k2cXhidDRraGhoNHdmZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/dKpEvFHdGsZBRuszpv/giphy.gif">'
        )
    elif guess == random_number:
        return (
            '<h1 style="color: green">Correct, you won!</h1>'
            '<img src="https://media.giphy.com/media/BPJmthQ3YRwD6QqcVD/giphy.gif?cid=790b7611qqpheszfm8dmwo5nrp3jmx6gexldtaqciznvkqal&ep=v1_gifs_search&rid=giphy.gif&ct=g">'
        )
    else:
        return (
            '<h1 style="color: green">Too high, try again.</h1>'
            '<img src="https://media.giphy.com/media/WtLa7qQ2JcL1kCiaFa/giphy.gif?cid=790b7611stuv8gjalkjuwl8no17iphbwqmuxvynsy8razcw6&ep=v1_gifs_search&rid=giphy.gif&ct=g" width=200>'
        )


if __name__ == "__main__":
    app.run(debug=True)
