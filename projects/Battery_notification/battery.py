# pip install psutil
import psutil
from pynotifier import Notification

battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = battery.percent

if percent <= 100 and plugged!=True:
 
    # pip install py-notifier
    # pip install win10toast

   notification = Notification(
        title="Batería Baja", 
        description=f"{percent}% de batería restante!",
        duration=5
    ).send()  # En lugar de .send()
