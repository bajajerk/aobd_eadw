rm -rf index/
mongo eadw_proj --eval "db.dropDatabase()"
mongoimport --db eadw_proj --collection news --file collection.json

