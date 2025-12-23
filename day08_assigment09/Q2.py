# import required packages
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
chat_history = []

# start selenium browser
driver = webdriver.Chrome()

# open DuckDuckGo
driver.get("https://duckduckgo.com/")
print("Page Title:", driver.title)

driver.implicitly_wait(5)

# search Sunbeam Pune
search_box = driver.find_element(By.ID, "searchbox_input")
search_box.send_keys("Sunbeam Pune Internship")
search_box.send_keys(Keys.RETURN)

time.sleep(3)

# click first result
driver.find_element(By.ID, "r1-0").click()
time.sleep(5)

# click Internship link
driver.find_element(By.PARTIAL_LINK_TEXT, "Intern").click()
time.sleep(5)

# scroll page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

# ---------------- REAL SCRAPING ----------------
page_text = driver.find_element(By.TAG_NAME, "body").text.lower()

print("\nSunbeam Web Scraping Agent")
print("Type 'exit' to stop\n")

# ---------------- USER QUERY LOOP ----------------
while True:
    question = input("Ask about Sunbeam internships or batches: ").lower()

    if question == "exit":
        break

    # ---------- ANSWER FROM SCRAPED DATA ----------
    if "internship" in question:
        if "internship" in page_text:
            answer = (
                "I checked the Sunbeam website content. "
                "The website clearly mentions internship programs. "
                "These internships are mainly related to IT and software training."
            )
        else:
            answer = (
                "I searched the website, but internship information "
                "was not clearly found on this page."
            )

    elif "batch" in question:
        if "batch" in page_text or "batches" in page_text:
            answer = (
                "I checked the Sunbeam website text. "
                "The website mentions multiple training batches. "
                "Sunbeam regularly runs batches for different IT courses."
            )
        else:
            answer = (
                "I searched the website, but batch information "
                "was not clearly available on this page."
            )

    else:
        answer = (
            "I checked the Sunbeam website, but your question does not "
            "match internship or batch information."
        )

    # save chat history
    chat_history.append(("User", question))
    chat_history.append(("Agent", answer))

    print("\nAnswer:")
    print(answer)
    print("-" * 50)

# ---------------- DISPLAY CHAT HISTORY ----------------
print("\nComplete Chat History:\n")

for role, message in chat_history:
    print(f"{role}: {message}")

# close browser
driver.quit()
