from playwright.sync_api import sync_playwright
from playwright.sync_api import Page


class Parser:
    def __init__(self, page_url: str) -> None:
        self.page_url = page_url

    def start(self) -> None:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)

            page = browser.new_page()
            page.goto(self.page_url)

            h2 = page.query_selector_all("h2")[1:-1]
            blockquote = page.query_selector_all("blockquote")[2:]

            print("Number of titles:", len(h2))
            print("Number of prompts:", len(blockquote))

            for i in range(len(h2)):
                title = h2[i].inner_text()
                prompt = blockquote[i].inner_text()

                title = title.replace("✂️", "")

                with open("./data/prompts.csv", "a", encoding="UTF-8") as f:
                    if i == 0:
                        f.write('User,Prompt\n')
                    f.write(f'"{title}","{prompt}"\n')

            browser.close()


if __name__ == "__main__":
    parser = Parser("https://prompts.chat/")
    parser.start()
