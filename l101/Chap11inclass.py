#from test import testEqual



def average_sales(daily_sales):

    num_weeks = len(daily_sales)
    weekly_averages = [0 for i in range(num_weeks)]

    for week in range(0, num_weeks):

        # calculate the average for the given week
        week_sum = 0
        for day_total in daily_sales[week]:
            week_sum += day_total

        weekly_averages[week] = week_sum / len(daily_sales[week])

    return weekly_averages


sales = [[1512.30, 1555.72, 1989.77, 2101.33, 1884.45, 1333.33, 1456.23],
[1215.340, 1565.99, 2989.34, 2301.77, 1234.81, 1923.44, 2282.39]]
print(average_sales(sales))



#testEqual(average_sales(sales), [1, 1])
