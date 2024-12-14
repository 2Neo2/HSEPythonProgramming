from datetime import datetime
import re

# Task.
dates = [
    "Daily News - Thursday, 18 August 1977",
    "The Guardian - Friday, 11.10.13",
    "The Moscow Times - Wednesday, October 2, 2002"
]

for date in dates:
    cleaned_date = date.split("-")[-1].strip()
    try:
        result = datetime.strptime(cleaned_date, "%A, %B %d, %Y")
        print("The Moscow Times:", result)
    except ValueError:
        try:
            result = datetime.strptime(cleaned_date, "%A, %d %B %Y")
            print("Daily News:", result)
        except ValueError:
            try:
                result = datetime.strptime(cleaned_date, "%A, %d.%m.%y")
                print("The Guardian:", result)
            except ValueError:
                print(f"Не удалось распознать формат даты: {date}")