import time

def welcome():
    print("="*50)
    print("🤖 Welcome to our E-Commerce Policy Chatbot!")
    name = input("👤 May I know your name? ")
    print(f"Hello, {name}! How can I assist you today?")
    print("Type 'help' anytime to see topics or 'exit' to quit.")
    print("="*50)
    return name

def show_help():
    print("\nHere are some topics you can ask about:")
    print("1️⃣ Return Policy")
    print("2️⃣ Delivery & Shipping")
    print("3️⃣ Payment Methods & COD")
    print("4️⃣ Order Cancellation")
    print("5️⃣ Refunds")
    print("6️⃣ Damaged or Wrong Products")
    print("7️⃣ Warranty")
    print("8️⃣ Offers & Coupons\n")

def chatbot():
    name = welcome()
    last_answer = None

    while True:
        user_input = input(f"{name}: ").lower()

        if 'exit' in user_input:
            print("🤖 Bot: Thank you for chatting with us! Have a great day! 👋")
            break

        elif user_input in ['help', 'menu']:
            show_help()

        elif 'return' in user_input:
            ans = "Returns are accepted within 7 days of delivery. Pickup is scheduled within 3 business days of approval."
            print("🤖 Bot:", ans)
            last_answer = ans

        elif 'delivery' in user_input or 'shipping' in user_input:
            ans = "Delivery takes 5–7 business days. Delays can happen due to weather or logistics issues."
            print("🤖 Bot:", ans)
            last_answer = ans

        elif 'payment' in user_input or 'cod' in user_input:
            ans = "We accept Credit/Debit cards, Net Banking, UPI, Wallets, and COD for orders below ₹10,000."
            print("🤖 Bot:", ans)
            last_answer = ans

        elif 'cancel' in user_input:
            ans = "Orders can be cancelled before shipment. Once shipped, please follow the return process."
            print("🤖 Bot:", ans)
            last_answer = ans

        elif 'refund' in user_input:
            ans = "Refunds are processed within 5–10 business days after verification, to your original payment method."
            print("🤖 Bot:", ans)
            last_answer = ans

        elif 'damage' in user_input or 'wrong' in user_input:
            ans = "Please report any damage or incorrect product with photo evidence within 48 hours of delivery."
            print("🤖 Bot:", ans)
            last_answer = ans

        elif 'warranty' in user_input:
            ans = "For warranty claims, please contact the manufacturer directly."
            print("🤖 Bot:", ans)
            last_answer = ans

        elif 'offer' in user_input or 'coupon' in user_input:
            ans = "Discounts and offers are valid only during the promotional period. Only one coupon per order is allowed unless specified."
            print("🤖 Bot:", ans)
            last_answer = ans

        elif 'repeat' in user_input:
            if last_answer:
                print("🤖 Bot (repeating):", last_answer)
            else:
                print("🤖 Bot: I haven't answered anything yet to repeat!")

        elif 'hi' in user_input or 'hello' in user_input:
            print(f"🤖 Bot: Hi {name}! How can I help you today?")

        elif 'thanks' in user_input or 'thank you' in user_input:
            print("🤖 Bot: You're welcome! 😊")

        else:
            print("🤖 Bot: I'm sorry, I didn't quite catch that. Please type 'help' to see topics.")

chatbot()
