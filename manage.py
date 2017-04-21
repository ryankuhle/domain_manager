import os
from flask_script import Manager

from mgr import app
from mgr.database import session, Entry

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

@manager.command
def seed():
    date_added = "10102010"
    # url = "liveryleads"
    web_host = "Vacares"
    host_login = "leo.vacares.com"
    username = "liveryleads"
    password = "badpass987"
    city = "Detroit"
    niche = "Lead Generation"
    forwarding_email = "brandon@liveryleads.com"
    # datetime = "44747"

    for i in range(5):
        entry = Entry(
            url="Test Entry #{}".format(i),
            date_added = date_added,
            web_host = web_host,
            host_login = host_login,
            username = username,
            password = password,
            city = city,
            niche = niche,
            forwarding_email = forwarding_email,
            # datetime = datetime
        )
        session.add(entry)
    session.commit()

if __name__ == "__main__":
    manager.run()
