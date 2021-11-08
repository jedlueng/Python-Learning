import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as delta

df = pd.read_csv('rooms.csv')


def capacity_finder(df, qty):
  return df.loc[df.capacity >= qty]



# print(capacity_finder(df, 5))


# START
start = '2021-10-11 11:00'

end = '2021-10-11 11:30'


start_time = dt.strptime(start, '%Y-%m-%d %H:%M')
print(start_time)

print(start_time + delta(hours=1))

