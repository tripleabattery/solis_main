# MySQL Credentials
mysql = {
    "user" : "evosity_storedev",
    "pass" : "x{_[ym?{fugGinXDqtZ7p~:Pu",
    "host" : "127.0.0.1",
    "database" : "evosity_storedev"

}

# SQL statements for each clothing drop (Most secure way to do this)
drops = {
    "dev" : {
        "getitems" : "SELECT * FROM `Items` WHERE `URL` = '{0}' ",
        "geturls" : "SELECT * FROM `Items`"
        },

    "ss18" : {
        "getitems" : "SELECT * FROM `ss18` WHERE `URL` = '{0}' ",
        "geturls" : "SELECT * FROM `ss18`"
    },

    "aw18" : {
        "getitems" : "SELECT * FROM `aw18` WHERE `URL` = '{0}' ",
        "geturls" : "SELECT * FROM `aw18`"
    }
}
