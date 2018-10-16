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
        <link rel="stylesheet" type="text/css" href="css/mall.css">

        <title>商城</title>
    </head>

    <body style="overflow-y:scroll">
        <h1 style="text-align:center">商城</h1>
        <div>
            选择商品种类：
            <select name="pageselect" onchange="self.location.href = options[selectedIndex].value" >
               <OPTION value="mall_my.jsp">马俑</OPTION>
                <OPTION value="mall.jsp">全部</OPTION>
                <OPTION value="mall_rx.jsp">人像</OPTION>
                <OPTION value="mall_sx.jsp">兽像</OPTION>
                <OPTION value="mall_wp.jsp">碗瓶</OPTION>
            </select>
        </div>
        <br>
        <sql:query var="result" dataSource="jdbc/antiqueid">
            SELECT * FROM commodity WHERE comm_con=1
        </sql:query>

        <c:forEach var="row" items="${result.rows}">
            <div class="commodity">
                <div style="width:170px;height:240px">
                    <img src="${row.comm_img}" style="width:100%" />
                </div>
                <p class="name"><c:out value="${row.comm_name}"/></p>
                <p class="content"><c:out value="${row.comm_info}"/></p>
                <p>

                <form action="mall_commoditydetails.jsp">
                    <input type="text1" hidden="hidden" name="comm_id" value=${row.comm_id}>
                    <button type="submit">Details</button>
                </form>
                <button>Buy</button>
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