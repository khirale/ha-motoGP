from __future__ import annotations
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

from .const import DOMAIN

class MotoGPConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for MotoGP Tracker."""

    VERSION = 1

    async def async_step_user(self, user_input=None) -> FlowResult:
        """Première étape (UI)."""
        if user_input is not None:
            await self.async_set_unique_id("motogp_tracker_singleton")
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title="MotoGP Tracker", data={})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
            description_placeholders={"info": "Aucune configuration requise."},
        )

    async def async_step_import(self, user_input=None) -> FlowResult:
        """Support import depuis configuration.yaml (optionnel)."""
        return await self.async_step_user(user_input)
