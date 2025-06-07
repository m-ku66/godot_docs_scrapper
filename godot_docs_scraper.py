import os
import shutil
import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

# ========== CONFIG ==========
BASE_URL = "https://docs.godotengine.org/en/stable/classes/class_{}.html"
CLASSES_TO_FETCH = [
    "Node",
    "Area3D",
    "Camera3D",
    "CharacterBody3D"
]
OUTPUT_DIR = "godot_docs_md"
CHUNK_SIZE = 4000  # characters per markdown chunk
# ==============================


def fetch_html(url: str) -> str:
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"❌ HTTP Error for {url}: {response.status_code}")
            return None
        return response.text
    except Exception as e:
        print(f"❌ Request failed for {url}: {e}")
        return None


def extract_class_doc(html: str, class_name: str) -> str:
    soup = BeautifulSoup(html, "html.parser")

    if soup.find(string=lambda text: text and "Page not found" in text):
        print(f"⚠️  '{class_name}' appears to be a missing page (in-page 404). Skipping.")
        return None

    main_content = soup.find("div", {"role": "main"})
    if not main_content:
        print(f"⚠️  Could not find main content for {class_name}. Dumping full page.")
        return md(str(soup.body)) if soup.body else None

    return md(str(main_content))


def split_markdown(markdown: str, chunk_size: int) -> list:
    chunks = []
    while len(markdown) > chunk_size:
        split_at = markdown.rfind("\n", 0, chunk_size)
        if split_at == -1:
            split_at = chunk_size
        chunks.append(markdown[:split_at].strip())
        markdown = markdown[split_at:].strip()
    if markdown:
        chunks.append(markdown)
    return chunks


def save_markdown_chunks(class_name: str, chunks: list):
    folder_path = os.path.join(OUTPUT_DIR, class_name)
    os.makedirs(folder_path, exist_ok=True)
    for i, chunk in enumerate(chunks):
        filename = os.path.join(folder_path, f"{class_name}_part_{i + 1}.md")
        with open(filename, "w", encoding="utf-8") as f:
            f.write(chunk)
    print(f"✅ Saved {len(chunks)} chunks to: {folder_path}")


def clear_output_dir():
    if os.path.exists(OUTPUT_DIR):
        shutil.rmtree(OUTPUT_DIR)
    os.makedirs(OUTPUT_DIR)


def main():
    print("\n=== Godot Docs Scraper (Descriptive Filenames) ===\n")
    clear_output_dir()

    for class_name in CLASSES_TO_FETCH:
        url = BASE_URL.format(class_name.lower())
        alt_url = BASE_URL.format(class_name)

        print(f"Fetching: {url}")
        html = fetch_html(url)
        if not html or "Page not found" in html:
            print(f"Trying fallback URL: {alt_url}")
            html = fetch_html(alt_url)

        if not html:
            print(f"❌ Skipping {class_name} due to fetch failure.")
            continue

        markdown = extract_class_doc(html, class_name)
        if not markdown:
            print(f"❌ Could not extract content for {class_name}")
            continue

        chunks = split_markdown(markdown, CHUNK_SIZE)
        save_markdown_chunks(class_name, chunks)

    print(f"\n🎉 Done. Markdown files saved to: {OUTPUT_DIR}\n")


if __name__ == "__main__":
    main()
