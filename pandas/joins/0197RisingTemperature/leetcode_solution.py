import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by='recordDate', inplace=True)
    return weather[
            (weather['temperature'].diff() > 0) &
            (weather['recordDate'].diff().dt.days == 1)
        ][['id']]

if __name__ == '__main__':
    data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
    weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype({'id':'Int64', 'recordDate':'datetime64[ns]', 'temperature':'Int64'})

    result = rising_temperature(weather)
    print(result)