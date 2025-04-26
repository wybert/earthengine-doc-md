 
#  ee.Date.format 
bookmark_borderbookmark Stay organized with collections  Save and categorize content based on your preferences.
  * On this page
  * [Examples](https://developers.google.com/earth-engine/apidocs/ee-date-format#examples)


Convert a date to string. 
Usage| Returns  
---|---  
`Date.format( _format_, _timeZone_)`| String  
Argument| Type| Details  
---|---|---  
this: `date`| Date|   
`format`| String, default: null| A pattern, as described at http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html; if omitted will use ISO standard date formatting.  
`timeZone`| String, default: null| The time zone (e.g., 'America/Los_Angeles'); defaults to UTC.  
## Examples
[Code Editor (JavaScript)](https://developers.google.com/earth-engine/apidocs/ee-date-format#code-editor-javascript-sample)[Colab (Python)](https://developers.google.com/earth-engine/apidocs/ee-date-format#colab-python-sample) More
```
// Various examples of ee.Date.format with Joda-Time formatting and time zones.
vardate=ee.Date('2020-08-18');// Defaults to UTC
print(date);// Date (2020-08-18 00:00:00)
// List of time zones:
// https://www.joda.org/joda-time/timezones.html
print(date.format(null,'GMT'));// 2020-08-18T00:00:00
print(date.format(null,'Etc/GMT'));// 2020-08-18T00:00:00
print(date.format(null,'Etc/GMT+0'));// 2020-08-18T00:00:00
print(date.format(null,'Zulu'));// 2020-08-18T00:00:00
print(date.format(null,'UTC'));// 2020-08-18T00:00:00
print(date.format(null,'America/Los_Angeles'));// 2020-08-17T17:00:00
print(date.format(null,'US/Pacific'));// 2020-08-17T17:00:00
print(date.format(null,'Etc/GMT+8'));// 2020-08-17T17:00:00
print(date.format(null,'PST8PDT'));// 2020-08-17T17:00:00
print(date.format(null,'Australia/Tasmania'));// 2020-08-18T10:00:00
print(date.format(null,'Etc/GMT-10'));// 2020-08-18T10:00:00
// Reference for Joda-Time format characters:
// https://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html
vardatetime=ee.Date('1975-07-23T21:13:59');// Defaults to UTC
print(datetime);// Date (1972-07-25 21:13:59)
// year of era and era
print(datetime.format('YYYY GG'));// 1975 AD
// century and year
print(datetime.format('CC YY'));// 19 75
// weekyear and week of weekyear
print(datetime.format('xxxx ww'));// 1975 30
// year and day of year
print(datetime.format('yy DDD'));// 75 204
// month of year and day of month
print(datetime.format('MM dd'));// 07 23
// day of week number and day of week text
print(datetime.format('e E'));// 3 Wed
print(datetime.format('e EEEEEEEE'));// 3 Wednesday
// half of day, hour of halfday, and clockhour of halfday
print(datetime.format('a K h'));// PM 9 9
print(datetime.format('a KK hh'));// PM 09 09
// hour of day, clockhour of day, minute, second, fraction of second
print(datetime.format('H k m s S'));// 21 21 13 59 0
print(datetime.format('HH kk mm ss SS'));// 21 21 13 59 00
// time zone
print(datetime.format('z'));// UTC
print(datetime.format('zzzz'));// Coordinated Universal Time
print(datetime.format('z','PST8PDT'));// PDT
print(datetime.format('zzzz','PST8PDT'));// Pacific Daylight Time
// time zone offset/id
print(datetime.format('Z'));// +0000
print(datetime.format('ZZ'));// +00:00
print(datetime.format('ZZZ'));// UTC
print(datetime.format('Z','PST8PDT'));// -0700
print(datetime.format('ZZ','PST8PDT'));// -07:00
print(datetime.format('ZZZ','PST8PDT'));// PST8PDT
// single quotes for text
print(datetime.format("YY 'yada' MM"));// 75 yada 07
// '' for a single quote
print(datetime.format("YY ''MM'' dd"));// 75 '07' 23
```
Python setup
See the [ Python Environment](https://developers.google.com/earth-engine/guides/python_install) page for information on the Python API and using `geemap` for interactive development.
```
importee
importgeemap.coreasgeemap
```
```
# Various examples of ee.Date.format with Joda-Time formatting and time zones.
date = ee.Date('2020-08-18') # Defaults to UTC
display(date) # Date (2020-08-18 00:00:00)
# List of time zones:
# https://www.joda.org/joda-time/timezones.html
display(date.format(None, 'GMT')) # 2020-08-18T00:00:00
display(date.format(None, 'Etc/GMT')) # 2020-08-18T00:00:00
display(date.format(None, 'Etc/GMT+0')) # 2020-08-18T00:00:00
display(date.format(None, 'Zulu')) # 2020-08-18T00:00:00
display(date.format(None, 'UTC')) # 2020-08-18T00:00:00
display(date.format(None, 'America/Los_Angeles')) # 2020-08-17T17:00:00
display(date.format(None, 'US/Pacific')) # 2020-08-17T17:00:00
display(date.format(None, 'Etc/GMT+8')) # 2020-08-17T17:00:00
display(date.format(None, 'PST8PDT')) # 2020-08-17T17:00:00
display(date.format(None, 'Australia/Tasmania')) # 2020-08-18T10:00:00
display(date.format(None, 'Etc/GMT-10')) # 2020-08-18T10:00:00
# Reference for Joda-Time format characters:
# http://joda-time.sourceforge.net/apidocs/org/joda/time/format/DateTimeFormat.html
datetime = ee.Date('1975-07-23T21:13:59') # Defaults to UTC
display(datetime) # Date (1972-07-25 21:13:59)
# year of era and era
display(datetime.format('YYYY GG')) # 1975 AD
# century and year
display(datetime.format('CC YY')) # 19 75
# weekyear and week of weekyear
display(datetime.format('xxxx ww')) # 1975 30
# year and day of year
display(datetime.format('yy DDD')) # 75 204
# month of year and day of month
display(datetime.format('MM dd')) # 07 23
# day of week number and day of week text
display(datetime.format('e E')) # 3 Wed
display(datetime.format('e EEEEEEEE')) # 3 Wednesday
# half of day, hour of halfday, and clockhour of halfday
display(datetime.format('a K h')) # PM 9 9
display(datetime.format('a KK hh')) # PM 09 09
# hour of day, clockhour of day, minute, second, fraction of second
display(datetime.format('H k m s S')) # 21 21 13 59 0
display(datetime.format('HH kk mm ss SS')) # 21 21 13 59 00
# time zone
display(datetime.format('z')) # UTC
display(datetime.format('zzzz')) # Coordinated Universal Time
display(datetime.format('z', 'PST8PDT')) # PDT
display(datetime.format('zzzz', 'PST8PDT')) # Pacific Daylight Time
# time zone offset/id
display(datetime.format('Z')) # +0000
display(datetime.format('ZZ')) # +00:00
display(datetime.format('ZZZ')) # UTC
display(datetime.format('Z', 'PST8PDT')) # -0700
display(datetime.format('ZZ', 'PST8PDT')) # -07:00
display(datetime.format('ZZZ', 'PST8PDT')) # PST8PDT
# single quotes for text
display(datetime.format("YY 'yada' MM")) # 75 yada 07
# '' for a single quote
display(datetime.format("YY ''MM'' dd")) # 75 '07' 23
```

Was this helpful?
