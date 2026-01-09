import os
import requests
from bs4 import BeautifulSoup
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# === EMAIL SETTINGS ===
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
TO_EMAIL = os.environ.get("TO_EMAIL")
FROM_EMAIL = os.environ.get("FROM_EMAIL")

# === SEARCH CRITERIA ===
criteria = {
    "year_built_min": 1960,
    "bedrooms_min": 3,
    "price_min": 60000,
    "price_max": 120000,
    "max_sqft": 1500
}

# === CITIES ===
cities = [
    "Edmonton, AB", "London, ON", "Red Deer, AB", "Regina, SK",
    "Airdrie, AB", "Calgary, AB", "Windsor, ON", "Wood Buffalo, AB",
    "Quebec, QC", "St. John's, NL", "Saskatoon, SK", "Brantford, ON",
    "Montreal, QC", "Hamilton, ON", "Peterborough, ON", "Winnipeg, MB",
    "Kingston, ON", "Oshawa, ON", "Ottawa, ON", "Barrie, ON",
    "Kitchener, ON", "Victoria, BC", "Moncton, NB", "Gatineau, QC",
    "Kelowna, BC", "St. Catharines, ON", "Ajax, ON"
]

# === REAL ESTATE SITES ===
sites = [
    "https://www.realtor.ca/",
    "https://www.housesigma.com/",
    "https://www.zolo.ca/",
    "https://www.remax.ca/",
    "https://www.zillow.com/"
]

# === FUNCTION TO SEND EMAIL ===
def send_email(subject, content):
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject=subject,
        plain_text_content=content
    )
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    sg.send(message)

# === FUNCTION TO CHECK SITES ===
def check_sites():
    for city in cities:
        for site in sites:
            # TODO: add real parsing logic for each site
            # This is an example placeholder
            found_house = f"Example house in {city} on {site} matching criteria"
            
            # Send email notification
            send_email("New House Found!", found_house)

# === RUN BOT ===
if name == "__main__":
    check_sites()
