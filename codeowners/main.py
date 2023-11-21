#!/usr/bin/env python3

import pandas
import tabulate

import extract


def main():
    df = pandas.DataFrame(extract.extract()).sort_values(
        by=["path"], ignore_index=True
    )

    print(tabulate.tabulate(df, headers="keys", tablefmt="psql"))


if __name__ == "__main__":
    main()
