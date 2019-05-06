from datetime import datetime, timedelta, timezone

def demo_datetime():
    now = datetime.now()
    print(now)
    dt = datetime(2015, 3, 10, 12, 10)
    print(dt)
    print(dt.timestamp())
    print(datetime.fromtimestamp(dt.timestamp()))
    print(datetime.utcfromtimestamp(dt.timestamp()))
    day_str = datetime.strptime('2010-1-1 18:45:20', '%Y-%m-%d %H:%M:%S')
    print(day_str)
    print(now.strftime('%Y-%m-%d %H:%M:%S'))

def demo_timedelta():
    now = datetime.now()
    t1 = now + timedelta(days=1, hours=20)
    print(t1)

def demo_timezone():
    tz_utc_8 = timezone(timedelta(hours=8))
    now = datetime.now()
    dt = now.replace(tzinfo=tz_utc_8)
    print(dt)


if __name__ == '__main__':
    demo_datetime()
    demo_timedelta()
    demo_timezone()