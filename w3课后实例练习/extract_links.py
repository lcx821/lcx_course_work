"""提取 Markdown 文本中的链接（agentic-coding 一讲课堂示例：argparse + 类型注解）。"""
import argparse
import re
from pathlib import Path

LINK_PATTERN = re.compile(r"\[.*?\]\((.*?)\)")


def extract(content: str) -> list[str]:
    return LINK_PATTERN.findall(content)


def main() -> None:
    parser = argparse.ArgumentParser(description="从 Markdown 文件提取链接")
    parser.add_argument("path", type=Path, help="Markdown 文件路径")
    parser.add_argument("--absolute", action="store_true", help="只保留绝对 URL")
    args = parser.parse_args()

    content: str = args.path.read_text(encoding="utf-8")
    links = extract(content)
    if args.absolute:
        links = [url for url in links if url.startswith("http")]
    for link in links:
        print(link)


if __name__ == "__main__":
    main()
