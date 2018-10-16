<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="sql" uri="http://java.sun.com/jsp/jstl/sql"%>
<%@ page language="java" import="java.util.*,java.sql.*,javax.servlet.*" pageEncoding="utf-8"%>

<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <link rel="stylesheet" type="text/css" href="css/mainpage_collection.css">
    </head>
    <body>
        <%
            HttpSession csession = request.getSession();
            String useremailString = new String(csession.getAttribute("user_email").toString());
            String queryString = new String(csession.getAttribute("main_id").toString());
            String queryString1 = new String(queryString);
            String deleteString = new String(request.getParameter("delete_info"));
            System.out.println("deleteString: " + deleteString);
            queryString = "\"" + queryString + "\"";
            System.out.println("queryString: " + queryString);
            Class.forName("com.mysql.jdbc.Driver");
            String url2 = "jdbc:mysql://localhost:3306/antiqueiddb?zeroDateTimeBehavior=convertToNull";
            String usename = "root";
            String psw = "1234";
            Connection connection = DriverManager.getConnection(url2, usename, psw);
            Statement statement = connection.createStatement();
            String sql = new String("SELECT * FROM  mainpage WHERE main_id = " + queryString);
            ResultSet rs = statement.executeQuery(sql);

            String expertlist[] = {};
            while (rs.next()) {
                String expertlisttemp[] = rs.getString(3).split("#");
                expertlist = expertlisttemp;
            }

            rs.close();
            statement.close();
            String newexpertlistString = new String("");
            for (int i = 0; i < expertlist.length; i++) {
                if (expertlist[i].equals(deleteString) == true) {
                }
                else if (i != expertlist.length - 1 && expertlist[i].equals(deleteString) == false) {
                    newexpertlistString = newexpertlistString + expertlist[i] + "#";
                } else {
                    if (expertlist[i].equals(deleteString) == false) {
                        newexpertlistString = newexpertlistString + expertlist[i];
                    }

                }
            }
            newexpertlistString = "\"" + newexpertlistString + "\"";
            if (newexpertlistString=="\"#\"") {
                    newexpertlistString = "";
                }
            System.out.println("newexpertlistString: " + newexpertlistString);
            String sql2 = new String("UPDATE mainpage SET  main_followexpert = " + newexpertlistString + "WHERE main_id = " + queryString);
            Statement statement2 = connection.createStatement();
            statement2.executeUpdate(sql2);
            if (true) {
                response.sendRedirect("mainpage_followexpert.jsp");
            }
        %>

    </body>
</html>

