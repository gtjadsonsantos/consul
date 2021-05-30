from homeassistant.core import (HomeAssistant,Config)

from .catalog import (
    register,
    deregister
)
from .kv import (
    create_or_update,
    delete
)

from .const import (
    DOMAIN
)

def setup(hass:HomeAssistant, config:Config):    
    
    hass.services.register(DOMAIN, "catalog_register", register.register)
    hass.services.register(DOMAIN, "catalog_deregister", deregister.deregister)
    hass.services.register(DOMAIN, "kv_create_or_update", create_or_update.create_or_update)
    hass.services.register(DOMAIN, "kv_delete", delete.delete)


    return True



