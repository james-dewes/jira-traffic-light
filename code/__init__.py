'''
Main file
'''
import time, trafficLight, jira


def main():
    # set up the light
    signal = trafficLight.TrafficLight()
    # run starting test sequence
    for i in range(1,4):
        signal.change('red')
        time.sleep(i)
        signal.change('yellow')
        time.sleep(i)
        signal.change('green')
        time.sleep(i)

    signal.red.on()
    signal.yellow.on()
    signal.green.on()
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

        time.sleep(5)


if __name__ == '__main__':
    main()
