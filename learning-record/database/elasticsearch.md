#### Elasticsearch 6 to 7 
If track_total_hits is set to false (because you don't care about the exact number of matching docs), then there's no need to count the docs at all, hence no need to visit all documents.
So you need to set `track_total_hits = true` when you need to get the real total count of the index.


###  Elasticsearch -> Hbase
Elasticsearch as a index table store indexs and to generate rowkeys, then use rowkeys to search Hbase.
 