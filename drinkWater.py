#Python program which will give you desktop notification to remind you to drink water.add()

import time
from plyer import notification

hour = 2
while True:
    time.sleep(3600 * hour)
    notification.notify(title="Water Break",
                        message="You should drink water now",
                        timeout=2)