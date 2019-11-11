import shutit
session = shutit.create_session('bash')
password = session.get_input('', ispass=True)
session.login('ssh you@example.com', user='you', password=password)
session.send('hostname', echo=True)
session.logout()