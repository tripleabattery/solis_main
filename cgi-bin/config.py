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
        "geturls" : "SELECT `Position`, `URL` FROM `Items` ORDER BY `Items`.`Position` ASC"
        },

    "solispremiere" : {
        "getitems" : "SELECT * FROM `ss18` WHERE `URL` = '{0}' ",
        "geturls" : "SELECT `Position`, `URL` FROM `ss18` ORDER BY `ss18`.`Position` ASC"
    },

    "aw18" : {
        "getitems" : "SELECT * FROM `aw18` WHERE `URL` = '{0}' ",
        "geturls" : "SELECT `Position`, `URL` FROM `aw18` ORDER BY `aw18`.`Position` ASC"
    }
}
