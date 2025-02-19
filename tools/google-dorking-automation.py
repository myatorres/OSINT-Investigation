import webbrowser

# Email target
email = "lilyanavonel@gmail.com"

# Google Dorking Queries
queries = [
    f'"{email}" site:linkedin.com',
    f'"{email}" site:twitter.com',
    f'"{email}" site:reddit.com',
    f'"{email}" filetype:pdf',
]

# Open each query in a new browser tab
for query in queries:
    webbrowser.open(f"https://www.google.com/search?q={query}")

# Run the Script
python3 tools/google-dorking-automation.py
