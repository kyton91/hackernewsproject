# 📊 Top Stories Scraper from Hacker News

This project is a Python-based **Hacker News Scraper** that collects and filters top news stories with **100 or more votes** from multiple pages on the [Hacker News](https://news.ycombinator.com/) website. It utilizes the `requests` library for HTTP requests, `BeautifulSoup` for HTML parsing, and filters results based on user votes.

---

## 📃 Features

1. **Multi-Page Scraping**
   - Scrapes stories from the first 4 pages of Hacker News (configurable).

2. **Vote Filtering**
   - Filters stories with **100 or more votes**.

3. **Ranked News Output**
   - Returns and prints the filtered news stories, sorted in descending order based on votes.

4. **Error Handling**
   - Handles HTTP request errors by checking response status codes.

5. **Customizable Sleep Interval**
   - Adds a 1-second delay between requests to avoid overloading the server.

---

## 🛠️ Technologies Used

- **Programming Language:** Python 3.x
- **Libraries:**
  - `requests` – To fetch the web pages.
  - `BeautifulSoup` – For parsing HTML content.
  - `pprint` – To print formatted output.
  - `time` – For adding delays between requests.

---

## ⚙️ Installation

Follow these steps to set up the project:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/hackernews-scraper.git
   cd hackernews-scraper
   ```

2. **Install Dependencies**
   Install the required Python libraries using `pip`:
   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the Script**
   Execute the script to fetch and display top stories:
   ```bash
   python hacker_news_scraper.py
   ```

---

## 🧩 Usage

- By default, the script scrapes the **first 4 pages** of Hacker News.
- Stories with **100 or more votes** are displayed, sorted by votes in descending order.

### Output Example:

```python
Stories having more than or equal to 100 votes:
[{'title': 'Example Story 1',
  'link': 'https://example.com/story1',
  'votes': 345},
 {'title': 'Example Story 2',
  'link': 'https://example.com/story2',
  'votes': 210}]
```

---

## 🔧 Code Explanation

1. **Fetching Pages:**
   - Iterates through the first 4 pages of Hacker News.
   - Requests each page and parses it using BeautifulSoup.

2. **Extracting Links and Votes:**
   - Extracts news titles, links, and vote counts.
   - Filters stories with 100+ votes.

3. **Sorting Stories:**
   - Sorts the filtered stories in descending order of votes.

4. **Output:**
   - Displays the final sorted list of news stories.

---

## 💡 Notes

- The `time.sleep(1)` delay prevents overloading the Hacker News server.
- Modify the `range(1,5)` to scrape more or fewer pages.

---

## 💼 License

This project is open-source and available under the **MIT License**.

---

## 📏 Author

- **Name:** [Your Name]
- **GitHub:** [YourUsername](https://github.com/yourusername)

---

## 🛠 Contribution

Contributions are welcome! If you find bugs or have ideas for improvements:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

---

## ✨ Acknowledgements

Special thanks to [Hacker News](https://news.ycombinator.com/) for providing the platform and content used in this project.
