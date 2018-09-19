<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%-- 
    Document   : cls_addtocollection
    Created on : 2018-9-19, 15:17:03
    Author     : agno3
--%>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@page import="java.sql.Statement"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<%
    String main_collection = new String("");
    //从session中获取鉴定id信息
    HttpSession csession = request.getSession();
    String useridString = csession.getAttribute("user_id").toString();
    String clsidString = csession.getAttribute("cls_id").toString();
    
 //从数据库中获取classification这张表中的所需内容
    Class.forName("com.mysql.jdbc.Driver");
    String url2 = "jdbc:mysql://localhost:3306/antiqueiddb?zeroDateTimeBehavior=convertToNull";
    String usename = "root";
    String psw = "1234";
    Connection connection = DriverManager.getConnection(url2, usename, psw);
    Statement statement = connection.createStatement();
    
    String sql = new String("SELECT main_collection FROM mainpage WHERE main_id = " + "\"" + useridString + "_mp" + "\"");
    System.out.println(sql);
    ResultSet rs = statement.executeQuery(sql);
 
    while (rs.next()) {
        main_collection = rs.getString(1);
    }
    System.out.println("main_collection: "+main_collection);
%>
<sql:update var="d" dataSource="jdbc/antiqueid">
    UPDATE mainpage
    SET main_collection = '<%out.print(main_collection);%>#<%out.print(clsidString);%>'
    WHERE main_id = '<%out.print(useridString);%>_mp'
</sql:update>

<script>
    function thisAlert(){
        alert("已加入您的收藏中~");   
        window.location.href='mainpage.jsp';
    }

</script>

<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>加入收藏</title>
    </head>
    <body onload="thisAlert()">

    </body>
</html>
