from traffic_bot_no_clicks import Scrape
import threading
from datetime import date, datetime


now = datetime.now()
t1 = now
urls = [
    'https://www.amazon.com//Breton-Dare-Cracker-Variety-Pack/dp/B08V3XBS8Z',
]
glance_view_count = 0
total_views= 0
failed_views = 0

'''
Baseline Weekly Stats:
Glance views = 196  
Fast Track Glance View = 3.57%
Conversion Rate = 17.35%
hello
'''


def run():
    global glance_view_count
    global total_views
    global failed_views
  
    while True:     
        for i in urls:
            s = Scrape(i)
            try:
                success_rate = int((glance_view_count/total_views)*100)
            except:
                pass    
            if s.gv == False:
                failed_views += 1
            elif s.gv == True:
                glance_view_count += 1
            else:
                print("Error")
    
            total_views +=1
            t2 = datetime.now()
            
            elapsed = t2 - t1
            print("Glance View Report:")
            print(f"Time Elapsed:{elapsed}")
            print(f"Glance Views:{glance_view_count}")
            print(f"Total Views:{total_views}")
            print(f"Failed Views:{failed_views}")
            try:
                print(f'Success Rate:{success_rate}%')
            except:
                pass

for _ in range(10):
    t = threading.Thread(target=run)
    t.start()
