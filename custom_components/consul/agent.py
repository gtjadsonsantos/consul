import logging
from homeassistant.core import ServiceCall
from requests import put
import json

_LOGGER = logging.Logger(__name__)


def service_register(call: ServiceCall) -> bool:
    
    host = call.data.get("host", None)
    host_port = call.data.get("host_port", 8500)
    protocol = call.data.get("protocol", "http")
    token = call.data.get("token", None)

    name = call.data.get("name", None)
    id = call.data.get("id", None)
    tags = call.data.get("tags", None)
    address = call.data.get("address", None)
    taggedaddresses = call.data.get("taggedaddresses", None)
    meta = call.data.get("meta", None)
    port = call.data.get("port", None)
    kind = call.data.get("kind", None)
    proxy = call.data.get("proxy", None)
    connect = call.data.get("connect", None)
    enabletagoverride = call.data.get("enabletagoverride", None)
    weights = call.data.get("weights", None)
    check = call.data.get("check", None)
    checks = call.data.get("checks", None)

    payload = {}
    headers = {}

    if name:
        payload['name'] = name
    if id:
        payload['id'] = id
    if tags:
        payload['tags'] = tags
    if address:
        payload['address'] = address
    if taggedaddresses:
        payload['taggedaddresses'] = taggedaddresses
    if meta:
        payload['meta'] = meta
    if port:
        payload['port'] = int(port)
    if kind:
        payload['kind'] = kind
    if proxy:
        payload['proxy'] = proxy
    if connect:
        payload['connect'] = connect
    if enabletagoverride:
        payload['enabletagoverride'] = enabletagoverride
    if weights:
        payload['weights'] = weights
    if check:
        payload['check'] = check
    if checks:
        payload['checks'] = checks
    if token:
        headers['X-Consul-Token'] = token
    try:
        response = put("{protocol}://{host}:{host_port}/v1/agent/service/register".format(protocol=protocol, host=host, host_port=host_port),
                       data=json.dumps(payload),
                       headers=headers)
        return response.__bool__()
    except IOError as e:
        _LOGGER.exception(e)
        return False


def service_deregister(call: ServiceCall) -> bool:
    host = call.data.get("host", None)
    protocol = call.data.get("protocol", "http")
    host_port = call.data.get("host_port", 8500)
    token = call.data.get("token", None)

    service_id = call.data.get("service_id", None)
    headers = {}

    if token:
        headers['X-Consul-Token'] = token

    try:
        response = put("{protocol}://{host}:{host_port}/v1/agent/service/deregister/{service_id}".format(protocol=protocol, host=host, host_port=host_port, service_id=service_id),
                       headers=headers
                       )
        return response.__bool__()
    except IOError as e:
        _LOGGER.exception(e)
        return False
