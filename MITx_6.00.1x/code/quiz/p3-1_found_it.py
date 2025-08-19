stuff = [ ( "iBoy", "iGirl", "iQ", "iC","iPaid","iPad") ]
for thing in stuff:
    if thing == 'iPad':
        print "Found it 1"

stuff = ( [ "iBoy", "iGirl", "iQ", "iC","iPaid","iPad" ], )
for thing in stuff:
    if thing == 'iPad':
        print "Found it 2"
