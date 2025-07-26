from flask import Flask, request, jsonify
from chatbot.intents_handler import handle_query
from chatbot.data_loader import load_data

app = Flask(__name__)
data = load_data()  # Load dataset into memory

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("query")
    response = handle_query(user_input, data)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

