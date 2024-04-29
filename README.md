# waifucards-scraper
A future scraper for waifucards.app witch only shows the characters that you have 1(one) or more cards of.

# Install
1. Install Python3: https://www.python.org/downloads/ (Linux already includes Python).
2. Copy and place the repo in a folder that you can easily reach, e.g. Documents.

# Usage
For now, it takes some manual work to make it work, but I am planning to make it a webscraper ... eventually.

1. Go to your user profile and click on album, or use the link and replace "[username]" with your username: https://waifucards.app/user/[username]?items=120&collection=has#cards-box
* Expand the view to 120 cards, or use the link and replace "[username]" with your username.
2. Inspect one of the waifu's:
![alt text](https://raw.githubusercontent.com/LavaLaugh/waifucards-scraper/main/images/Inspect.png "Inspect waifu")

3. Find the "card-frame" class and copy the inner HTML of the class:
![alt text](https://raw.githubusercontent.com/LavaLaugh/waifucards-scraper/main/images/inner-HTML.png "Inner HTML")

4. Paste it in the "cards.txt" file.
5. (Optional) If you have more than 120 cards, do it all over again, but on the next page and append the cards.txt file with the next page page etc.
6. Run main.py
7. Open cards.csv and use "|" as a custom delimiter (Some shows use a comma and the pipe symbol was the only real option).
8. Enjoy!
