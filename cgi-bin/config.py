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
    }
}

page = """
<!DOCTYPE html>
<html>
<head>
<title>SOLIS 2018 S/S Archive</title>
<link rel="stylesheet" type="text/css" href="/style/arch.css">
</head>

<body>

<div class="title">
<table>
<td>{title}</td>
</table>
</div>
<div class="item">
<a href="PLACEHOLDER">
<img src="/img/uploads/{image}">
</a>
</div>
<div class="description">
<table>
<td>{desc}</td>
</table>
</div>

<div class="bogo">
<div>
<div>
<a href="http://dev.sxlis.com/archives/ss18/{idprev}" class="left">
<img src="/img/left.png">
</a>
<a href="http://sxlis.com/" class="logo">
<img src="/img/boxlogo.png">
</a>
<a href="http://dev.sxlis.com/archives/ss18/{idnext}" class="right">
<img src="/img/right.png">
</a>
</div>
</div>
</div>

</body>
"""
