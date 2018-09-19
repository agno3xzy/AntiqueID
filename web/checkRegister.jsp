
<%@ page language="java" import="java.util.*,java.sql.*,javax.servlet.*" pageEncoding="utf-8"%>
<%
    String path = request.getContextPath();
    String basePath = request.getScheme() + "://" + request.getServerName() + ":" + request.getServerPort() + path + "/";
%>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <base href="<%=basePath%>">

        <title>chechRegister</title>

        <meta http-equiv="pragma" content="no-cache">
        <meta http-equiv="cache-control" content="no-cache">
        <meta http-equiv="expires" content="0">    
        <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
        <meta http-equiv="description" content="This is my page">
        <!--
        <link rel="stylesheet" type="text/css" href="styles.css">
        -->

    </head>
    <body>
        <%
             String user = new String(request.getParameter("username").getBytes("ISO-8859-1"), "UTF-8");
            String pwd = request.getParameter("password");
            String driverClass = "com.mysql.jdbc.Driver";
            String url = "jdbc:mysql://localhost:3306/antiqueiddb?zeroDateTimeBehavior=convertToNull";
            String username = "root";
            String password = "1234";
            
            Class.forName(driverClass);//加载驱动 
            Connection conn = DriverManager.getConnection(url, username, password);//得到连接
            
            int maxID = 0;
             try {

            Statement stmt = conn.createStatement();
            ResultSet rs;
 
            rs = stmt.executeQuery("SELECT user_id FROM user  WHERE user_id = (select max(user_id) from user)");
            while ( rs.next() ) {
                maxID = rs.getInt("user_id");
           
            }
            
        } catch (Exception e) {
            System.err.println("Got an exception! ");
            System.err.println(e.getMessage());
        }
    
    
            maxID = maxID + 1;
            String mainpageID = new String(maxID+"_mp");
            PreparedStatement pStmt = conn.prepareStatement("select * from user where user_email = '" + user + "'");
            ResultSet rs = pStmt.executeQuery();
            if (rs.next()) {
                out.println("<script language='javascript'>alert('该用户已存在，请重新注册！');window.location.href='register.jsp';</script>");
            } else {
                PreparedStatement tmt1 = conn.prepareStatement("Insert into mainpage (main_id) values ('" + mainpageID + "')");
                                
                PreparedStatement tmt2 = conn.prepareStatement("Insert into user (`user_email`, `user_passwd`,`mainpage_main_id` ) values   ('" + user + "','" + pwd + "','" + mainpageID +"') ");
                int rst1 = tmt1.executeUpdate();
                int rst2 = tmt2.executeUpdate();
                if (rst1 != 0) {
                    out.println("<script language='javascript'>alert('用户注册成功！');window.location.href='welcome.jsp';</script>");
                } else {
                    out.println("<script language='javascript'>alert('用户注册失败！');window.location.href='welcome.jsp';</script>");
                }
            }
        %>
    </body>
