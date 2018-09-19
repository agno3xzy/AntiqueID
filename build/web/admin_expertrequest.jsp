<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%@ page language="java" import="java.util.*,java.sql.*,javax.servlet.*" pageEncoding="utf-8"%>

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="css/mainpage_collection.css">
        <link rel="stylesheet" type="text/css" href="css/mall.css">     
        <link rel="stylesheet" type="text/css" href="css/expert_request.css">
    </head>
    <body>        
        <h1 style="text-align: center">Expert Request</h1>

        <sql:query var="result" dataSource="jdbc/antiqueid">
            SELECT * FROM user where user_idenity=1
        </sql:query>

        <c:forEach var="row" items="${result.rows}">
            <div class="card">
            <img src="${row.user_avatar}" alt="Avatar" style="width:100%">
            <div class="container">
                <h4 id='user_name'>
                    <c:out value="${row.user_email}"/>
                </h4> 
                <p><c:out value="${row.user_info}"/></p>
                
            </div>
            <form action="admin_passexpert.jsp">
                <input type="text1" hidden="hidden" name="user_id" value=${row.user_id}>
                <button type="submit">Pass</button>
            </form>
            <form action="admin_rejectexpert.jsp">
                <input type="text1" hidden="hidden" name="user_id" value=${row.user_id}>
                <button type="submit">Reject</button>
            </form>
        </div>
        </c:forEach>   
    </body>
</html>

