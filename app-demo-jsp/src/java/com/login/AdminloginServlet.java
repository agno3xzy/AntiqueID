/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.login;

import javax.servlet.annotation.WebServlet;
import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.logging.Level;
import java.util.logging.Logger;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.sql.*;

/**
 *
 * @author agno3
 */
@WebServlet("/AdminloginServlet")
public class AdminloginServlet extends HttpServlet {

    public void doGet(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        request.setCharacterEncoding("UTF-8");
        
        String adminidString = new String(request.getParameter("admin_id"));        
        String pwd = request.getParameter("admin_passwd");
        String driverClass = "com.mysql.jdbc.Driver";
        String url = "jdbc:mysql://localhost:3306/antiqueiddb?zeroDateTimeBehavior=convertToNull";
        String username = "root";
        String password = "1234";

        try {
            Class.forName(driverClass);//加载驱动 
        } catch (ClassNotFoundException ex) {
            Logger.getLogger(LoginServlet.class.getName()).log(Level.SEVERE, null, ex);
        }

        Connection conn = null;
        try {
            conn = DriverManager.getConnection(url, username, password); //得到连接
        } catch (SQLException ex) {
            Logger.getLogger(LoginServlet.class.getName()).log(Level.SEVERE, null, ex);
        }

        PreparedStatement pStmt = null;
        try {
            pStmt = conn.prepareStatement("select * from administrator where admin_id = '" + adminidString + "' and admin_passwd = '" + pwd + "'");
        } catch (SQLException ex) {
            Logger.getLogger(LoginServlet.class.getName()).log(Level.SEVERE, null, ex);
        }

        ResultSet rs = null;
        try {
            rs = pStmt.executeQuery();
        } catch (SQLException ex) {
            Logger.getLogger(LoginServlet.class.getName()).log(Level.SEVERE, null, ex);
        }

        try {
            if (rs.next()) {
                //登陆成功
                //创建session对象
                HttpSession session = request.getSession();
                //把用户数据保存在session域对象中
                session.setAttribute("admin_id", adminidString);
                //跳转到用户主页
                 response.sendRedirect("admin_page.jsp");
//                response.sendRedirect(request.getContextPath() + "/mainpage.jsp");
            } else {
                response.sendRedirect("login_admin.jsp?errNo");//密码不对返回到登陆
            }
        } catch (SQLException ex) {
            Logger.getLogger(LoginServlet.class.getName()).log(Level.SEVERE, null, ex);
        }

        try {
            rs.close();
            pStmt.close();
            conn.close();
        } catch (SQLException ex) {
            Logger.getLogger(LoginServlet.class.getName()).log(Level.SEVERE, null, ex);
        }
       
    }

    public void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        doGet(request, response);
    }
}
