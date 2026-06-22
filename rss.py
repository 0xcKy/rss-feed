import feedparser
from pprint import pprint

rss_url = ['https://feedexample.com/feed.xml'] #list with feeds
filename = "intel_report.html"

def get_rss():
    result_header = "<html lang=\"pt-BR\"><head><meta charset=\"UTF-8\"><title>Intelligence Report</title></head>\n"
    result_string = ""
    result_end = "\n</html>"
    for i in rss_url:
        rss_feed = feedparser.parse(i)
        if rss_feed.status == 200:
            result_string+=(f"<h2>Feed Title: %s</h2>" %(rss_feed.feed.title))
            try:
                result_string+=(f"<strong>Published: %s</strong>" %(rss_feed.feed.published))
            except:
                pass
            for entry in rss_feed.entries:
                result_string+=("<p><strong>[+] %s - <a href=\"%s\" rel=\"noopener noreferrer nofollow\" target=\"_blank\">Link de refer&ecirc;ncia</a> [+]</strong><br>%s</p>" %(entry.title, entry.link, entry.description))
        else:
            print("Failed to get RSS feed. Status code:", rss_feed.status)
    write_file(result_header+result_string+result_end)

def write_file(i):
    with open(str(filename), 'w+') as f:
        f.write('%s\n' %i)
        print("File written successfully")
        f.close()

if __name__ == '__main__':
    get_rss()
