<%-- 
    Document   : expert_detail_update
    Created on : 2018-9-19, 22:04:20
    Author     : piao
--%>
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


    </head>

    <body style="overflow-y:scroll">

        <%
            String expert_id_str = request.getParameter("expert_id");
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
//            if(main_followexpert_str != ""){
//                main_followexpert_str += "#";
//            }
            main_followexpert_str = main_followexpert_str+expert_id_str+"#";
            System.out.println(main_followexpert_str);
            response.sendRedirect("expert_detail.jsp?expert_id="+expert_id_str);

        %>
        
         <sql:update var="d" dataSource="jdbc/antiqueid">
                UPDATE mainpage
                SET main_followexpert = <%out.print("\""+main_followexpert_str+"\"");%>
                WHERE main_id = <%out.print(main_id_str);%>
            </sql:update>

    </body>
</html>
