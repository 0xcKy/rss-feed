import feedparser

rss_url = ['https://filestore.fortinet.com/fortiguard/rss/outbreakalert.xml', 'https://filestore.fortinet.com/fortiguard/rss/ir.xml', 'https://filestore.fortinet.com/fortiguard/rss/threatsignal.xml']
filename = "intelligence_report.html"

def get_rss():
    result_header = "<html lang=\"pt-BR\"><head><meta charset=\"UTF-8\"><title>Intelligence Report</title></head>\n"
    result_string = ""
    result_end = "\n</html>"
    for i in rss_url:
        rss_feed = feedparser.parse(i)
        if rss_feed.status == 200:
            result_string+=(f"<p>Feed Title: %s</p>" %(rss_feed.feed.title))
            result_string+=(f"Published: %s" %(rss_feed.feed.published))
            for entry in rss_feed.entries:
                result_string+=("<p><strong>[+] %s - <a href=\"%s\" rel=\"noopener noreferrer nofollow\" target=\"_blank\">Link de refer&ecirc;ncia</a> [+]</strong></p>\n%s\n" %(entry.title, entry.link, entry.description))
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
