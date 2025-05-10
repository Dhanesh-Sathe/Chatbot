import re

# Example product catalog with product names and their links
products = {
    "led bulb": "https://sathetelecom.com/products/led-bulb",
    "mobile charger": "https://sathetelecom.com/products/mobile-charger",
    "ceiling fan": "https://sathetelecom.com/products/ceiling-fan",
    "earphones": "https://sathetelecom.com/products/earphones",
    "adapter": "https://sathetelecom.com/products/adapter",
    "switch": "https://sathetelecom.com/products/switch",
    "wire": "https://sathetelecom.com/products/wire",
    "mobile phone": "https://sathetelecom.com/products/mobile-phone"
}

def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    # Check if the user is asking about a specific product
    for product, link in products.items():
        if product in user_input:
            return f"Yes, we have {product.title()}! You can view details or buy here: {link}"

    # General responses
    responses = {
        r"\b(hello|hi|hey)\b": "Hello! Welcome to Sathe Telecom. How can I assist you today?",
        r"\b(how are you)\b": "I'm here to help you with your electrical and electronics needs at Sathe Telecom.",
        r"\b(products|what do you sell|available items|electronics|electrical)\b": (
            "We offer a wide range of products: mobile phones, chargers, adapters, earphones, LED bulbs, fans, switches, wires, and more. "
            "If you mention a product name, I can share a direct link!"
        ),
        r"\b(brand|brands|which brands)\b": "We stock top brands like Samsung, Philips, Havells, Syska, Bajaj, MI, and more.",
        r"\b(price|cost|how much)\b": "Product prices vary by brand and model. Please mention the product you're interested in for details.",
        r"\b(warranty|guarantee)\b": "Most products come with a manufacturer warranty. Would you like to know the warranty for a specific item?",
        r"\b(payment|payment methods|how to pay)\b": "We accept cash, UPI, credit/debit cards, and net banking.",
        r"\b(offers|discounts|sale)\b": "We have special discounts on select products. Ask for today's deals or specify a product for offer details.",
        r"\b(order|buy|purchase)\b": "You can visit our shop or place an order by calling us. Home delivery is available for select items.",
        r"\b(track order|order status|delivery status)\b": "Please provide your order number, and I'll check the status for you.",
        r"\b(return|exchange|refund)\b": "Returns and exchanges are accepted within 7 days for eligible products. Please keep your bill for reference.",
        r"\b(repair|service|fix|maintenance)\b": "We offer repair and servicing for select electronics. Please specify your product and issue.",
        r"\b(location|address|where are you)\b": "Sathe Telecom is located at Main Market, [Your City]. Need directions?",
        r"\b(timing|hours|open|close|working hours)\b": "We are open Monday to Saturday, 10 AM to 8 PM.",
        r"\b(contact|phone number|call)\b": "You can reach us at 98765-43210 for any queries or orders.",
        r"\b(bye|exit|goodbye)\b": "Thank you for visiting Sathe Telecom! Have a great day."
    }

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    return (
        "I'm sorry, I couldn't understand that. "
        "Could you please rephrase or ask about our products or services? "
        "If you mention a product name, I can share a direct link!"
    )

# Chatbot interaction loop
print("Welcome to Sathe Telecom Chatbot! Type 'exit' to end the conversation.")

while True:
    user_message = input("You: ")
    if user_message.lower() in ["bye", "exit", "goodbye"]:
        print("Chatbot: Thank you for visiting Sathe Telecom! Have a great day.")
        break
    response = chatbot_response(user_message)
    print("Chatbot:", response)
