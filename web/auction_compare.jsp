<%@page import="entity.Commodity_.price"%>
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
<%
    String queryString = request.getParameter("comm_id");
    String price = request.getParameter("price");
%>
<script>
    function thisAlert(){
    <sql:query var="sellprice" scope="session" dataSource="jdbc/antiqueid">
    SELECT comm_sellprice FROM commodity WHERE comm_id = <%out.print(queryString);%>
    </sql:query>
    <sql:query var="startprice" scope="session" dataSource="jdbc/aniqueid">
    SELECT comm_startprice FROM commodity WHERE comm_id = <%out.print(queryString);%>
    </sql:query>


    if (<%out.print(Integer.parseInt(price));%> >= ${row.comm_sellprice} && <%out.print(Integer.parseInt(price));%> > ${row.comm_startprice}){
    <sql:update var="price" scope="session" dataSource="jdbc/antiqueid">
    UPDATE commodity
            SET comm_sellprice = <%out.print(Integer.parseInt(price));%>
    WHERE comm_id = <%out.print("\"" + queryString + "\"");%>;
    </sql:update>
    }
    else if (<%out.print(Integer.parseInt(price));%> <= ${row.comm_sellprice}){
<p>请价格高于最高报价</p>
    }
    else{
<p>请输入价格高于起价</p>
    }
    alert("更新价格完成");
    window.location.href("auction_details.jsp?comm_id=" +<%out.print(queryString);%>);
    }

</script>
<html>
    <head>

        <title>compare</title>
    </head>
    <body onload="thisAlert()"><h1 style="text-align:center">Auction Details</h1>

        <sql:query var="result" dataSource="jdbc/antiqueid">
            SELECT * FROM commodity where comm_id=<%out.print(queryString);%>
        </sql:query>

        <script>

        </script>


    </body>
</html>
