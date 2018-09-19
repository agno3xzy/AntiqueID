<!DOCTYPE html>
<html >
    <head>
        <meta charset="UTF-8">
        <title>Sign Up Login</title>
        <link rel="stylesheet" href="css/welcome.css">
    </head>

    <body>

        <link href="https://fonts.googleapis.com/css?family=Lato" rel="stylesheet">
        <link rel='stylesheet prefetch' href='https://fonts.googleapis.com/icon?family=Material+Icons'>


       <div class="cotn_principal">
            <div class="cont_centrar">
                <div class="cont_login">


                    <div class="cont_forms_admin" >

                        <div class="cont_img_back_"> <img src="img/po.jpg" alt="" /> </div>

                        <div class="cont_forms_active_login_admin" style="position: absolute"> 
                            <h2>ADMIN LOGIN</h2>
                            <div class="ipt"><input class="usrpswd" type="text" placeholder="Email" /></div>
                            <div class="ipt"><input class="usrpswd" type="password" placeholder="Password" /></div>
                            <br>
                            <button class="btn_login" onClick="cambiar_login()">LOGIN</button>
                        </div>

                    </div>

                </div>    
            </div>
            <a href="login.jsp" style="text-decoration : none;"><h3 class="ttb">BACK</h3></a>
        </div>
    <!--
     <center>
         <font face="??" size="6" color="#000" >????</font>
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
<form action = "loginCh.jsp" method="post">
    <table width="300" height = "180" border="5" bordercolor="#A0A0A0"> 
        <tr>
            <th>?  ??</th>
            <td><input type="text" name="name"  value = "??????" maxlength = "16" onfocus = "if (this.value == '??????')
                        this.value = ''"></td>
        </tr>
        <tr>
            <th>?  ??</th>
            <td><input type="password" name="pwd" maxlength = "20"></td>
        </tr>
        <tr>
            <th>? ??</th>
            <td><select name="usertype">
                    <option>normal user</option>
                    <option>expert</option>
                    <option>admin</option>
                </select>
            </td>
        </tr>
        <tr>
            <td colspan = "2" align = "center">
                <input type="submit" name="submit" value="?       ?">
                <input type="button" value="?       ?"
                       onclick="window.location.href('/webText')">
            </td>
        </tr>
    </table>
</form>
</center>
    -->

</body>
</html>
