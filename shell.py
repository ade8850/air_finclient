try:
    from IPython.core.debugger import set_trace
except ImportError:
    from pdb import set_trace

from rich.pretty import pprint

from finclient.containers import Container



container = Container()

client = container.client()

set_trace()