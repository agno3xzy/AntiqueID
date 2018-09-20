<%@page import="java.beans.Statement"%>
<%@page import="java.sql.SQLException"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>

<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<!DOCTYPE html>
<%@ page contentType="text/html; charset=UTF-8" %>

<script>

</script>
<html>
    <head>

        <title>compare</title>
    </head>
    <body onload="thisAlert()"><h1 style="text-align:center">Auction Details</h1>
        <%
            String queryString = request.getParameter("comm_id");
            String price = request.getParameter("price");
            
            
        %>
        <sql:query var="result" dataSource="jdbc/antiqueid">
            SELECT * FROM commodity where comm_id=<%out.print("\"" + queryString + "\"");%>
        </sql:query>

        <script>
            function thisAlert(){
            
            <sql:update var="price" scope="session" dataSource="jdbc/antiqueid">
            UPDATE commodity
                    SET comm_sellprice = <%out.print(Integer.parseInt(price));%>
            WHERE comm_id = <%out.print("\"" + queryString + "\"");%>;
            </sql:update>
            
            alert("更新价格完成");
            window.location.href("auction_details.jsp?comm_id=" +<%out.print(queryString);%>);
            }

        </script>


    </body>
</html>
