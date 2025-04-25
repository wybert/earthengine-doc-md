 
#  Save-First Joins 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
To save only the first match for each element in a collection, use an `ee.Join.saveFirst()`. The `saveFirst()` join functions in an equivalent way to the `saveAll()` join, except for each element in the `primary` collection, it simply saves the first element from the `secondary` collection matching the condition specified in the `ee.Filter`. Unmatched elements in the `primary` collection are dropped. Unless a sorting property and an order are supplied (as in the [saveAll example](https://developers.google.com/earth-engine/guides/joins_save_all)), the first element saved might be any of the elements in the list found by `saveAll()` with the same filter.
