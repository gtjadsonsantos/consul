"""The Scheduler Integration."""

from homeassistant.core import (HomeAssistant, Config)

from . import (
    agent,
    catalog,
    kv,
    const
)


def setup(hass: HomeAssistant, config: Config):

    hass.services.register(
        const.DOMAIN, "catalog_register", catalog.service_register)
    hass.services.register(
        const.DOMAIN, "catalog_deregister", catalog.service_deregister)
    hass.services.register(
        const.DOMAIN, "kv_create_or_update", kv.create_or_update)
    hass.services.register(const.DOMAIN, "kv_delete", kv.delete)
    hass.services.register(
        const.DOMAIN, "agent_service_register", agent.service_register)
    hass.services.register(
        const.DOMAIN, "agent_service_deregister", agent.service_deregister)

    return True
