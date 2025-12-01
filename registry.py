import datetime
REGISTRY={}
def register_model(name,version,path):
    REGISTRY[name]={"version":version,"path":path,"timestamp":str(datetime.datetime.utcnow())}
def list_models(): return REGISTRY
def get_model_info(name): return REGISTRY.get(name)
