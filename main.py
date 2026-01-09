import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Email settings
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY")
TO_EMAIL = os.environ.get("TO_EMAIL")
FROM_EMAIL = os.environ.get("FROM_EMAIL")

# Search criteria
criteria = {
    "year_built_min": 1960,
    "bedrooms_min": 3,
    "price_min": 60000,
    "price_max": 120000,
    "max_sqft": 1500
}

# Cities to search
cities = [
    "Edmonton, AB", "London, ON", "Red Deer, AB", "Regina, SK",
    "Airdrie, AB", "Calgary, AB", "Windsor, ON", "Wood Buffalo, AB",
    "Quebec, QC", "St. John's, NL", "Saskatoon, SK", "Brantford, ON",
    "Montreal, QC", "Hamilton, ON", "Peterborough, ON", "Winnipeg, MB",
    "Kingston, ON", "Oshawa, ON", "Ottawa, ON", "Barrie, ON",
    "Kitchener, ON", "Victoria, BC", "Moncton, NB", "Gatineau, QC",
    "Kelowna, BC", "St. Catharines, ON", "Ajax, ON"
]

# Real estate sites
sites = [
    "https://www.realtor.ca/",
    "https://www.housesigma.com/",
    "https://www.zolo.ca/",
    "https://www.remax.ca/",
    "https://www.zillow.com/"
]

# Function to send email
def send_email(subject, content):
    message = Mail(
        from_email=FROM_EMAIL,
        to_emails=TO_EMAIL,
        subject=subject,
        plain_text_content=content
    )
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    sg.send(message)

# Function to check sites
def check_sites():
    for city in cities:
        for site in sites:
            # Example placeholder
            found_house = f"Example house in {city} on {site} matching criteria"
            send_email("New House Found!", found_house)

# Run the bot
if __name__=="__main__":
    check_sites()
