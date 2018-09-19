<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<!--
To change this license header, choose License Headers in Project Properties.
To change this template file, choose Tools | Templates
and open the template in the editor.
-->
<%@ page contentType="text/html; charset=UTF-8" %>
<!DOCTYPE html>
<html>
    <head>
     <link rel="stylesheet" type="text/css" href="css/bottom_navigation.css">
        <link rel="stylesheet" type="text/css" href="css/mall.css">

        <title>拍卖</title>
    <body style="overflow-y:scroll">
        <h1 style="text-align:center">拍卖</h1>

        <br>
        <sql:query var="result" dataSource="jdbc/antiqueid">
            SELECT * FROM commodity WHERE comm_con=2
        </sql:query>

        <c:forEach var="row" items="${result.rows}">
            <div class="commodity">
                <div style="width:170px;height:210px">
                    <img src="${row.comm_img}" style="position:absolute;clip:rect(0px,170px,210px,0px);width:11.5%" alt=""/>
                </div>
                <p class="name"><c:out value="${row.comm_name}"/></p>
                <p class="content"><c:out value="${row.comm_info}"/></p>
                <p>

                <form action="auction_details.jsp">
                    <input type="text1" hidden="hidden" name="comm_id" value=${row.comm_id}>
                    <button type="submit">Details</button>
                </form>
               
            </p>
        </div>
    </c:forEach>

       <div class="buttonDiv">
            <ul>
                <li><a class="active" href="mainpage.jsp">主页</a></li>
                <li><a href="auction.jsp">拍卖</a></li>
                <li><a href="cls_upload.jsp">鉴定</a></li>
                <li><a href="mall.jsp">商城</a></li>
                <li ><a href="expert_ask.jsp">问答</a></li>
            </ul>
        </div>
    </body>
</html>



