<%-- 
    Document   : index
    Created on : 2018-9-10, 10:43:20
    Author     : Kai98
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>

<%
    HttpSession csession = request.getSession();
    String queryString = new String(csession.getAttribute("user_email").toString());
    String alertOrNot = new String("noAlert");
    if (request.getAttribute("message") != null) {
        String msg = request.getAttribute("message").toString();
        if (msg.equals("请上传图片文件以进行鉴别~")) {
            alertOrNot = "bigAlert";
        }
    }
%>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="css/bottom_navigation.css">
        <link rel="stylesheet" type="text/css" href="css/welcome.css">
        <!--<link rel="stylesheet" type="text/css" href="css/upload.css">-->
        <title>Classification Demo</title>
        <script>
            function bigAlert()
            {
                alert("请上传图片文件以进行鉴别~");
            }
            function noAlert()
            {

            }
        </script>
    </head>
    <body onload="<%out.println(alertOrNot);%>()">
        <!--<form action='/UploadServlet' method='post' enctype='multipart/form-data'>-->
        <!--<input type="file" name="pic" value="选择照片" />-->
        <!--<input type="submit" value="提交" />-->
        <!--<input type="reset" value="清空" />-->
        <!--</form>#-->
        <div class="cotn_principal">
            <div class="cont_centrar">                
                <form id="upload" method="post" action="/AntiqueID/UploadServlet" enctype="multipart/form-data" style="position: absolute; margin-left: 43%;margin-top:10%">
                <h1 class="upload"> 请上传图片：</h1><br><br><br>
                    <h2 class="upload">选择一个文件:</h2><br><br>
                    <input class="upload" type="file" name="uploadFile" />
                    <br><br><br><br><br><br>
                    <button class="btn_sign_up" type="submit">Upload</button>

                </form>


                <div>
                    <ul>
                        <li><a href="mainpage.jsp">主页</a></li>
                        <li><a href="auction.html">拍卖</a></li>
                        <li><a class="active" href="cls_upload.jsp">鉴定</a></li>
                        <li><a href="mall.jsp">商城</a></li>
                        <li style="float:left"><a href="expert_ask.jsp">问答</a></li>
                    </ul>
                </div>
            </div></div>
    </body>
</html>
