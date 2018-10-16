<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%-- 
    Document   : cls_addcollection
    Created on : 2018-9-19, 11:20:16
    Author     : agno3
--%>

<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.DriverManager"%>
<%@page import="java.sql.Connection"%>
<%@page import="java.sql.Statement"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<%
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
    String sql = new String("SELECT * FROM classification WHERE class_id = " + "\"" + clsidString + "\"");
    System.out.println(sql);
    ResultSet rs = statement.executeQuery(sql);
    
    //class_id
    String comm_id = new String(clsidString);
    
    //class_choose_type
    Integer comm_type = new Integer(1);
    
    //class_evaluate
    String comm_info = new String();
    
    //class_evaluate
    Integer comm_startprice = new Integer(0);
    
    
    Integer comm_sellprice = new Integer(0);
    
    //class_img
    String comm_img = new String();
    
    //class_result的前半部分
    String comm_name = new String();
    
    //专家评语，另行处理
    String comm_expert_evaluation = new String("");
    
    //商品状态，提交后默认置为0，即待审核。
    Integer comm_con = new Integer(0);
    
    String classification_user_user_id = new String(useridString);
    String classification_class_id = new String(clsidString);

    while (rs.next()) {
        
        comm_type = Integer.parseInt(rs.getString(4));
        comm_info = rs.getString(5).split("#")[1];
        comm_startprice = Integer.parseInt(rs.getString(6));
        comm_img = rs.getString(2);
        comm_name = rs.getString(5).split("#")[0];
    }
%>
<sql:update var="insert" dataSource="jdbc/antiqueid">
    INSERT INTO commodity
    VALUES ('<%out.print(comm_id);%>', <% out.print(comm_type); %>, '<% out.print(comm_info); %>', <%out.print(comm_startprice);%>,
            <%out.print(comm_sellprice);%>, '<%out.print(comm_img);%>', '<%out.print(comm_name);%>', '<%out.print(comm_expert_evaluation);%>', 
            <%out.print(comm_con);%>, <%out.print(classification_user_user_id);%>, '<%out.print(classification_class_id);%>' )
</sql:update>
            
<script>
    function thisAlert(){
        alert("您的商品正在审核中~");   
        window.location.href='mainpage.jsp';
    }

</script>

<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>立即出售</title>
    </head>
    <body onload="thisAlert()">

    </body>
</html>
