from datetime import datetime
import pytz
import os

dict_tz = {key: val for key, val in pytz.country_timezones.items()}



def search_tz():

    country_code = input('Please, insert the country code(s) for research the Time Zone: ').upper()

    # assert(type(country_code) == int), 'You can only enter values from the list of tz '

    for key in dict_tz:
            if key == country_code:
                return "".join(dict_tz[key])

            
def country_time_zone(result):
    
    country = pytz.timezone(result)
    country_tz = datetime.now(country)
    print(f'\nThe date in {result} is {country_tz.strftime("%d/%m/%Y")} in format day/month/year \nand hour local is: {country_tz.strftime("%H: %M")}\n ')


def main():
    os.system('clear')
    country_time_zone(search_tz())
    
if __name__ == '__main__':
    main()
    


