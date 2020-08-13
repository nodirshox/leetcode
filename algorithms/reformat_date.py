class Solution:
    def reformatDate(self, date: str) -> str:
        result = []

        converted_date = date.split()
        # Adding Year
        result.append(converted_date[2])
        # Adding month
        month = converted_date[1]
        month_number = None
        if month == "Jan":
            month_number = '01'
        elif month == "Feb":
            month_number = '02'
        elif month == "Mar":
            month_number = '03'
        elif month == "Apr":
            month_number = '04'
        elif month == "May":
            month_number = '05'
        elif month == 'Jun':
            month_number = '06'
        if month == "Jul":
            month_number = '07'
        elif month == "Aug":
            month_number = '08'
        elif month == "Sep":
            month_number = '09'
        elif month == "Oct":
            month_number = '10'
        elif month == "Nov":
            month_number = '11'
        elif month == 'Dec':
            month_number = '12'

        result.append(month_number)

        # Add day
        day = converted_date[0]
        day_digit = None
        if len(day) == 3:
            day_digit = '0' + str(day[0:1])
        elif len(day) == 4:
            day_digit = day[0:2]

        result.append(day_digit)

        result_date = '-'.join(result)

        return result_date