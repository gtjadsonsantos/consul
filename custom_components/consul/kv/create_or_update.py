

from homeassistant.core import ServiceCall
from requests import put
import logging

_LOGGER = logging.Logger(__name__)

def create_or_update(call: ServiceCall) -> bool:

    host = call.data.get("host", None)
    protocol = call.data.get("protocol", "http")
    port = call.data.get("port", 8500)
    token = call.data.get("token", None)
    
    
    key = call.data.get("key", None)
    value = call.data.get("value", None)
    datacenter = call.data.get("datacenter", None)
    flags = call.data.get("flags", None)
    cas = call.data.get("cas", None)
    acquire  = call.data.get("acquire", None)
    release  = call.data.get("release", None)
    ns  = call.data.get("ns", None)
    
    params = {}
    data = None
    headers = {}

    if datacenter: params['dc'] = datacenter
    if value: data = value
    if flags: params['flags'] = flags
    if cas: params['cas'] = cas
    if acquire: params['acquire'] = acquire
    if release: params['release'] = release
    if ns: params['ns'] = ns

    if token:
        headers['X-Consul-Token'] = token
    try:
        response = put("{protocol}://{host}:{port}/v1/kv/{key}".format(protocol=protocol,host=host,port=port,key=key),
        data=data,
        headers=headers,
        params=params
        
        )
        return response.__bool__()
    except IOError as e :
        _LOGGER.exception(e)
        return False

    
