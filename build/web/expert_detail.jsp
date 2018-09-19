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

                <form action="follow.jsp">
                    <input type="text1" hidden="hidden" name="expert_id" value=${row.expert_id}>
                    <button type="submit">follow</button>
                </form>

                <%
                    String expert_id_str = request.getParameter("follow");
                    String userid_str = session.getAttribute("user_id").toString();
                    String main_id_str = "\"" + userid_str + "_mp\"";
                    System.out.println(expert_id_str);
                    System.out.println(userid_str);
                    System.out.println(main_id_str);
                    Class.forName("com.mysql.jdbc.Driver");
                    String url2 = "jdbc:mysql://localhost:3306/antiqueiddb?zeroDateTimeBehavior=convertToNull";
                    String usename = "root";
                    String psw = "1234";
                    Connection connection = DriverManager.getConnection(url2, usename, psw);
                    Statement statement = connection.createStatement();
                    String sql = new String("SELECT * FROM  mainpage WHERE main_id = " + main_id_str);
                    System.out.println("sql");
                    ResultSet rs = statement.executeQuery(sql);
                    String main_followexpert_str = new String(" ");
                    if (rs.next()) {
                        main_followexpert_str = rs.getString(3);
                    }
                    main_followexpert_str += "#";
                    main_followexpert_str += expert_id_str;
                    System.out.println(main_followexpert_str);
                %>



                    <sql:update var="d" dataSource="jdbc/antiqueid">
                        UPDATE mainpage
                        SET main_followexpert = <%out.print("\""+main_followexpert_str+"\"");%>
                        WHERE main_id = <%out.print(main_id_str);%>
                    </sql:update>


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