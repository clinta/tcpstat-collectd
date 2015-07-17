import collectd

CONFIGS = []


def configure_callback(conf):
  for node in conf.children:

    promiscuous = True
    linklayer = False

    key = node.key.lower()
    val = node.values

    if key == 'interface':
      interface = val[0]
      continue

    if key == 'promiscuous':
      promiscous = val[0]

    if key == 'linklayer':
      linklayer = val[0]

    if key == 'filter_expr':
      filter_expr = val.join(' ')


def init_callback:


def read(data=None):
  vl = collectd.Values(type='gauge')
  vl.plugin='python.spam'
  vl.dispatch(values=[random.random() * 100])


def write(vl, data=None):
  for i in vl.values:
    print "%s (%s): %f" % (vl.plugin, vl.type, i)


collectd.register_init(init_callback)
collectd.register_config(configure_callback)
ncollectd.register_read(read_callback)
