import tkinter as tk

# Instagram FAQ database
faq_data = {
    "How do I reset my Instagram password?":
        "Go to the login screen > Tap 'Forgot password?' > Follow the instructions to reset it.",
    "How do I delete my Instagram account?":
        "Visit instagram.com/accounts/remove/request/permanent on a browser and follow the steps.",
    "How can I recover a hacked account?":
        "Use the 'Get help logging in' option and follow security steps. Contact support if needed.",
    "How do I make my account private?":
        "Go to Profile > Settings > Privacy > Toggle 'Private Account' on.",
    "How do I block or report someone?":
        "Go to their profile > Tap the three dots > Choose Block or Report.",
    "Why was my post removed?":
        "Posts may be removed if they violate Instagram's Community Guidelines.",
    "How do I add music to my story?":
        "When creating a story, tap the sticker icon and select 'Music' to add a track.",
    "How do I verify my Instagram account?":
        "Go to Settings > Account > Request Verification and follow the steps.",
    "Why can't I follow people or like posts?":
        "You may have reached a temporary action limit or your account is restricted.",
    "How can I check if Instagram is down?":
        "Use websites like downdetector.com or check Instagram’s official Twitter for updates."
}

# GUI setup
root = tk.Tk()
root.title("FAQ Chatbot")
root.geometry("600x450")

# Title label
title_label = tk.Label(root, text="📱 Instagram FAQ Chatbot", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Dropdown menu
question_var = tk.StringVar(root)
question_var.set("Select a question")

def show_dropdown_answer(*args):
    selected = question_var.get()
    if selected in faq_data:
        response_label.config(text="Bot: " + faq_data[selected])
    else:
        response_label.config(text="")

dropdown = tk.OptionMenu(root, question_var, *faq_data.keys())
dropdown.config(width=60, font=("Arial", 11))
dropdown.pack(pady=10)

question_var.trace("w", show_dropdown_answer)

# Response display label
response_label = tk.Label(root, text="", wraplength=550, font=("Arial", 12), fg="blue", justify="left")
response_label.pack(pady=10)

# Manual input
entry_label = tk.Label(root, text="Or ask your own question below:", font=("Arial", 12))
entry_label.pack(pady=5)

manual_entry = tk.Entry(root, font=("Arial", 12), width=60)
manual_entry.pack(pady=5)

# Ask button
def answer_manual_question():
    user_question = manual_entry.get().strip().lower()
    found = False
    for q, a in faq_data.items():
        if user_question in q.lower():
            response_label.config(text="Bot: " + a)
            found = True
            break
    if not found:
        response_label.config(text="Bot: Sorry, I don't have an answer for that.")

ask_btn = tk.Button(root, text="Ask", command=answer_manual_question, font=("Arial", 12))
ask_btn.pack(pady=10)

root.mainloop()
