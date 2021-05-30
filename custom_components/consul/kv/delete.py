

from homeassistant.core import ServiceCall
import requests
import logging

_LOGGER = logging.Logger(__name__)

def delete(call: ServiceCall) -> bool:

    host = call.data.get("host", None)
    protocol = call.data.get("protocol", "http")
    port = call.data.get("port", 8500)
    token = call.data.get("token", None)
    
    
    key = call.data.get("key", None)
    datacenter = call.data.get("datacenter", None)
    cas = call.data.get("cas", None)
    recurse  = call.data.get("recurse", None)
    ns  = call.data.get("ns", None)
    
    params = {}
    data = None
    headers = {}

    if datacenter: params['dc'] = datacenter
    if recurse: params['recurse'] = recurse
    if cas: params['cas'] = cas
    if ns: params['ns'] = ns

    if token:
        headers['X-Consul-Token'] = token
    try:
        response = requests.delete("{protocol}://{host}:{port}/v1/kv/{key}".format(protocol=protocol,host=host,port=port,key=key),
        data=data,
        headers=headers,
        params=params
        )
        return response.__bool__()
    except IOError as e :
        _LOGGER.exception(e)
        return False

    
