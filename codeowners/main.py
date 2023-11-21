#!/usr/bin/env python3

import pandas
import extract


def main():
    print(
        pandas.DataFrame(extract.extract())
        .style.set_properties(**{"text-align": "left"})
        .to_string()
    )


if __name__ == "__main__":
    main()
