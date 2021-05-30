# CONSUL

This custom integration permits Home Assistant to communicate with `consul` through  http requests.

## GETTING STARTED

Paste this property `consul:` in your configuration file

## Services

### consul.catalog_register

A a low level mechanism for directly registering or updating entries in the catalog.


```yaml
service: consul.catalog_register
data:
  host: 192.168.0.21
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  datacenter: dc1
  address: "192.168.0.21"
  node: jadson
  service:
    id: jadson
    service: jadson
    tags:
      - master
      - v1
    port: 8000
  check:
    node: jadson
    checkid: 'service:jadson'
    name: Redis health check
    notes: Script based health check
    status: passing
    serviceid: jadson

```


### consul.catalog_deregister

Directly remove entries in the catalog.

```yaml
service: consul.catalog_deregister
data:
  host: 192.168.0.21
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  node: raspberry
  datacenter: prod
  service_id: freepbx
  check_id: 'service:freepbx'

```

### consul: kv_create_or_update

The /kv endpoints access Consul's simple key/value store, useful for storing service configuration or other metadata

```yaml
service: consul.kv_create_or_update
data:
  host: 192.168.0.21
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  key: jadson179
  value: 'https://github.com/jadson179'
```

### consul: kv_delete

This endpoint deletes a single key or all keys sharing a prefix.


```yaml
service: consul.kv_delete
data:
  host: 192.168.0.21
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  key: jadson179
  datacenter: prod
  ns: default
```


## LICENSE 📝

This project use license MIT - see file [LICENSE](LICENSE) for more details
## AUTOR

<table>
  <tr>
    <td align="center"><a href="https://github.com/jadson179"><img src="https://avatars0.githubusercontent.com/u/42282908?s=460&u=79ce909209ebf14da91a2d2517c9b0f9e378a4e1&v=4" width="100px;" alt=""/><br /><sub><b>Jadson Santos</b></sub></a><br /><a href="https://github.com/jadson179/controlid/commits?author=jadson179" title="Code">💻</a> <a href="https://github.com/jadson179" title="Design">🎨</a></td>
</table>





 

