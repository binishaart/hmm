from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    text = ""
    char_count = word_count = sentence_count = 0

    if request.method == "POST":
        text = request.form.get("text", "")
        char_count = len(text)
        word_count = len(text.split()) if text else 0
        sentence_count = text.count('.') + text.count('!') + text.count('?')

    return render_template("index.html",
                           text=text,
                           char_count=char_count,
                           word_count=word_count,
                           sentence_count=sentence_count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000,debug=True)
