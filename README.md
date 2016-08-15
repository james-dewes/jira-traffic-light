<html>
<body>
  <h1>Jira Traffic Light</h1>
  <p>Make a simple traffic light system to monitor Jira helpdesk project queues.</p>

  <h2>Notes</h2>
  <p>This is written for Python 2 and uses the urllib, urlib2 and RPi.</p>
  <p>
  You will need to create your own text file for conex.txt containing the link to your Jira implimentation, your JQL which produces a list of
  all the tickets that you want to watch and the authorisation token which you need to acess Jira. Deatils on generating this token can be found at 
  <a href="https://developer.atlassian.com/hipchat/guide/hipchat-rest-api/api-access-tokens">https://developer.atlassian.com/hipchat/guide/hipchat-rest-api/api-access-tokens</a></p>
  <p>You will also need to create your own sound file for the sound notifications and add this in mp3 format to the sound folder.</p>
</body>
</html>
