import logging
from typing import Any, Dict

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import STATE_UNKNOWN

_LOGGER = logging.getLogger(__name__)


class MotoGPEntityBase(SensorEntity):
    """Classe de base pour les capteurs MotoGP."""

    def __init__(self, hass, name: str, unique_id: str, icon: str) -> None:
        self.hass = hass
        self._attr_name = name
        self._attr_unique_id = unique_id
        self._attr_icon = icon
        self._attr_should_poll = False
        self._attr_state = STATE_UNKNOWN
        self._attr_extra_state_attributes: Dict[str, Any] = {}

    async def async_update(self) -> None:
        """Méthode à surcharger dans les sous-classes."""
        pass

    # ---------- Logging utils ----------
    def log_debug(self, msg: str) -> None:
        _LOGGER.debug(f"[{self._attr_name}] {msg}")

    def log_warn(self, msg: str) -> None:
        _LOGGER.warning(f"[{self._attr_name}] {msg}")

    def log_error(self, msg: str) -> None:
        _LOGGER.error(f"[{self._attr_name}] {msg}")

    # ---------- Disponibilité ----------
    @property
    def available(self) -> bool:
        """Retourne True si l'entité a un état défini (non unknown)."""
        return self._attr_state not in (None, STATE_UNKNOWN)
