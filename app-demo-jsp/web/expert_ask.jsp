<%-- 
    Document   : ask
    Created on : 2018-9-17, 9:59:13
    Author     : park
--%>

<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%-- 
    Document   : mall
    Created on : 2018-9-11, 10:15:26
    Author     : vanit
--%>
<%
    HttpSession csession = request.getSession();
    String queryString = new String(csession.getAttribute("user_email").toString());
%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@ page import="java.io.*,java.util.*,java.sql.*"%>
<%@ page import="javax.servlet.http.*,javax.servlet.*" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="css/bottom_navigation.css">
        <link rel="stylesheet" type="text/css" href="css/expert_ask.css">
        <link rel="stylesheet" type="text/css" href="css/expert_request.css">
        <link rel="stylesheet" type="text/css" href="css/mall.css">     

        <title>专家</title>
    </head>

    <body style="overflow-y:scroll">
        <h1 style="text-align:center">专家</h1>
        <sql:query var="result" dataSource="jdbc/antiqueid">
             SELECT * from expert;
        </sql:query>

             
        <c:forEach var="row" items="${result.rows}">
            <div class="card">
            <img src="${row.expert_avatar}" alt="Avatar" style="width:100%">
            <div class="container">
                <h4 id='user_name'>
                    <c:out value="${row.expert_name}"/>
                </h4> 
                <p><c:out value="${row.expert_info}"/></p>
                
            </div>                           

                <form action="expert_detail.jsp">
                    <input type="text1" hidden="hidden" name="expert_id" value=${row.expert_id}>
                    <button type="submit">Details</button>
                </form>
                <button>Contact</button>
            </div>
    </c:forEach>

     <div class="buttonDiv">
        <ul>
            <li><a href="mainpage.jsp">主页</a></li>
            <li><a href="auction.jsp">拍卖</a></li>
            <li><a href="cls_upload.jsp">鉴定</a></li>
            <li><a href="mall.jsp">商城</a></li>
            <li style="float:left"><a class="active"href="expert_ask.jsp">问答</a></li>
        </ul>
    </div>
</body>
</html>
