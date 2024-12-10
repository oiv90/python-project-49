#!/usr/bin/env python
from ..cli import welcome_user


def main():
    print('Welcome to the Brain Games!')
    username = welcome_user()


if __name__ == '__main__':
    main()