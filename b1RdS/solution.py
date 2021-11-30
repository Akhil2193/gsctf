#!/usr/bin/env python3
import sys
import time
import random
import hashlib


def seed():
    return round(time.time())


def hash(text):
    return hashlib.sha256(str(text).encode()).hexdigest()


def main():
    s = seed()
    while s>0:
        random.seed(s, version=2)

        x = random.random()
        flag = hash(x)
        if '9f098311' in flag:
            with open("./ans", "w") as f:
                f.write(f"GSCTF{{{flag}}}")
            f.close()
            break
        print(f"Incorrect: {x}")
        s-=1
    print("Good job <3")


if __name__ == "__main__":
    sys.exit(main())
