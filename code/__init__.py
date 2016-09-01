'''
Main file
'''
import time, trafficLight, jira, sound


def main():
    # set up the pin numbers should be the out pins on your Pi
    signal = trafficLight.TrafficLight([18, 15, 17])
    #set up the sound
    noise = sound.sound()
    # run starting test sequence
    for i in range(1,4):
        signal.change('red')
        time.sleep(0.5)
        signal.change('yellow')
        time.sleep(0.5)
        signal.change('green')
        time.sleep(0.5)
        

    signal.red.on()
    signal.yellow.on()
    signal.green.on()
    time.sleep(1)
    signal.red.off()
    signal.yellow.off()
    signal.green.off()
    noise.play()


    # import connection string and jql
    conex_file = open('conx.txt')
    url = conex_file.readline()
    auth_string = conex_file.readline()
    jql = conex_file.readline()
    jira_handle = jira.Jira(url, jql, auth_string)
    old_total = 0
    try:
        while True:
            jira_handle.request()
            if jira_handle.total_tickets() >= 0 and jira_handle.total_tickets() < old_total:
                noise.play()
                old_total = jira_handle.total_tickets()
            elif jira_handle.total_tickets() > 0:
                old_total = jira_handle.total_tickets()
            
            if jira_handle.total_tickets() == -1:
                # Connection error
                signal.change('red')
                for i in range(0,10):
                    signal.red.on()
                    time.sleep(0.5)
                    signal.red.off()
            
            elif jira_handle.total_tickets() == -2:
                # parse error
                signal.change('yellow')
                for i in range(0,10):
                    signal.yellow.on()
                    time.sleep(0.5)
                    signal.yellow.off()    
                    
            elif jira_handle.total_tickets() < 35 and jira_handle.critical_tickets() == False:
                signal.change('green')
                
            elif jira_handle.total_tickets() >= 35 and jira_handle.total_tickets() < 50 and jira_handle.critical_tickets() == False:
                signal.change('yellow')
                
            else:
                signal.change('red')

            ##so we don't hammer the API
            time.sleep(5)

    except KeyboardInterrupt:
        signal.cleanup()
        pass

if __name__ == '__main__':
    main()
