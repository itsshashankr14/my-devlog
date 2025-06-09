# Problem Statement:
# You are given an HTML code snippet of N lines.
# Your task is to detect and print all the HTML tags, attributes and attribute values.

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

    def handle_startendtag(self, tag, attrs):
        print(tag)
        for attr, value in attrs:
            print(f"-> {attr} > {value}")

if __name__ == "__main__":
    n = int(input())
    html_code = [input() for _ in range(n)]
    parser = MyHTMLParser()
    parser.feed('\n'.join(html_code))