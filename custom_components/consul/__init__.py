from homeassistant.core import (HomeAssistant,Config)

from .catalog import (
    register,
    deregister
)
from .kv.set import (setOne,setMany)
from .kv.delete import (delete)
from .acl.create import create
from .acl.destroy import destroy
from .acl.update import update

from .const import (
    DOMAIN
)

def setup(hass:HomeAssistant, config:Config):    
    
    hass.services.register(DOMAIN, "catalog_register", register.register)
    hass.services.register(DOMAIN, "catalog_deregister", deregister.deregister)

    hass.services.register(DOMAIN, "kv_set_one", setOne)
    hass.services.register(DOMAIN, "kv_set_many", setMany)
    hass.services.register(DOMAIN, "kv_delete", delete)

    hass.services.register(DOMAIN, "acl_create", create)
    hass.services.register(DOMAIN, "acl_destroy", destroy)
    hass.services.register(DOMAIN, "acl_update", update)
    
    






    return True



