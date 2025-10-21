from datetime import timedelta
import logging

DOMAIN = "motogp_tracker"
_LOGGER = logging.getLogger(__name__)

_BASE_URL = "https://api.motogp.pulselive.com/motogp/v1"

UPDATE_INTERVAL_CONFIG = timedelta(hours=6)
UPDATE_INTERVAL_LONG = timedelta(hours=3)
UPDATE_INTERVAL_LIVE = timedelta(seconds=30) 

CONFIG_SENSOR_ID = "sensor.motogp_configuration"
NEXT_EVENT_ENTITY = "sensor.motogp_next_event"
NEXT_SESSIONS_ENTITY = "sensor.motogp_next_sessions"

ATTRIB_COUNT = "count"
ATTRIB_STANDINGS = "standings"
ATTRIB_HTML = "html"
ATTRIB_LAST_UPDATE = "last_update"
ATTRIB_TEAMS_STANDINGS = "teams_standings"

SERVICE_REFRESH_CONFIG = "refresh_config"
SERVICE_REFRESH_EVENT = "refresh_event"
SERVICE_REFRESH_SESSIONS = "refresh_sessions"
SERVICE_REFRESH_STANDINGS = "refresh_standings"
SERVICE_REFRESH_LIVE = "refresh_live"

TZ_PARIS = "Europe/Paris"
