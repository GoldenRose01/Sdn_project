import os
import sys
from webob.static import DirectoryApp
from ryu.app.wsgi import ControllerBase, WSGIApplication, route
from ryu.base import app_manager

# Determina il percorso della cartella topologies
TOPOLOGIES_PATH = os.path.join(os.path.dirname(__file__), 'topologies')

class GUIServerApp(app_manager.RyuApp):
    _CONTEXTS = {'wsgi': WSGIApplication}

    def __init__(self, *args, **kwargs):
        super(GUIServerApp, self).__init__(*args, **kwargs)
        wsgi = kwargs['wsgi']
        wsgi.register(GUIServerController)

        # Carica dinamicamente lo script della topologia specificato
        if len(sys.argv) > 2:
            topology_script = sys.argv[2]
            self.load_topology_script(topology_script)

    def load_topology_script(self, script_name):
        script_path = os.path.join(TOPOLOGIES_PATH, script_name)
        if os.path.isfile(script_path):
            sys.path.append(TOPOLOGIES_PATH)
            __import__(os.path.splitext(script_name)[0])
        else:
            print(f"Topology script {script_name} not found.")

class GUIServerController(ControllerBase):
    def __init__(self, req, link, data, **config):
        super(GUIServerController, self).__init__(req, link, data, **config)
        path = os.path.join(os.path.dirname(__file__), 'html')
        self.static_app = DirectoryApp(path)

    @route('gui', '/{filename:[^/]*}')
    def static_handler(self, req, **kwargs):
        if kwargs['filename']:
            req.path_info = kwargs['filename']
        return self.static_app(req)

# Richiede altre applicazioni Ryu
app_manager.require_app('ryu.app.rest_topology')
app_manager.require_app('ryu.app.ofctl_rest')
# Aggiungi qui altre applicazioni Ryu necessarie
