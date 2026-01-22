from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def get_bot_response(user_input, last_answer=None):
    user_input = user_input.lower()

    if 'return' in user_input:
        return "Returns are accepted within 7 days of delivery. Pickup is scheduled within 3 business days of approval."

    elif 'delivery' in user_input or 'shipping' in user_input:
        return "Delivery takes 5–7 business days. Delays can happen due to weather or logistics issues."

    elif 'payment' in user_input or 'cod' in user_input:
        return "We accept Credit/Debit cards, Net Banking, UPI, Wallets, and COD for orders below ₹10,000."

    elif 'cancel' in user_input:
        return "Orders can be cancelled before shipment. Once shipped, please follow the return process."

    elif 'refund' in user_input:
        return "Refunds are processed within 5–10 business days after verification."

    elif 'damage' in user_input or 'wrong' in user_input:
        return "Please report damaged or incorrect products with photos within 48 hours."

    elif 'warranty' in user_input:
        return "For warranty claims, please contact the manufacturer."

    elif 'offer' in user_input or 'coupon' in user_input:
        return "Only one coupon per order unless specified. Offers are time-limited."

    elif 'help' in user_input:
        return (
            "You can ask about:\n"
            "• Return Policy\n"
            "• Delivery & Shipping\n"
            "• Payments & COD\n"
            "• Order Cancellation\n"
            "• Refunds\n"
            "• Warranty\n"
            "• Offers & Coupons"
        )

    elif 'hi' in user_input or 'hello' in user_input:
        return "Hello! How can I assist you today?"

    elif 'thanks' in user_input or 'thank you' in user_input:
        return "You're welcome 😊"

    else:
        return "Sorry, I didn't understand that. Type 'help' to see available topics."

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    last_answer = data.get("last_answer", None)

    bot_reply = get_bot_response(user_message, last_answer)

    return jsonify({
        "reply": bot_reply
    })

if __name__ == "__main__":
    app.run(debug=True)
