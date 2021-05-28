from homeassistant.core import ServiceCall
import logging

from consulate import Consul
from consulate.exceptions import (Forbidden,NotFound)

_LOGGER = logging.Logger(__name__)


def destroy(call:ServiceCall) -> bool:

    host = call.data.get("host", "")
    port = call.data.get("port", 8500)
    token = call.data.get("token", "")
    datacenter = call.data.get("datacenter", None)
    acl_id = call.data.get("acl_id", None)
                    
    consul = Consul(host=host,token=token,datacenter=datacenter,port=port)
    
    try:
        consul.acl.destroy(acl_id=acl_id)
    except Forbidden as e :
        _LOGGER.exception(e,e.args)
    except NotFound as e :
        _LOGGER.exception(e,e.args)
        



    





