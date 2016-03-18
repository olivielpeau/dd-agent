Install:

```
bash -c "$(curl -L https://raw.githubusercontent.com/olivielpeau/dd-agent/olivielpeau/mqtt/packaging/datadog-agent/source/setup_agent.sh)"
```

Use:

```
cd ~/.datadog-agent/dogstatsd/agent
../venv/bin/python dogstatsd --broker="test.mosquitto.org" --topic="testing-dogstatsd"
```
