```python
import requests

# Enter email to check
email = "lilyanavonel@gmail.com"
url = f"https://emailrep.io/{email}"

# Send request
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print("\n🔍 Email Reputation Analysis\n")
    print(f"📧 Email: {email}")
    print(f"✔ Reputation: {data['reputation']}")
    print(f"✔ Linked Accounts: {', '.join(data['details']['profiles']) if data['details']['profiles'] else 'None found'}")
    print(f"✔ Blacklisted: {'Yes' if data['details']['blacklisted'] else 'No'}")
    print(f"✔ Risk Level: {'High' if data['suspicious'] else 'Low'}")
else:
    print("❌ Error: Unable to fetch email reputation data.")

# Run the Script
python3 tools/email-reputation-checker.py
