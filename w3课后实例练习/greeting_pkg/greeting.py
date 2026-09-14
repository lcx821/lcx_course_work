"""示例库：打招呼。用于演示 wheel 打包。"""


def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Greet someone")
    parser.add_argument("name", help="要打招呼的对象")
    args = parser.parse_args()
    print(greet(args.name))


if __name__ == "__main__":
    main()
