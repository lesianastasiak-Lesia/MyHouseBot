select("div.listing-card"):
        try:
            title = card.select_one("h2.title").get_text(strip=True)
            price = card.select_one("span.price").get_text(strip=True)
            link = "https://www.housesigma.com" + card.select_one("a").get("href")
            beds = card.select_one("span.bedrooms").get_text(strip=True)
            sqft = card.select_one("span.sqft").get_text(strip=True)

            price_num = int(''.join(filter(str.isdigit, price)))
            beds_num = int(''.join(filter(str.isdigit, beds)))
            sqft_num = int(''.join(filter(str.isdigit, sqft)))

            if (criteria["price_min"] <= price_num <= criteria["price_max"] and
                beds_num >= criteria["bedrooms_min"] and
                sqft_num <= criteria["max_sqft"]):
                results.append({"title": title, "price": price, "bedrooms": beds, "sqft": sqft, "link": link})
        except:
            continue
    return results

def extract_remax(soup):
    results = []
    if not soup: return results
    for card in soup.select("div.property-card"):
        try:
            title = card.select_one("h2.property-address").get_text(strip=True)
            price = card.select_one("span.price").get_text(strip=True)
            link = card.select_one("a").get("href")
            beds = card.select_one("li.bedrooms").get_text(strip=True)
            sqft = card.select_one("li.sqft").get_text(strip=True)

            price_num = int(''.join(filter(str.isdigit, price)))
            beds_num = int(''.join(filter(str.isdigit, beds)))
            sqft_num = int(''.join(filter(str.isdigit, sqft)))

            if (criteria["price_min"] <= price_num <= criteria["price_max"] and
                beds_num >= criteria["bedrooms_min"] and
                sqft_num <= criteria["max_sqft"]):
                results.append({"title": title, "price": price, "bedrooms": beds, "sqft": sqft, "link": link})
        except:
            continue
    return results

def extract_zillow(soup):
    results = []
    if not soup: return results
    for card in soup.select("article.list-card"):
        try:
            title = card.select_one("address.list-card-addr").get_text(strip=True)
            price = card.select_one("div.list-card-price").get_text(strip=True)
            link = card.select_one("a.list-card-link").get("href")
            beds = card.select_one("ul.list-card-details li:nth-child(1)").get_text(strip=True)
            sqft = card.select_one("ul.list-card-details li:nth-child(3)").get_text(strip=True)

            price_num = int(''.join(filter(str.isdigit, price)))
            beds_num = int(''.join(filter(str.isdigit, beds)))
            sqft_num = int(''.join(filter(str.isdigit, sqft)))

            if (criteria["price_min"] <= price_num <= criteria["price_max"] and
                beds_num >= criteria["bedrooms_min"] and
                sqft_num <= criteria["max_sqft"]):
                results.append({"title": title, "price": price, "bedrooms": beds, "sqft": sqft, "link": link})
        except:
            continue
    return results

extractors = {
    "Realtor": extract_realtor,
    "Zolo": extract_zolo,
    "HouseSigma": extract_housesigma,
    "Remax": extract_remax,
    "Zillow": extract_zillow
}

# -------- MAIN ASYNC FUNCTION --------
async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()

        for city in cities:
            city_url = city.replace(" ", "-")
            for site_name, url_template in sites.items():
                url = url_template.format(city=city_url)
                soup = await fetch_page(url, page)
                houses = extractors[site_name](soup)

                for h in houses:
                    body = f"""
City: {city}
Site: {site_name}
Title: {h['title']}
Price: {h['price']}
Bedrooms: {h['bedrooms']}
SqFt: {h['sqft']}
Link: {h['link']}
"""
                    send_email("New House Found!", body)
        await browser.close()

if name == "__main__":
    asyncio.run(main())
