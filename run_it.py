from traffic_bot import Scrape
import threading
from datetime import date, datetime


now = datetime.now()
t1 = now
urls = [
    'https://www.amazon.ca/dp/B08YGK9KWC',
    'https://www.amazon.ca/dp/B08YGH6LHY',
    'https://www.amazon.ca/dp/B08YGFM4SQ',
]
glance_view_count = 0
total_views= 0
failed_views = 0
successful_clicks = 0
failed_clicks = 0
click_count = 0
'''
Baseline Weekly Stats:
Glance views = 196  
Fast Track Glance View = 3.57%
Conversion Rate = 17.35%
'''


def run():
    global glance_view_count
    global total_views
    global failed_views
    global successful_clicks
    global failed_clicks
    global click_count

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
            try:
                click_success_rate = int((successful_clicks/click_count)*100)
            
            except:
                pass

            if s.click_result==True:
                successful_clicks +=1
            
            elif s.click_result ==False:
                failed_clicks +=1
            
            click_count +=1
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

            print('\n')
            print("Click Report:")
            print(f"Successful Clicks: {successful_clicks}")
            print(f"Failed Clicks: {failed_clicks}")
            try:
                print(f"Click Success Rate:{click_success_rate}%")
            except:
                pass    

            print('\n')
            print('\n')


for _ in range(10):
    t = threading.Thread(target=run)
    t.start()
