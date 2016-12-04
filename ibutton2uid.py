from flask import Flask, abort
from ldap.ldapobject import ReconnectLDAPObject
import ldap
from os import getenv

app = Flask(__name__)
ldap_conn = ReconnectLDAPObject(getenv("IBUTTON2UID_LDAP_SERVER"))
ldap_conn.simple_bind_s(getenv("IBUTTON2UID_LDAP_BINDDN"),
        getenv("IBUTTON2UID_LDAP_BINDPW"))

@app.route("/<ibutton>/")
def search_ibuttons(ibutton):
    ldap_results = ldap_conn.search_s(getenv("IBUTTON2UID_LDAP_BASEOU"),
            ldap.SCOPE_SUBTREE, "(&(ibutton=*%s)(ibutton!=x*))" % ibutton)
    if len(ldap_results) != 1:
        abort(404)
    return ldap_results[0][1]['uid'][0].decode('utf-8')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
