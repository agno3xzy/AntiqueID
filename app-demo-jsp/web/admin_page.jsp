<%@page import="java.net.URLEncoder"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%@ page language="java" import="java.util.*,java.sql.*,javax.servlet.*" pageEncoding="utf-8"%>


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
    </script>
      
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="css/mainpage.css">
        <title>Admin Main Page</title>
    </head>
    <body>
        <%  
            HttpSession csession = request.getSession();
            String queryString = new String(csession.getAttribute("admin_id").toString());
          queryString = "\"" + queryString + "\"";
        %>
        <sql:query var="result" dataSource="jdbc/antiqueid">
            SELECT * FROM administrator where admin_id=<%out.print(queryString);%>
        </sql:query>

        <%--<c:forEach var="row" items="${result.rows}">--%> 
            <div class="card">
                <img src="img/img_avatar1.png" alt="Avatar" style="width:100%">
                <div class="container">
                    <h4 id='user_name'>
                        <%--<c:out value="${row.admin_email}"/>--%>
                        <%--c:out value="1@1.com"/--%>
                        <%out.print(queryString);%>
                    </h4> 
                    <p>
                        Administrator
                    </p>
                </div>
            </div>
        <%--</c:forEach>--%>
        <a href="admin_commodityrequest.jsp"><button>Commodity Request</button></a>
        <a href="admin_expertrequest.jsp"><button>Expert Requset</button></a>
    </body>
</html>
