from flask import Flask, render_template, request
import random

app = Flask(__name__)

# This number gets picked once when the server starts.
# (Later you can make it reset per game with "sessions" - not needed yet.)
secret_number = random.randint(1, 100)

@app.route("/", methods=["GET", "POST"])
def guessing_game():
    message = "Guess a number between 1 and 100!"

    if request.method == "POST":
        guess = int(request.form["guess"])

        if guess < 1 or guess > 100:
            message = "invalid input"
        elif guess < secret_number:
            message = "too low"
        elif guess > secret_number:
            message = "too high"
        else:
            message = f"🎉 you guessed the number! It was {secret_number}."

    return render_template("index.html", message=message)


if __name__ == "__main__":
    app.run(debug=True)

