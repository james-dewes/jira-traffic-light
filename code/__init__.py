'''
Main file
'''
import trafficLight
import jira
import time


def main():
    # set up the light
    signal = trafficLight()
    # TODO import connection string
    connection_string = ''
    jira_handle = jira()
    jira_handle.connect(connection_string)
    while True:
        if jira_handle.TotalTickets() < 35 & jira_handle.CriticalTickets == 0:
            signal.change('green')
        elif jira_handle.TotalTickets() >= 35 & jira_handle.TotalTickets() < 50 & jira_handle.CriticalTickets == 0:
            signal.change('yellow')
        else:
            signal.change('red')

        time.sleep(2)


if __name__ == '__main__':
    main()
