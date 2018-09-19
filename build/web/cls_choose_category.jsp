<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%-- 
    Document   : choose_category
    Created on : 2018-9-10, 11:32:19
    Author     : Kai98
--%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page language="java" import="java.util.*, java.lang.System, java.io.*,java.time.*,javax.servlet.*"%>
<!DOCTYPE html>

<%
    HttpSession csession = request.getSession();
    String useridString = csession.getAttribute("user_id").toString();
    System.out.println("进入了choosecategory");
    //获取文件路径
    //String filePath = request.getAttribute("fileName").toString();
    String filePath = request.getAttribute("filePath").toString();
    //生成鉴定ID，存入date字符串中
    System.out.println("准备生成id");
    String today = new String(LocalDate.now().toString().replaceAll("-", ""));
    String now = new String(LocalTime.now().toString().replaceAll(":", "").replace(".", ""));
    System.out.println("today: " + today);
    System.out.println("now: " + now);
    String date = new String(today);
    date += now;
    //将鉴定id设置如session中，方便后续获取
    csession.setAttribute("cls_id", date);

    //运行python代码返回结果
    Process process = Runtime.getRuntime().exec("python D:\\a.py");
    BufferedReader in = new BufferedReader(new InputStreamReader(process.getInputStream()));
    String str = in.readLine();
    process.waitFor();
    Integer recommendType = Integer.parseInt(str);
    System.out.println("recommendType" + recommendType);
    String[] names = new String[10];
    names[1] = "人像俑";
    names[2] = "人头俑";
    names[3] = "马俑";
    names[4] = "天神俑";
    names[5] = "器物俑";
    String[] recommendText = new String[10];
    for (int i = 0; i < 10; i++) {
        recommendText[i] = ".";
    }
    recommendText[recommendType] = "(推荐)";
    System.out.println(recommendText[recommendType]);
    Integer[] predict = new Integer[10];
    predict[1] = 80;
    predict[2] = 10;
    predict[3] = 4;
    predict[4] = 3;
    predict[5] = 3;

%>
<sql:update var="insertFilePath" dataSource="jdbc/antiqueid">
    INSERT INTO classification (class_id, class_img, class_recommend_type, user_user_id) 
    VALUES ("<%out.print(date);%>", "<% out.print(filePath); %>", <% out.print(recommendType); %>, "<%out.print(useridString);%>");
</sql:update>

<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
        <meta name="format-detection" content="telephone=no">
        <meta name="msapplication-tap-highlight" content="no">
        <meta name="viewport" content="user-scalable=no, initial-scale=1, maximum-scale=1, minimum-scale=1, width=device-width">
        <link rel="stylesheet" type="text/css" href="css/bottom_navigation.css">
        <link rel="stylesheet" type="text/css" href="css/cls_choose_category.css">
        <link rel="stylesheet" type="text/css" href="css/welcome.css">        
        <title>Choose the type</title>
    </head>
    <body style="overflow-y: scroll">     
        <div class="cotn_principal">
            <div class="cont_centrar">
                <h1 class="ttl" style="color:white">选择鉴定类别</br><%=request.getAttribute("fileName")%></h1>
                <div style="margin-top:8%;margin-left:22%">
                <div class="photoleft" style="margin-left:20px">

                    <img src="img/img_my.jpg" style="width:100%">
                    <a href="cls_result.jsp?recommendType=1&clsID=<%out.print(date);%>">
                        <button>鉴定马俑<%out.print(recommendText[1]);%></button></a>
                </div>

                <div class="photoleft" style="margin-left:20px">
                    <img src="img/img_rx.jpg" style="width:100%">
                    <a href="cls_result.jsp?recommendType=2&clsID=<%out.print(date);%>">
                        <button>鉴定人像<%out.print(recommendText[2]);%></button></a>
                </div>

                <div class="photoleft" style="margin-left:20px">
                    <img src="img/img_wp.jpg" style="width:100%">
                    <a href="cls_result.jsp?recommendType=3&clsID=<%out.print(date);%>">
                        <button>鉴定碗盆<%out.print(recommendText[3]);%></button></a>
                </div>

                <div class="photoleft" style="margin-left:20px">
                    <img src="img/img_sx.jpg" style="width:99%">
                    <a href="cls_result.jsp?recommendType=4&clsID=<%out.print(date);%>">
                        <button>鉴定兽像<%out.print(recommendText[4]);%></button></a>
                </div>
            </div>
            </div>
        </div>
        <div class="buttonDiv">
            <ul>
                <li><a href="mainpage.jsp">主页</a></li>
                <li><a href="auction.html">拍卖</a></li>
                <li><a class="active" href="cls_upload.jsp">鉴定</a></li>
                <li><a href="mall.html">商城</a></li>
                <li style="float:left"><a href="expert_ask.jsp">问答</a></li>
            </ul>
        </div>

    </body>
</html>
