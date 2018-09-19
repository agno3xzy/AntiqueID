<!DOCTYPE html>
<html >
    <head>
        <meta charset="UTF-8">
        <title>Sign Up Login</title>
        <link rel="stylesheet" href="css/welcome.css">
        <script src="js/welcome.js"></script>
        <script>


            function isValid(form)
            {
                if (form.username.value == "")
                {
                    alert("???????");
                    return false;
                }
                if (form.password.value != form.newword.value)
                {
                    alert("??????????");
                    return false;
                } else if (form.password.value == "")
                {
                    alert("?????????");
                    return false;
                } else
                    return true;
            }
        </script>  
         <%
                    String flag = request.getParameter("errNo");
                    try {
                        if (flag != null) {
                            out.println("???????????");
                        }
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
        %>
    </head>

    <body>

        <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
        <link rel='stylesheet prefetch' href='https://fonts.googleapis.com/icon?family=Material+Icons'>


        <div class="cotn_principal">
            
            <div class="cont_centrar">
                <h1 class="ttl" style="color:white">Main Page</h1>
                <div class="cont_login">
                    <div class="cont_info_log_sign_up">

                        <div class="col_md_login">

                            <div class="cont_ba_opcitiy">
                                <h2>LOGIN</h2>
                                <p style="font-size: 15px">Already have an acount ? Click here.</p>
                                <button class="btn_login" onClick="cambiar_login()">LOGIN</button>
                            </div>

                        </div>

                        <div class="col_md_sign_up">

                            <div class="cont_ba_opcitiy">
                                <h2>SIGN UP</h2>
                                <p style="font-size: 15px">First come here ? Please sign up.</p>
                                <button class="btn_sign_up" onClick="cambiar_sign_up()">SIGN UP</button>
                            </div>

                        </div>

                    </div>

                    <div class="cont_back_info">
                        <div class="cont_img_back_grey"> <img src="img/po.jpg" alt="" /> </div>
                    </div>

                    <div class="cont_forms" >

                        <div class="cont_img_back_"> <img src="img/po.jpg" alt="" /> </div>

                        <div class="cont_form_login"> <a href="#" onClick="ocultar_login_sign_up()" ><i class="material-icons">&#xE5C4;</i></a>
                            <h2>LOGIN</h2>
                            <form action="/AntiqueID/LoginServlet" method="get" >
                                <input class="usrpswd" type="text" name="userEmail" placeholder="Email" maxlength="16"/>
                                <input class="usrpswd" type="password"  name="pwd" placeholder="Password" maxlength="20"/>
                                <button class="btn_login" type="submit" onClick="cambiar_login()">LOGIN</button>
                            </form>
                        </div>

                        <div class="cont_form_sign_up"> <a href="#" onClick="ocultar_login_sign_up()"><i class="material-icons">&#xE5C4;</i></a>
                            <h2>SIGN UP</h2>
                            <form action = "checkRegister.jsp" method = "post" onsubmit = "return isValid(this)">
                                <input class="usrpswd" type="text" name="username"placeholder="Email" />
                                <input class="usrpswd" type="password" name="password" placeholder="Password" />
                                <input class="usrpswd" type="password" name="newword" placeholder="Confirm Password" />                            
                                <button class="btn_sign_up" type="submit">SIGN UP</button>
                            </form>
                        </div>

                    </div>

                </div>    
            </div>
            <a href="login_admin.jsp" style="text-decoration : none;"><h3 class="ttb">ADMIN LOGIN</h3></a>
        </div>
    </body>
</html>