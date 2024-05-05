
from modules.downloader import Downloader
from modules.parser import Parser

proxy = ''
your_email = 'nerengtseel@hotmail.com'
your_password = 'Toan@1234'

def parsing(keywords):

    parser = Parser(your_email, your_password, proxy=None, headless=False)

    for key in keywords:
        # parser.login()

        parser.parse_by_keyword(key)



def downloading(keywords):
    for key in keywords:
        downloader = Downloader(key, proxy=None, headless=False)
        links = downloader.read_links_file()


        for index, link in enumerate(links, 1):
            print(f"Processing Link {index}/{len(links)}")
            downloader.download(link)



if __name__ == '__main__':
    keys = [
        'keto',
    ]
    choice = input("Enter '1' to run the parser, '2' run the downloader: " )

    if choice == '1':
        parsing(keys)
    elif choice == '2':
        downloading(keys)
    else:
        print("Invalid choice. Please enter '1' or '2'.")

