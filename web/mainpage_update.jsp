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
            String queryString = new String(csession.getAttribute("main_id").toString());
            String queryString1 = queryString;
            String useremailString = new String(csession.getAttribute("user_email").toString());

            
            String deleteString = new String(request.getParameter("delete_info"));
            queryString = new String("\"" + queryString + "\"");
            Class.forName("com.mysql.jdbc.Driver");
            String url2 = "jdbc:mysql://localhost:3306/antiqueiddb?zeroDateTimeBehavior=convertToNull";
            String usename = "root";
            String psw = "1234";
            Connection connection = DriverManager.getConnection(url2, usename, psw);
            Statement statement = connection.createStatement();
            String sql = new String("SELECT * FROM  mainpage WHERE main_id = " + queryString);
            ResultSet rs = statement.executeQuery(sql);

            String colllist[] = {};
            while (rs.next()) {
                String colllisttemp[] = rs.getString(2).split("#");
                colllist = colllisttemp;
            }
            
            rs.close();
            statement.close();
            String newcollliString = "";
           for (int i = 0; i < colllist.length; i++) {   
               if (colllist[i].equals(deleteString)==true) {
                       }
                  else if (i != colllist.length-1 &&colllist[i].equals(deleteString)==false) {
                           newcollliString = newcollliString+colllist[i] + "#";
                       }

                   else{
                       if (colllist[i].equals(deleteString)==false) {
                               newcollliString = newcollliString+colllist[i];
                           }
                   
                   }
                   }
           newcollliString = "\""+newcollliString+"\"";
            if (newcollliString=="\"#\"") {
                    newcollliString = "";
                }
             String sql2 = new String("UPDATE mainpage SET  main_collection = "+ newcollliString +"WHERE main_id = " + queryString);     
               Statement statement2 = connection.createStatement();
               statement2.executeUpdate(sql2);
               if(true){
               response.sendRedirect("mainpage_collection.jsp");
               }
        %>

    </body>
</html>

