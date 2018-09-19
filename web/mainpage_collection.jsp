<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%@ page language="java" import="java.util.*,java.sql.*,javax.servlet.*" pageEncoding="utf-8"%>

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="css/mainpage_collection.css">
        <link rel="stylesheet" type="text/css" href="css/bottom_navigation.css">
    </head>
    <body>
        <%
            HttpSession csession = request.getSession();
            String useremailString = new String(csession.getAttribute("user_email").toString());
            String queryString = new String(csession.getAttribute("main_id").toString());
            String queryString1 = new String(queryString);

            System.out.println("进入collection");
            System.out.println("main_id: " + queryString);
            System.out.println("user_email: " + useremailString);
            queryString = new String("\"" + queryString + "\"");
            Class.forName("com.mysql.jdbc.Driver");
            String url2 = "jdbc:mysql://localhost:3306/antiqueiddb?zeroDateTimeBehavior=convertToNull";
            String usename = "root";
            String psw = "1234";
            Connection connection = DriverManager.getConnection(url2, usename, psw);
            Statement statement = connection.createStatement();
            String sql = new String("SELECT * FROM  mainpage WHERE main_id = " + queryString);
            ResultSet rs = statement.executeQuery(sql);
            String colllist[] = {};
            while (rs.next()) {
                String colllisttemp[] = rs.getString(2).split("#");
                colllist = colllisttemp;
            }
        %>


        <h2>Collection</h2>

        <%
            for (int i = 0; i < colllist.length; i++) {
                out.print("<form action=\"mainpage_update.jsp\">");
                out.print("<div class=\"alert" + " ");
                if (i % 2 == 0) {
                    out.print("info");
                } else if (i % 2 == 1) {
                    out.print("success");
                }
                out.print("\">");
                out.print("<input type=\"text\" hidden=\"hidden\" name=\"delete_info\" value=\"");
                out.print(colllist[i] + "\" />");
                out.print("<p id=\"" + i);
                out.print("\">" + colllist[i] + "</p>");
                out.print("<input type=\"submit\" value=\"&times;\" name=\"closebtn\" />");
                out.print("</div>");
                out.print("</form>");
            }

        %>

        <div class="buttonDiv">
            <ul>
                <li><a class="active" href="mainpage.jsp">主页</a></li>
                <li><a href="auction.html">拍卖</a></li>
                <li><a href="cls_upload.jsp">鉴定</a></li>
                <li><a href="mall.jsp">商城</a></li>
                <li style="float:left"><a href="expert_ask.jsp">问答</a></li>
            </ul>
        </div>

        <!--
        以下一段JavaScript代码旨在当用户选择删除某条收藏纪录时，同时操纵相应数据库内存储的数据
        -->
        <script>
            var close = document.getElementsByClassName("closebtn");
            var i;

            for (i = 0; i < close.length; i++) {
                close[i].onclick = function () {
                    var div = this.parentElement;
                    div.style.opacity = "0";
                    setTimeout(function () {
                        div.style.display = "none";
                    }, 600);

                };
            }
        </script>
    </body>
</html>


