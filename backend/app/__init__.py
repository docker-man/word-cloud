from flask import Flask

from raven.contrib.flask import Sentry

app = Flask(__name__,
            template_folder="../../frontend/dist",
            static_folder="../../frontend/dist/static")

sentry = Sentry(app, dsn='https://f8ece1bc0e4a4a809a7f9a735c88f0a6:18db107f22f741e5b6b31e1a4063d39c@sentry.xialv.com/2')

from app import routes
