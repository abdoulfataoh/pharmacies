# HOW TO
### Create a 2d Index for mongodb collection:
```
db.<collection>.createIndex( { <location field> : "2d" ,
                               <additional field> : <value> } ,
                             { <index-specification options> } )
```
