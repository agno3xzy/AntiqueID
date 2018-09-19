
<%@ page language="java" import="java.util.*,javax.servlet.*" pageEncoding="utf-8"%>
<%
    String path = request.getContextPath();
    String basePath = request.getScheme() + "://" + request.getServerName() + ":" + request.getServerPort() + path + "/";
%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html>
    <head>
        <base href="<%=basePath%>">
        <title>register</title>
        <meta http-equiv="pragma" content="no-cache">
        <meta http-equiv="cache-control" content="no-cache">
        <meta http-equiv="expires" content="0">    
        <meta http-equiv="keywords" content="keyword1,keyword2,keyword3">
        <meta http-equiv="description" content="This is my page">
        <!--
        <link rel="stylesheet" type="text/css" href="styles.css">
        -->
        <script>


            function isValid(form)
            {
                if (form.username.value == "")
                {
                    alert("用户名不能为空");
                    return false;
                }
                if (form.password.value != form.newword.value)
                {
                    alert("两次输入的密码不同！");
                    return false;
                } else if (form.password.value == "")
                {
                    alert("用户密码不能为空！");
                    return false;
                } else
                    return true;
            }
        </script>  

    </script>
<body>
    <center>
        <font face="楷体" size="6" color="#000">注册界面</font>
        <form action = "checkRegister.jsp" method = "post" onsubmit = "return isValid(this)">
            <table width="300" height = "180" border="5" bordercolor="#A0A0A0">
                <tr>
                    <th>用户名：</th>
                    <td><input type="text" name="username" value="输入16个字符以内" maxlength = "16" onfocus = "if (this.value == '输入16个字符以内')
                                this.value = ''"></td>
                </tr>
                <tr>
                    <th>输入密码：</th>
                    <td><input type="text" name="password" value="输入20个字符以内" maxlength = "20" onfocus = "if (this.value == '输入20个字符以内')
                                this.value = ''"></td>
                </tr>
                <tr>
                    <th>确认密码：</th>
                    <td><input type="text" name="newword" value="重新输入密码" maxlength = "20" onfocus = "if (this.value == '重新输入密码')
                                this.value = ''"></td>
                </tr>
                <tr>
                    <td colspan = "2" align = "center">
                        <input type="submit" value="注  册"/>    
                        <input type="reset" value="重  置"/>
                    </td>
                </tr>
            </table>
        </form>
    </center>
</body>
