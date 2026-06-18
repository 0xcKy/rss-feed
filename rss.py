import feedparser

rss_url = ['https://filestore.fortinet.com/fortiguard/rss/outbreakalert.xml', 'https://filestore.fortinet.com/fortiguard/rss/ir.xml', 'https://filestore.fortinet.com/fortiguard/rss/threatsignal.xml']

for i in rss_url:
    feed = feedparser.parse(i)
    if feed.status == 200:
        print(f"Feed Title: %s" %(feed.feed.title))
        print(f"Published: %s\n" %(feed.feed.published))
        for entry in feed.entries:
            print(f"<p><strong>[+] %s - %s [+]</strong></p>\n%s\n" %(entry.title, entry.link, entry.description))
    else:
        print("Failed to get RSS feed. Status code:", feed.status)
