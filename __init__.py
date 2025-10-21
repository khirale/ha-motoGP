"""Initialisation de l'intégration MotoGP Tracker pour Home Assistant."""

import logging
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

# Liste des plateformes supportées
PLATFORMS = ["sensor"]


# ---------- SETUP YAML ----------
async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Appelée si l’intégration est chargée via configuration.yaml (non recommandé)."""
    _LOGGER.debug("[MotoGP] async_setup (YAML) appelé — pas de configuration YAML attendue.")
    hass.data.setdefault(DOMAIN, {})
    return True


# ---------- SETUP VIA CONFIG FLOW ----------
async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Appelée lors de l’ajout de l’intégration via l’interface Home Assistant."""
    _LOGGER.info("[MotoGP] Initialisation de l'intégration via ConfigEntry")
    hass.data.setdefault(DOMAIN, {})

    try:
        # Charge toutes les plateformes (ici : sensor)
        await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
        _LOGGER.info("[MotoGP] Plateformes MotoGP chargées avec succès ✅")
    except Exception as e:
        _LOGGER.exception(f"[MotoGP] Erreur lors du chargement des plateformes : {e}")
        return False

    return True


# ---------- UNLOAD ----------
async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Supprime proprement l’intégration lors de la désinstallation ou du rechargement."""
    _LOGGER.info("[MotoGP] Déchargement de l’intégration.")
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)

    if unload_ok and DOMAIN in hass.data:
        hass.data.pop(DOMAIN)
        _LOGGER.debug("[MotoGP] Domaine supprimé de hass.data")

    return unload_ok


# ---------- RELOAD ----------
async def async_reload_entry(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Rechargement dynamique de l'intégration."""
    _LOGGER.info("[MotoGP] Rechargement de l’intégration demandé.")
    await async_unload_entry(hass, entry)
    await async_setup_entry(hass, entry)
