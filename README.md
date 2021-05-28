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
  host: 127.0.0.1
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  datacenter: prod
  node: raspberry
  service:
    id: redis1
    service: redis
    tags:
      - master
      - v1
    port: 8000
  check:
    node: foobar
    checkid: 'service:redis1'
    name: Redis health check
    notes: Script based health check
    status: passing
    serviceid: redis1

```


### consul.catalog_deregister

Directly remove entries in the catalog.

```yaml
service: consul.catalog_deregister
data:
  host: 127.0.0.1
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  node: raspberry
  datacenter: prod
  service_id: freepbx
  check_id: 'service:freepbx'

```


### consul: kv_set_one

Create one key value.


```yaml
service: consul.kv_set_one
data:
  host: 127.0.0.1
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  datacenter: prod
  data:
    item: vpn_public_key
    value: any thing

```

### consul: kv_set_many

Create many key value.

```yaml
service: consul.kv_set_many
data:
  host: 127.0.0.1
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  datacenter: prod
  datas:
    - item: teste1
      value: value test1
    - item: teste2
      value: value test2
```

### consul: kv_set_delete

Delete one key value.

```yaml
service: consul.kv_delete
data:
  host: 127.0.0.1
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  datacenter: prod
  item: teste1

```

### consul: acl_create

Create one ACL

```yaml
service: consul.acl_create
data:
  host: 127.0.0.1
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  datacenter: prod
  name: jadson179
  rules: ""
  acl_type: client
```

### consul: acl_update

Update one ACL

```yaml
service: consul.acl_update
data:
  host: 127.0.0.1
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  datacenter: prod
  name: jadson179
  acl_id: ""
  rules: ""
  acl_type: client
```

### consul: acl_destroy

Destroy one ACL

```yaml
service: consul.acl_destroy
data:
  host: 127.0.0.1
  port: 8500
  token: 57c5d69a-5f19-469b-0543-12a487eecc66
  datacenter: prod
  acl_id: ""
```

## LICENSE 📝

This project use license MIT - see file [LICENSE](LICENSE) for more details
## AUTOR

<table>
  <tr>
    <td align="center"><a href="https://github.com/jadson179"><img src="https://avatars0.githubusercontent.com/u/42282908?s=460&u=79ce909209ebf14da91a2d2517c9b0f9e378a4e1&v=4" width="100px;" alt=""/><br /><sub><b>Jadson Santos</b></sub></a><br /><a href="https://github.com/jadson179/controlid/commits?author=jadson179" title="Code">💻</a> <a href="https://github.com/jadson179" title="Design">🎨</a></td>
</table>





 

