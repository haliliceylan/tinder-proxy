



# ADDITIONAL METHODS

DOMAINS = [
    {"fake":"api.haliltinder.com","real":"api.gotinder.com"},
]

def change_fake_domain_from_request(string):
    global DOMAINS
    for dom in DOMAINS:
        string = string.replace(dom["fake"],dom["real"])
    return string

def change_fake_domain_from_respond(string):
    global DOMAINS
    for dom in DOMAINS:
        string = string.replace(dom["real"],dom["fake"])
    return string

def gzip_remover(string):
    string = string.replace("gzip,","")
    return string

def location_changer(string):
    string = string.replace('{"lat":37.06,"lon":37.34}','{"lat":36.54,"lon":31.99}')
    if(string.find('{"lat":36.54,"lon":31.99}') != -1):
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"
        print "location modified"

    return string
# MAIN METHOD

def request(string):
    #string = change_fake_domain_from_request(string)
    string = gzip_remover(string)
    string = location_changer(string)
    print "<======================== REQUEST <-> START <-> REQUEST ========================>"
    print string
    print "<======================== REQUEST <-> END <-> REQUEST ========================>"
    return string

def respond(string):
    #string = change_fake_domain_from_respond(string)
    print "<======================== RESPOND <-> START <-> RESPOND ========================>"
    print string
    print "<======================== RESPOND <-> END <-> RESPOND ========================>"
    return string
