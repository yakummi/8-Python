from dateutil.parser import parse

logline = 'INFO 2022-01-01T00:00:01 Happy new year, human.'
timestamp = parse(logline, fuzzy=True)
print(timestamp)