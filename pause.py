import shutit
session = shutit.create_session('bash')
session.pause_point('Have a look around!')
session.send('echo "Did you enjoy your pause point?"', echo=True)