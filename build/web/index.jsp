<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<sql:query var="result" dataSource="jdbc/antiqueid">
    SELECT * FROM `user`
</sql:query>

<table border="1">
    <!-- column headers -->
    <tr>
        <c:forEach var="columnName" items="${result.columnNames}">
            <th><c:out value="${columnName}"/></th>
            </c:forEach>
    </tr>
    <!-- column data -->
    <c:forEach var="row" items="${result.rowsByIndex}">
        <tr>
            <c:forEach var="column" items="${row}">
                <td><c:out value="${column}"/></td>
            </c:forEach>
        </tr>
    </c:forEach>
</table>
    <sql:query var="result" dataSource="jdbc/antiqueid">
        SELECT * FROM mainpage
    </sql:query>
        
    <table border="1">
        <!-- column headers -->
        <tr>
            <c:forEach var="columnName" items="${result.columnNames}">
                <th><c:out value="${columnName}"/></th>
                </c:forEach>
        </tr>
        <!-- column data -->
        <c:forEach var="row" items="${result.rowsByIndex}">
            <tr>
                <c:forEach var="column" items="${row}">
                    <td><c:out value="${column}"/></td>
                </c:forEach>
            </tr>
        </c:forEach>
    </table> 
    
<code class="language-html"><%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>  
    <%
        String path = request.getContextPath();
        String basePath = request.getScheme() + "://" + request.getServerName() + ":" + request.getServerPort() + path + "/";
    %>  

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">  
    <html>  

        <head>  
            <base href="<%=basePath%>">  
            <title>Starting Page</title>  
            <meta http-equiv="pragma" content="no-cache">  
            <meta http-equiv="cache-control" content="no-cache">  
            <meta http-equiv="expires" content="0">
            <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">  
            <meta http-equiv="description" content="This is my page">  
            <link rel="stylesheet" type="text/css" href="css/index.css">  
        </head>  
        <body>  
            <table width = "200" border ="1" bordercolor = "#00F">  
                <tr> 
                <td><input type = "button" value = "Normal User Login" onclick = "window.location.href='login.jsp'"></td> 
                <td><input type = "button" value = "Expert Login" onclick = "window.location.href='login.jsp'"></td> 
                <td><input type = "button" value = "Admin Login" onclick = "window.location.href='login_admin.jsp'"></td>  
                <td><input type = "button" value = "Register" onclick = "window.location.href='register.jsp'"></td>  
                </tr>   
            </table>  
            </center>  
        </body>  
    </html></code> 
