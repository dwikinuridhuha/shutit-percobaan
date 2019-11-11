import shutit
session = shutit.create_session('bash')
session.login('ssh you@example.com', user='you', password='mypassword')
session.send('hostname', echo=True)
session.logout()