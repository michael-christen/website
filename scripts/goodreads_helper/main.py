import csv
import json
import sys


EXPECTED_FIELDNAMES = [
    "Book Id",
    "Title",
    "Number of Pages",
    "image_url",
]


def _lower_and_fill_space(s):
    return s.replace(' ', '_').lower()


def parse(f):
    reader = csv.DictReader(f)
    if set(reader.fieldnames) < set(EXPECTED_FIELDNAMES):
        raise ValueError("Expected fields not present")
    return list(reader)


def main():
    rows = parse(sys.stdin)
    output_rows = []
    for row in rows:
        raw_dates_read = row['read_dates']
        split_dates_read = raw_dates_read.split(';')
        for read_dates in split_dates_read:
            try:
                read_start, read_end = read_dates.split(',')
            except ValueError:
                # Didn't get 2 values
                continue
            out_row = {_lower_and_fill_space(field): row[field]
                       for field in EXPECTED_FIELDNAMES}
            out_row['date_started'] = read_start
            out_row['date_finished'] = read_end
            output_rows.append(out_row)
    json.dump(output_rows, sys.stdout, indent=4, sort_keys=True)


if __name__ == '__main__':
    main()
