<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%-- 
    Document   : mall
    Created on : 2018-9-11, 10:15:26
    Author     : vanit
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@ page import="java.io.*,java.util.*,java.sql.*"%>
<%@ page import="javax.servlet.http.*,javax.servlet.*,javax.servlet.*" %>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <link rel="stylesheet" type="text/css" href="css/stylesheet.css">
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
                    <form action="admin_passcommodity.jsp">
                        <input type="text1" hidden="hidden" name="comm_id" value=${row.comm_id}>
                        <button type="submit">Pass</button>
                    </form>
                    <form action="admin_rejectcommodity.jsp">
                        <input type="text1" hidden="hidden" name="comm_id" value=${row.comm_id}>
                        <button type="submit">Reject</button>
                    </form>
                    <a href="ask.jsp"><button>Ask Expert</button></a>                    
            </p>
        </div>
    </c:forEach>
</body>
</html>