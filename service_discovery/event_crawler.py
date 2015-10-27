# stdlib
import logging
import time

# project
from utils.dockerutil import get_client


CONFIG_RELOAD_STATUS = ['start', 'die']


log = logging.getLogger('collector')


def crawl_docker_events(from_ts):
    """Crawl events from the docker API and return `True` if the agent configuration
       needs to be reloaded."""
    log.info('Crawling docker events looking for newly started/killed containers.')
    client = get_client()
    should_reload_conf = False
    now = int(time.time())
    events = client.events(since=from_ts, until=now, decode=True)
    for ev in events:
        if ev.get('status') in CONFIG_RELOAD_STATUS:
            should_reload_conf = True
            break
    return should_reload_conf
