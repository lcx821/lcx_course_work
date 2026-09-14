import argparse

def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--name", required=True)
    a = p.parse_args(argv)
    if not a.name.strip():
        p.error("--name must not be blank")
    print(f"Hello, {a.name}!")
