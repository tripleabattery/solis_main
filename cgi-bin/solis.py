start_html_arch = """
<!DOCTYPE html>
<html>
<head>
<title>SOLIS PREMIERE</title>
<link rel="stylesheet" type="text/css" href="/style/arch.css">
<script src="/javascript/imgswap.js"></script>
</head>
<body>
"""

end_html_arch = "</body></html>"

html_body_arch = """
<div class="title">
<table>
<td>{title}</td>
</table>
</div>
<div class="item">
<a href="javascript:void(0)">
<img id="itempic" src="/img/uploads/{image}" onclick="imgswap('{image}', '{image2}')">
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
<a href="http://dev.sxlis.com/archives/{drop}/{urlprev}" class="left">
<img src="/img/left.svg">
</a>
<a href="http://sxlis.com/" class="logo">
<img src="/img/black_bogo.png">
</a>
<a href="http://dev.sxlis.com/archives/{drop}/{urlnext}" class="right">
<img src="/img/right.svg">
</a>
</div>
</div>
</div>
"""
