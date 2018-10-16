<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%-- 
    Document   : response
    Created on : 2018-9-13, 9:51:18
    Author     : Kai98
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%@page language="java" import="java.util.*, java.lang.System, java.io.*,java.time.*, java.sql.*,javax.servlet.*"%>
<!DOCTYPE html>

<%
    String img = new String();
    String img_decoded = new String();
    String img_decoded_relative = new String();
    
    String clsID = new String();
    Integer chooseType = new Integer(1);
    
    //对应class_result项。class_result项的信息是“名称#鉴定结果”这样的格式，
    String result = new String("马俑唐三彩#绝世宝物");
    //对应evaluate项，是估价的意思。
    Integer evaluate = new Integer(0);
    
    HttpServletRequest httpRequest=(HttpServletRequest)request;  
    String query = httpRequest.getQueryString();
    chooseType = Integer.parseInt(query.split("&")[0].split("=")[1]);
    clsID = query.split("&")[1].split("=")[1];
    System.out.print(chooseType + " " + clsID);
    
    Class.forName("com.mysql.jdbc.Driver");
    String url2 = "jdbc:mysql://localhost:3306/antiqueiddb?zeroDateTimeBehavior=convertToNull";
    String usename = "root";
    String psw = "1234";
    Connection connection = DriverManager.getConnection(url2, usename, psw);
    Statement statement = connection.createStatement();
    String sql = new String("SELECT class_img FROM  classification WHERE class_id = " + "\'" + clsID+ "\'");
    System.out.println(sql);
    ResultSet rs = statement.executeQuery(sql);
    
    while(rs.next()){
        img = rs.getString(1);
        System.out.println(img);
    }
    rs.close();
    statement.close();
    connection.close();
    
    String[] img_cut = img.split("#");
    for(int i=0; i<img_cut.length-1; i++){
        img_decoded += img_cut[i];
        img_decoded += "\\";
    }
    img_decoded += img_cut[img_cut.length-1];
    img_decoded_relative = img_decoded.split("web\\\\")[1];
    System.out.println(img_decoded);
    System.out.println(img_decoded_relative);
    

%>
<sql:update var="insertFilePath" dataSource="jdbc/antiqueid">
    UPDATE classification SET class_choose_type = <%out.print(chooseType);%>, 
                              class_result = '<%out.print(result);%>', 
                              class_evaluate = '<%out.print(evaluate);%>' 
    WHERE class_id = '<%out.print(clsID);%>' 
</sql:update>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="format-detection" content="telephone=no">
        <meta name="msapplication-tap-highlight" content="no">
        <meta name="viewport" content="user-scalable=no, initial-scale=1, maximum-scale=1, minimum-scale=1, width=device-width">
        <link rel="stylesheet" type="text/css" href="css/bottom_navigation.css">
        <link rel="stylesheet" type="text/css" href="css/cls_result.css">
        <title>鉴定结果</title>
    </head>
    <body style="overflow-y:scroll">
        <h1 style="text-align:center">鉴定结果</h1>
        <div class="result">
            <img src= <%out.println(img_decoded_relative);%>>
            <p class="name">马俑唐三彩</p>
            <p class="content">您的鉴定ID：<%out.println(clsID);%><br/>
                               您的鉴定结果：绝世宝物
            </p>
            <a href="cls_addtocomm.jsp"><button>立即出售</button></a>
            <a href="expert_ask.jsp"><button>咨询专家</button></a>
            <a href="cls_addtocollection.jsp"><button>加入我的藏品</button></a>
            
        </div>

         <div class="buttonDiv">
            <ul>
                <li><a href="mainpage.jsp">主页</a></li>
                <li><a href="auction.html">拍卖</a></li>
                <li><a class="active" href="cls_upload.jsp">鉴定</a></li>
                <li><a href="mall.jsp">商城</a></li>
                <li style="float:left"><a href="expert_ask.jsp">问答</a></li>
            </ul>
        </div>
    </body>
</html>
