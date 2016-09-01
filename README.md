<html>
<body>
  <h1>Jira Traffic Light</h1>
  <p>Make a simple traffic light system to monitor Jira helpdesk project queues.</p>

  <h2>Notes</h2>
  <p>This is written for Python 2 and uses the urllib, urlib2 and RPi.</p>
  <p>
  You will need to create your own text file for conex.txt containing the link to your Jira implementation, your JQL which produces a list of
  all the tickets that you want to watch and the basic authorisation token which you need to access Jira. Details on generating this token can be found at 
  <a href="http://stackoverflow.com/questions/15006705/how-to-use-basic-authentication-with-jira-rest-api-in-javascript">http://stackoverflow.com/questions/15006705/how-to-use-basic-authentication-with-jira-rest-api-in-javascript</a></p>
  <p>You will also need to create your own sound file for the sound notifications and add this in mp3 format to the sound folder.</p>
  <h2>Error response codes</h2>
  <p>To help spot issues with the traffic light error responses have been added</p>
  <p><b>Red Flashing</b>: HTTP error.
  <p><b>Yellow Flashing</b>: JSON Parse error.
</body>
</html>
