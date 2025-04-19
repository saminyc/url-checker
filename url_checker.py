# Developed by Samin Chowdhury
# This url checker checks if url is secure.

def url_checker(url):
    if url.startswith("https://"):
        print(f'{url} uses HTTPS (secured).')
    elif url.startswith("http://"):
        print(f'{url} uses HTTP (Not secured).')
    else:
        print(f"{url} doesn't look like a complete url.")
        
if __name__=="__main__":
    user_input=input("Enter URL: ")
    url_checker(user_input)