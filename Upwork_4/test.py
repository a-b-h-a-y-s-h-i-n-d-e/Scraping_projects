from urllib.parse import urlsplit

url = "https://m2picks.blogabet.com/"

# Extract the subdomain from the URL
subdomain = urlsplit(url).hostname.split('.')[0]

print(subdomain)

