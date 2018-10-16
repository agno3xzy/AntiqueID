<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%@ page language="java" import="java.util.*,java.sql.*,javax.servlet.*" pageEncoding="utf-8"%>

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="css/mainpage_collection.css">
        <link rel="stylesheet" type="text/css" href="css/mall.css">     
    </head>
    <body>        
        <h1 style="text-align: center">Commodity Request</h1>

        <sql:query var="result" dataSource="jdbc/antiqueid">
            SELECT * FROM commodity where comm_con=0
        </sql:query>

        <c:forEach var="row" items="${result.rows}">
            <div class="commodity">
                <div style="width:170px;height:210px">
                    <img src="${row.comm_img}" style="position:absolute;clip:rect(0px,170px,210px,0px);width:11.5%" alt=""/>
                </div>
                <p class="name"><c:out value="${row.comm_name}"/></p>
                <p class="content"><c:out value="${row.comm_info}"/></p>
                <p>

                <form action="admin_commoditydetails.jsp">
                    <input type="text1" hidden="hidden" name="comm_id" value=${row.comm_id}>
                    <button type="submit">Details</button>
                </form>
                <form action="admin_passcommodity.jsp">
                    <input type="text1" hidden="hidden" name="comm_id" value=${row.comm_id}>
                    <button type="submit">Pass</button>
                </form>
                 <form action="admin_rejectcommodity.jsp">
                    <input type="text1" hidden="hidden" name="comm_id" value=${row.comm_id}>
                    <button type="submit">Reject</button>
                 </form>
            </div>
        </c:forEach>   
    </body>
</html>

