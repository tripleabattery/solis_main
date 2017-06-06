<!DOCTYPE HTML>
<html>
    <head>
        <?php
        require_once("Mobile-Detect-2.8.25/Mobile_Detect.php");
        $detect = new Mobile_Detect;
        if ($detect->isMobile()) {
            echo '<link id="style" rel="stylesheet" type="text/css" href="style/mobile_style.css">';
            $plat = "mobile";
        }
        else {
            echo '<link id="style" rel="stylesheet" type="text/css" href="style/style.css">';
            $plat = "desktop";
        }
        ?>
        <meta charset="UTF-8">
        <link rel="icon" type="image/png" href="favicon-32x32.png" sizes="32x32" />
        <link rel="icon" type="image/png" href="favicon-16x16.png" sizes="16x16" />
        <script src="javascript/jquery-3.2.1.slim.min.js"></script>
        <script src="javascript/jquery.mobile-1.5.0-alpha.1.min.js"></script>

        <script>
         var plat = "<?php echo $plat?>";

         $(window).on("orientationchange",function(){
             if (plat == "desktop") {
                 document.getElementById('style').href='style/mobile_style.css'
                 plat = "mobile";
             }

             else if (plat == "mobile") {
                 document.getElementById('style').href='style/style.css'
                 plat = "desktop";
             }
         });
        </script>

        <title>SOLIS</title>
    </head>

    <body>
        <a href="pages/arch.html"> STORE </a>
    </body>


</html>    
