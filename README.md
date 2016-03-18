Use alongside an existing install of the agent (to have a conf file + no trouble with deps):

```
/opt/datadog-agent/embedded/bin/pip install -r requirements.txt
/opt/datadog-agent/embedded/bin/python dogstatsd --broker="test.mosquitto.org" --topic="testing-dogstatsd"
```
