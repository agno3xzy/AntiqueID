<%@page import="java.net.URLEncoder"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%@ page language="java" import="java.util.*,java.sql.*,javax.servlet.*" pageEncoding="utf-8"%>

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>JSP Page</title>
    </head>
    <body>
        <%

            String expertInfo = request.getParameter("expertInfo");
            String userEmail = request.getParameter("user_email");
            expertInfo = "\"" + expertInfo  +"\"";
            String userEmail1 = "\"" + userEmail  +"\"";
            System.out.println("URL参数1：" + expertInfo);
            System.out.println("URL参数2：" + userEmail);

            String driverClass = "com.mysql.jdbc.Driver";
            String url = "jdbc:mysql://localhost:3306/antiqueiddb?zeroDateTimeBehavior=convertToNull";
            String username = "root";
            String password = "1234";
            Class.forName(driverClass);//加载驱动 
            Connection conn = DriverManager.getConnection(url, username, password);//得到连接
            
            String sql = "UPDATE user SET `user_info` = " + expertInfo +" WHERE `user_email` = "+ userEmail1 ;
            
            PreparedStatement pStmt = conn.prepareStatement(sql);
            pStmt.execute();
            
            pStmt.close();
            conn.close();        
        %>
        <sql:update var="updateUser" dataSource="jdbc/antiqueid">
            UPDATE user
            SET user_idenity = 1
            WHERE user_email = <%out.print(userEmail1);%>
        </sql:update>
    </body>
    <form action="mainpage.jsp">
          <input type="text1" hidden="hidden" name="user_email" value=<%out.print(userEmail);%> />
          <input type="submit" value="You submit your information successfully! Click me return!"/>
    </form>
    
</html>
