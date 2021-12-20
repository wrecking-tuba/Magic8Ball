# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Flask is working. Next: Magic 8 Ball!"

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

ANSWERS = [
    "It is certain.",
    "Without a doubt.",
    "You may rely on it.",
    "Yes – definitely.",
    "It is decidedly so.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don’t count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

@app.route("/", methods=["GET", "POST"])
def index():
    answer = None
    question = None

    if request.method == "POST":
        question = request.form.get("question", "").strip()
        if question:
            answer = random.choice(ANSWERS)

    return render_template("index.html", answer=answer, question=question)


# optional: API endpoint for ajax fetch
@app.route("/api/ask", methods=["POST"])
def api_ask():
    data = request.get_json(force=True)
    question = data.get("question", "").strip()
    if not question:
        return jsonify({"error": "question required"}), 400
    return jsonify({
        "question": question,
        "answer": random.choice(ANSWERS)
    })

if __name__ == "__main__":
    app.run(debug=True)
