import requests
import re

def get_news_headlines():
  """Scrape the news headlines from the BBC website."""
  url = "https://howtostartanllc.com/business-ideas/fruit-market"
  response = requests.get(url)
  html = response.content.decode("utf-8")

  headlines = []
  for match in re.finditer(r"<h3 class=\"gs-c-headline\">(.*?)</h3>", html):
    headlines.append(match.group(1))

  return headlines

def main():
  headlines = get_news_headlines()
  print("Fruit Market website headlines:")
  for headline in headlines:
    print(f"{headline}")

if __name__ == "__main__":
  main()
