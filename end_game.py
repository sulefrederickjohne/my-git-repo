#!/usr/bin/env python3

import sys

def battle_status(file1, hero):
    print("Selected hero: {0}".format(hero))
    with open(file1, 'r') as file1:
        if hero in file1.read():
            print("Thanos Wins! Sad...")
        else:
            print("Thanos Wins! Sad...")

def main():
    battle_status(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
