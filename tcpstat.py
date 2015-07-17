import collectd


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
collectd.register_read(read_callback)
