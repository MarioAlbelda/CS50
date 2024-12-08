import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(
        r'^<iframe( width="\d{3}" height="\d{3}")? src="(?P<url1>https?)://(www\.)?youtube\.com/embed(?P<url2>/\w{11})"( title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen)?></iframe>$',
        s,
    ):
        url1 = matches.group("url1")
        if not url1.endswith("s"):
            url1 = url1 + "s"
        url = url1 + "://youtu.be" + matches.group("url2")
        return url
    else:
        return None


if __name__ == "__main__":
    main()
