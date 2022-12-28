
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
from time import sleep
import sys

g_should_run = True

def check_logs(log_file="log.txt",keywords=["error"]):
    global g_should_run
    print(f"Checking logs now at {datetime.datetime.now()}")
    file = open(log_file, "r")
    for keyword in keywords:
        if keyword in file.read():
            g_should_run = False
            raise Exception(f"Keyword Found !!!!!!!!!!!!")

    print("No Error.............")
    file.close()


def main():
    plugin_scheduler = BackgroundScheduler()
    plugin_scheduler.add_job(func=check_logs,trigger='interval',seconds = 3)
    plugin_scheduler.start()
    # Runs an infinite loop
    while g_should_run:
        sleep(1)
    if not g_should_run:
        sys.exit()

if __name__ == "__main__":
    main()
