import shutit
session = shutit.create_session('bash')
session.send('telnet', expect='elnet', echo=True)
session.send('open google.com 80', expect='scape character', echo=True)
session.send('GET ', echo=True, check_exit=False)
session.logout()