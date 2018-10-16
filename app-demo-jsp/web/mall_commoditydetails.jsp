<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%-- 
    Document   : mall
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
        <h1 style="text-align:center">Commodity Details</h1>
        <%
            String queryString = request.getParameter("comm_id");
        %>
        <sql:query var="result" dataSource="jdbc/antiqueid">
            SELECT * FROM commodity where comm_id=<%out.print(queryString);%>
        </sql:query>

        <c:forEach var="row" items="${result.rows}">
            <div class="commodity">
                <img src="${row.comm_img}" style="width:100%" alt=""/>
                <p class="name"><c:out value="${row.comm_name}"/></p>
                <p class="price"><c:out value="售价:￥${row.comm_sellprice}"/></p>
                <c:if test="${row.comm_type==1}">
                    <p class="content"><c:out value="种类:马俑"/></p>
                </c:if>
                <c:if test="${row.comm_type==2}">
                    <p class="content"><c:out value="种类:人像"/></p>
                </c:if>
                <c:if test="${row.comm_type==3}">
                    <p class="content"><c:out value="种类:兽像"/></p>
                </c:if>
                <c:if test="${row.comm_type==4}">
                    <p class="content"><c:out value="种类:碗瓶"/></p>
                </c:if>
                <p class="content"><c:out value="简介:${row.comm_info}"/></p>
                <p class="expertevalution"><c:out value="专家评语:${row.comm_expert_evaluation}"/>
                <p>
                    <button>Buy</button>
                    <a href="expert_ask.jsp"><button>Ask Expert</button></a>
                    <button>Contact Seller</button>
                </p>
            </div>
        </c:forEach>

         <div class="buttonDiv">
            <ul>
            <li><a href="mainpage.jsp">主页</a></li>
            <li><a href="auction.jsp">拍卖</a></li>
            <li><a href="cls_upload.jsp">鉴定</a></li>
            <li><a class="active" href="mall.jsp">商城</a></li>
            <li style="float:left"><a href="expert_ask.jsp">问答</a></li>
            </ul>
        </div>
    </body>
</html>