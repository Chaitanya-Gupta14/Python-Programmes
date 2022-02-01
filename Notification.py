import time 
from plyer import notification
if __name__ == "__main__":
    while True:
        notification.notify(
            title="**Please learn Python!!", 
            message = "We need to grow worth each other to live together!!", 
            app_icon = "E:\softwares\Python mini Projects\python.ico", 
            timeout = 10
        )
        time.sleep(60)