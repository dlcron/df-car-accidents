#!/bin/sh

docker run \
  -e OVERPASS_META=yes \
  -e OVERPASS_MODE=init \
  -e OVERPASS_PLANET_URL=https://download.geofabrik.de/europe/poland/slaskie-latest.osm.bz2 \
  -e OVERPASS_DIFF_URL=http://download.openstreetmap.fr/replication/europe/poland/slaskie/minute/ \
  -e OVERPASS_RULES_LOAD=10 \
  -v /Users/dlc/projects/dw/overpass_db/:/db \
  -p 12345:80 \
  -i -t \
  wiktorn/overpass-api
