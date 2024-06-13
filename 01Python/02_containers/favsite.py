import webbrowser
import json 
import sys

# ath to Google Chrome executable
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

#parse the bookmarks from local file
bookmarks_file_path = 'C:/Users/Shrouk/AppData/Local/Google/Chrome/User Data/Default/Bookmarks'

try:
    with open(bookmarks_file_path, 'r', encoding='utf-8') as bookmarks:
        bookmarks_data = json.load(bookmarks)
        for iterator in range(len(bookmarks_data['roots']['bookmark_bar']['children'])):
            print(str(iterator)+" "+bookmarks_data['roots']['bookmark_bar']['children'][iterator]['name']+" "+bookmarks_data['roots']['bookmark_bar']['children'][iterator]['url'])
except Exception as e:
    print(f"Error reading bookmarks: {e}")
    sys.exit()

#open the bookmark link
GivenSiteNo = input("Please enter the number of the site (e.g., 8):")

#Check the input
try:
    GivenSiteNo = int(GivenSiteNo)
    if not (GivenSiteNo > 0 and GivenSiteNo < len(bookmarks_data['roots']['bookmark_bar']['children'])) :
        print("ERROR: Your input is not a valid number")
        sys.exit()
except ValueError:
    print("ERROR: Your input is not a number")
    sys.exit()

webbrowser.get(chrome_path).open(bookmarks_data['roots']['bookmark_bar']['children'][GivenSiteNo]['url'])