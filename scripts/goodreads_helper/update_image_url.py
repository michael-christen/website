import argparse
import csv

from goodreads import client as goodreads_client


STANDARD_FIELDNAMES = ["Book Id", "Title", "Author", "Author l-f", "Additional Authors", "ISBN", "ISBN13", "My Rating",
                       "Average Rating", "Publisher", "Binding", "Number of Pages", "Year Published",
                       "Original Publication Year", "Date Read", "Date Added", "Bookshelves",
                       "Bookshelves with positions", "Exclusive Shelf", "My Review", "Spoiler", "Private Notes",
                       "Read Count", "Recommended For", "Recommended By", "Owned Copies", "Original Purchase Date",
                       "Original Purchase Location", "Condition", "Condition Description", "BCID",
                       "read_dates", "genres"]


def parse_csv(filename):
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        return list(reader)


def get_client(client_key, client_secret):
    return goodreads_client.GoodreadsClient(
        client_key=client_key,
        client_secret=client_secret,
    )


def get_image_url(gr_client, book_id):
    book = gr_client.book(book_id)
    return book.image_url


def main(options):
    csv_file = options['csv']
    update = options['update']
    update_rows = parse_csv(update)
    id_to_image_url = {}
    for row in update_rows:
        image_url = row.get('image_url')
        if image_url:
            id_to_image_url[row['Book Id']] = image_url
    input_rows = parse_csv(csv_file)
    # Get image_url
    client = get_client(
        client_key=options['client_key'], client_secret=options['client_secret'])
    for i, row in enumerate(input_rows):
        book_id = row['Book Id']
        image_url = id_to_image_url.get(book_id)
        if not image_url:
            print(i, row['Title'])
            image_url = get_image_url(client, book_id)
        row['image_url'] = image_url
    # Update
    with open(csv_file, 'w') as f:
        writer = csv.DictWriter(
            f, fieldnames=STANDARD_FIELDNAMES + ["image_url"],
            delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        writer.writerows(input_rows)


if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser(
        description="Adds image_url to a GoodReads export file")
    argument_parser.add_argument("-c", "--csv", help="path of your GoodReads export file (the new columns will be "
                                                     "added to this file)")
    argument_parser.add_argument("-u", "--update", help="(optional) path of previously enhanced GoodReads export file "
                                                        "to update (output will still be written to the file "
                                                        "specified in --csv)")
    argument_parser.add_argument("--client-key", help="Goodreads client key")
    argument_parser.add_argument("--client-secret",
                                 help="Goodreads client secret")
    options = vars(argument_parser.parse_args())
    main(options)
