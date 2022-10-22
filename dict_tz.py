import pytz

dict_tz = {key: val for key, val in pytz.country_timezones.items()}

print(dict_tz)