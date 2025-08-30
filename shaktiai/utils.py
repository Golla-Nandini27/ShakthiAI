import pandas as pd
import os

DATA_FILE = "data/contributions.csv"

def save_contribution(text, lang):
    if not os.path.exists("data"):
        os.makedirs("data")
    df = pd.DataFrame([[text, lang]], columns=["Text", "Language"])
    if os.path.exists(DATA_FILE):
        df.to_csv(DATA_FILE, mode='a', header=False, index=False)
    else:
        df.to_csv(DATA_FILE, index=False)

def load_contributions():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame(columns=["Text", "Language"])

def get_safety_tip(hour):
    if 6 <= hour < 12:
        return "Morning Tip: Always inform someone before heading out."
    elif 12 <= hour < 18:
        return "Afternoon Tip: Be aware of your surroundings when traveling."
    elif 18 <= hour < 21:
        return "Evening Tip: Avoid isolated areas and stay in well-lit places."
    else:
        return "Night Tip: Share your location with a trusted contact."

def get_emergency_contacts(location):
    # Static data (you can extend with real APIs later)
    emergency_data = {
        "hyderabad": {
            "Women Helpline": "1091",
            "Police": "100",
            "She Team": "040-27852400"
        },
        "delhi": {
            "Women Helpline": "181",
            "Police": "100",
            "NGO Support": "1091"
        },
    }

    loc = location.strip().lower()
    if loc in emergency_data:
        contacts = emergency_data[loc]
        return "\n".join([f"**{k}**: {v}" for k, v in contacts.items()])
    else:
        return "Emergency contacts not available for this location. Try Hyderabad or Delhi."
