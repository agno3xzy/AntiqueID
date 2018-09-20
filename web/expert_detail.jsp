<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%-- 
    Document   : expertdetail
    Created on : 2018-9-11, 10:15:26
    Author     : vanit
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@ page import="java.io.*,java.util.*,java.sql.*"%>
<%@ page import="javax.servlet.http.*,javax.servlet.*" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="css/bottom_navigation.css">
        <link rel="stylesheet" type="text/css" href="css/commodity.css">

        <title>商城</title>
    </head>

    <body style="overflow-y:scroll">
        <h1 style="text-align:center">专家详情</h1>
        <%
            String queryString = request.getParameter("expert_id");

        %>


        <sql:query var="result" dataSource="jdbc/antiqueid">
            SELECT * from expert WHERE expert_id=<%out.print(queryString);%> ;
        </sql:query>


        <c:forEach var="row" items="${result.rows}">


            <c:forEach var="row" items="${result.rows}">

                <p class="name"><c:out value="${row.expert_name}"/></p>
                <p class="content"><c:out value="${row.expert_email}"/></p>
                <p class="content"><c:out value="简介:${row.expert_info}"/></p>
            </c:forEach>
            <form action="contact.jsp">
                <input type="context1" hidden="hidden" name="contact" value=contact">
                <button type="submit">contact</button>
            </form>

            <form action="expert_detail_update.jsp">
                <input type="text1" hidden="hidden" name="expert_id" value=<%out.print(queryString);%>
<!--                       $-{row.expert_id}>-->
                <button type="submit">follow</button>
                        
            </form>



           


        </c:forEach>


        <div class="buttonDiv">
            <ul>
                <li><a  href="mainpage.jsp">主页</a></li>
                <li><a href="auction.jsp">拍卖</a></li>
                <li><a href="cls_upload.jsp">鉴定</a></li>
                <li><a href="mall.jsp">商城</a></li>
                <li ><a class="active" href="expert_ask.jsp">问答</a></li>
            </ul>
        </div>
    </body>
</html>
