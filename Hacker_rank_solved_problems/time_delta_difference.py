# When users post an update on social media, such as a URL, image, status update, etc.,
# other users in their network are able to view this post in their news feed.
# Users can also see exactly when the post was published — i.e., how many hours,
# minutes, or seconds ago.
#
# Since posts may be published and viewed in different time zones, the displayed
# time can be confusing. You are given two timestamps in the format:
# Day dd Mon yyyy hh:mm:ss +xxxx

from datetime import datetime

def time_delta(t1 :str,t2:str)-> str:
    fmt = "%a %d %b %Y %H:%M:%S %z"

    dt1 = datetime.strptime(t1, fmt)
    dt2 = datetime.strptime(t2, fmt)

    return str(int(abs((dt1 - dt2).total_seconds())))
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        t1 = input().strip()
        t2 = input().strip()
        print(time_delta(t1, t2))