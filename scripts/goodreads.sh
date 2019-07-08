#!/bin/bash
base=$(dirname $0)
# Download export from Goodreads
original_export=$base/../timeline_data/goodreads_library_export.csv
# Only view read files
read_export=$base/../timeline_data/goodreads_read_export.csv
# Temp file
old_read_export=$base/../timeline_data/_old_goodreads_read_export.csv
json_file=$base/../timeline_data/goodreads_input.json

# 1: Backup Read export
cp $read_export $old_read_export

# 2: Parse read books from export
head -n 1 < $original_export > $read_export
grep ,read, $original_export >> $read_export

# 3: Add read dates
python $base/../third_party/Enhance-GoodReads-Export/enhance_goodreads_export.py \
	--csv $read_export \
  --update $old_read_export \
	--email mchristen96@gmail.com \
	--password $(cat $base/goodreads_password)

# 4: Add image_url
python $base/goodreads_helper/update_image_url.py \
	--csv $read_export \
	--update $old_read_export \
  --client-key $(cat $base/goodreads_client_key) \
	--client-secret $(cat $base/goodreads_client_secret)

# 5: Remove backup
rm $old_read_export

# 6: Generate json
python $base/goodreads_helper/main.py < $read_export > $json_file
