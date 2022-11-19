import pewee
from  contextvars import ContextVar
from fastapi import Depends


from v1.utils.env_variables import Env_variables

env_variables=Env_variables()

DB_NAME= env_variables.db_name
DB_USER= env_variables.db_user
DB_PASS= env_variables.db_pass
DB_HOST= env_variables.db_host
DB_PORT= env_variables.db_port

 
db_state_default={
    "closed":None,
    "conn":None,
    "ctx":None,
    "transactions":None
}

db_state=ContextVar("db_state",default=db_state_default.copy())

class Peweeconnstate(pewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]

db=pewee.PostgresqlDatabase(
    name=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=DB_PORT
)

db.state=Peweeconnstate()

async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()


def get_db(db_state=Depends(reset_db_state)):
    try:
        db.connect()
        yield
    finally:
        if not db.is_closed():
            db.close()