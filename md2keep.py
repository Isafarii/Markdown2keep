"""
Markdown-to-Google-Keep Script
...
1. Place your Markdown files in the same directory as this script.
2. Run the script using Python 3.x.
3. Follow the on-screen instructions to place the cursor in Google Keep.
4. The script will create notes for each Markdown file in Google Keep.

Adjust the sleep duration in the script (`time.sleep(seconds)`) based on your needs.

"""
import keyboard
import glob
import time
import re
import markdown2

def convert_md_to_html(md_text):
    return markdown2.markdown(md_text)

def main():
    transfer = set()

    for i, doc in enumerate(glob.iglob("*.md")):
        # Extract the title from the file name using regex
        match = re.match(r'(.+?)\.md', doc)
        title = match.group(1) if match else f"Untitled_{i}"

        with open(doc, 'r', encoding='utf-8') as md_file:
            md_text = md_file.read()

        html_text = convert_md_to_html(md_text)
        transfer.add((title, html_text.strip()))

    print('\nPlace your cursor in Google Keep (click "Take a note...") and press backspace.')
    keyboard.wait("backspace")

    for title, html_text in transfer:
        keyboard.write(f"{title}\n{html_text}")
        keyboard.press_and_release("ctrl+enter")
        
        # Introduce a delay before creating the next note
        time.sleep(5)  # Adjust the delay based on your needs

    print("Notes creation completed.")

if __name__ == "__main__":
    main()
