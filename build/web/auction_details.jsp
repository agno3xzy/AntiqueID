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

<html>
    <head>
        <link rel="stylesheet" type="text/css" href="css/bottom_navigation.css">

        <link rel="stylesheet" type="text/css" href="css/cheakbox.css">
       <link rel="stylesheet" type="text/css" href="css/commodity.css">
        <title>拍卖信息</title>
    </head>
    <script>
        function lager(form) {
//            var comparePrice = document.getElementById("sellprice").innerText;
//            var inputPrice = document.getElementById("currentprice").innerText;
            if (form.sellprice.value >= form.currentprice.value) {
                alert("请报价高于目前最高报价");
                return false;
            } else {
                return true;
            }
        }
    </script>
    <body style="overflow-y:scroll">
        <h1 style="text-align:center">Auction Details</h1>
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
                <p class="content"><c:out value="简介:${row.comm_info}"/></p>
                <p class="expertevalution"><c:out value="专家评语:${row.comm_expert_evaluation}"/>
                <p class="price"><c:out value="商品起拍价格:￥${row.comm_startprice}"/></p>
                <p class="price"><c:out value="目前最高竞拍价:￥${row.comm_sellprice}"/></p>
                <p class="content"><input type="checkbox" name="num" value="c" id="3"><label for="3">favorite</label></p>
                <p class="content"><c:out value="您的报价为 "/>
<!--                <p class="content">-->

                <form action="auction_compare.jsp"onsubmit = "return lager(this)">
                    <input id="sellprice" type="text" hidden="hidden" name="sellprice" value="${row.comm_sellprice}" />
                    <input id="currentprice" type="text" name="price" size="1000000" style="width:200px; height:25px" />
                    <input type="text" hidden="hidden" name="comm_id" value=<%out.print(queryString);%> />
                    <input type="submit" value="submit" />
                </form>
            </c:forEach>




            <p> * 注意：1.本页面拍卖商品均于每周日晚0点整确定最终报价，并将其定为商品售价。</p>
        </div>
        <br>
        <div class="buttonDiv">
            <ul>
                <li><a  href="mainpage.jsp">主页</a></li>
                <li><a class="active" href="auction.jsp">拍卖</a></li>
                <li><a href="cls_upload.jsp">鉴定</a></li>
                <li><a href="mall.jsp">商城</a></li>
                <li ><a href="expert_ask.jsp">问答</a></li>
            </ul>
        </div>
    </body>
</html>
