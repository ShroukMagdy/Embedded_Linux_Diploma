from win10toast import ToastNotifier
import psutil

# Get battery percentage
battery = psutil.sensors_battery()
percent = battery.percent

# Print the battery percentage to the console
print(percent)

# Initialize the notifier
toaster = ToastNotifier()

# Show the notification
toaster.show_toast(
    "Battery Percentage",
    f"{percent}% Percent Remaining",
    duration=10
)
