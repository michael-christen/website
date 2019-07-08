# Sources

## Goodreads

`goodreads_library_export.csv` generated via
[import page](https://www.goodreads.com/review/import).

Goodreads has its own stats page: https://www.goodreads.com/review/stats/.

It's missing some critical information, so we then need to:

1. Filter down to books where "Exclusive Shelf" is "Read"
2. Then run

```
python third_party/Enhance-GoodReads-Export/enhance_goodreads_export.py --csv ~/projects/blog2/timeline_data/goodreads_library_export.csv --email mchristen96@gmail.com --password $password
```

This comes from the [bookstats website](https://almoturg.com/bookstats/).

API may make this
automatable, but doesn't look too convenient for now:
[Reviews.list](https://www.goodreads.com/api/index#reviews.list).
