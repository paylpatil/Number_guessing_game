from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # Generate a random number between 1 and 9
    number = random.randint(1, 9)
    chances = 0
    message = "Guess a number between 1 and 9:"

    if request.method == "POST":
        guess = int(request.form["guess"])
        chances += 1
        
        if guess == number:
            message = f"CONGRATULATIONS! YOU GUESSED THE NUMBER {number} IN {chances} ATTEMPTS!"
        elif guess < number:
            message = f"Your guess was too low! Try a higher number."
        else:
            message = f"Your guess was too high! Try a lower number."
        
        return render_template("index.html", message=message, chances=chances, number=number)

    return render_template("index.html", message=message, chances=chances)

if __name__ == "__main__":
    app.run(debug=True)
