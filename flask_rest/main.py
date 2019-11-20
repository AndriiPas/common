from flask import Flask

from res.main_staff import staff
from res.main_room import room
from res.main_tenants import tenants
from config import run_config

app = Flask(__name__)
app.config.from_object(run_config())

app.register_blueprint(staff)
app.register_blueprint(room)
app.register_blueprint(tenants)




if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
