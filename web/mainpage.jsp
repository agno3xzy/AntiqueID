<%@page import="java.net.URLEncoder"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%@ page language="java" import="java.util.*,java.sql.*,javax.servlet.*" pageEncoding="utf-8"%>

<%
    HttpSession csession = request.getSession();
    String queryString = new String(csession.getAttribute("user_email").toString());
    String queryString123 = new String(csession.getAttribute("main_id").toString());
    System.out.print("This is an main_id:" + queryString123);
    String queryString1 = new String("\"" + queryString + "\"");
    Class.forName("com.mysql.jdbc.Driver");
    String url2 = "jdbc:mysql://localhost:3306/antiqueiddb?zeroDateTimeBehavior=convertToNull";
    String usename = "root";
    String psw = "1234";
    Connection connection = DriverManager.getConnection(url2, usename, psw);
    Statement statement = connection.createStatement();
    String sql = new String("SELECT * FROM  user WHERE user_email = " + queryString1);
    ResultSet rs = statement.executeQuery(sql);
    String mainIdString = "";
%>
<!DOCTYPE html>
<html>
    <script>

        // Get the modal
        var modal = document.getElementById('id01');

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function (event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }

        function test() {
            var userIdenity = <%while (rs.next()) {
                    out.print(rs.getInt(6));%>
            if (userIdenity === 0)
            {
                document.getElementById("user_idenity").innerHTML = "Normal User";
            } else if (userIdenity === 1)
            {
                document.getElementById("user_idenity").innerHTML = "Expert (Pending)";
            } else if (userIdenity === 2)
            {
                document.getElementById("user_idenity").innerHTML = "Expert";
            } else
            {
                document.getElementById("user_idenity").innerHTML = "Expert application failed";
            }
        }
    </script>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="css/mainpage.css">
        <link rel="stylesheet" type="text/css" href="css/bottom_navigation.css">
        <title>Main Page</title>
    </head>
    <body onload = "test()">


        <div class="card">
            <img src="img/img_avatar.png" alt="Avatar" style="width:100%">
            <div class="container">
                <h4 id='user_name'><b>
                        <%out.print(queryString);%>
                    </b></h4> 

                <p id="user_idenity" onclick="test" >
                    Identity Placeholder
                </p>

                <p>    
                    <%

                            out.print(rs.getString(10));
                        }
                        rs.close();
                        statement.close();
                        connection.close();
                    %>
                </p> 
            </div>
        </div>

        <form action="mainpage_collection.jsp">

            <input type="submit" value="collection" />
        </form>


        <form action="mainpage_followexpert.jsp">
            <input type="submit" value="Expert Following" />
        </form>

        <button onclick="document.getElementById('id01').style.display = 'block'" style="width:100%;">Apply Expert</button>

        <div id="id01" class="modal">

            <form class="modal-content animate" action="apply_expert.jsp">
                <div class="imgcontainer">
                    <span onclick="document.getElementById('id01').style.display = 'none'" class="close" title="Close Modal">&times;</span>
                    <img src="img/img_avatar.png" alt="Avatar" class="avatar">
                </div>

                <div class="container">

                    <label for="psw"><b>Expert Info</b></label>
                    <input type="text" placeholder="Enter Your Infomation" name="expertInfo" required>
                    <input type="text1" hidden="hidden" name="user_email" value= <%out.print(queryString1);%>/>
                    <button type="submit">Submit</button>

                </div>

                <div class="container" style="background-color:#f1f1f1">
                    <button type="button" onclick="document.getElementById('id01').style.display = 'none'" class="cancelbtn">Cancel</button>

                </div>
            </form>
        </div>

        <div class="buttonDiv">
            <ul>
                <li><a class="active" href="mainpage.jsp">主页</a></li>
                <li><a href="auction.jsp">拍卖</a></li>
                <li><a href="cls_upload.jsp">鉴定</a></li>
                <li><a href="mall.jsp">商城</a></li>
                <li ><a href="expert_ask.jsp">问答</a></li>
            </ul>
        </div>
    </body>
</html>
