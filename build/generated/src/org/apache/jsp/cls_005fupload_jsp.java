package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class cls_005fupload_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("\n");

    HttpSession csession = request.getSession();
    String queryString = new String(csession.getAttribute("user_email").toString());
    String alertOrNot = new String("noAlert");
    if (request.getAttribute("message") != null) {
        String msg = request.getAttribute("message").toString();
        if (msg.equals("请上传图片文件以进行鉴别~")) {
            alertOrNot = "bigAlert";
        }
    }

      out.write("\n");
      out.write("<html>\n");
      out.write("    <head>\n");
      out.write("        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n");
      out.write("        <link rel=\"stylesheet\" type=\"text/css\" href=\"css/bottom_navigation.css\">\n");
      out.write("        <!--<link rel=\"stylesheet\" type=\"text/css\" href=\"css/upload.css\">-->\n");
      out.write("        <title>Classification Demo</title>\n");
      out.write("        <script>\n");
      out.write("            function bigAlert()\n");
      out.write("            {\n");
      out.write("                alert(\"请上传图片文件以进行鉴别~\");\n");
      out.write("            }\n");
      out.write("            function noAlert()\n");
      out.write("            {\n");
      out.write("\n");
      out.write("            }\n");
      out.write("        </script>\n");
      out.write("    </head>\n");
      out.write("    <body onload=\"");
out.println(alertOrNot);
      out.write("()\">\n");
      out.write("        <h1>请上传图片：</h1>\n");
      out.write("        <!--<form action='/UploadServlet' method='post' enctype='multipart/form-data'>-->\n");
      out.write("        <!--<input type=\"file\" name=\"pic\" value=\"选择照片\" />-->\n");
      out.write("        <!--<input type=\"submit\" value=\"提交\" />-->\n");
      out.write("        <!--<input type=\"reset\" value=\"清空\" />-->\n");
      out.write("        <!--</form>#-->\n");
      out.write("        <form id=\"upload\" method=\"post\" action=\"/AntiqueID/UploadServlet\" enctype=\"multipart/form-data\">\n");
      out.write("            选择一个文件:\n");
      out.write("            <input type=\"file\" name=\"uploadFile\" />\n");
      out.write("            <br/><br/>\n");
      out.write("            <input type=\"submit\" value=\"上传\" />\n");
      out.write("\n");
      out.write("        </form>\n");
      out.write("\n");
      out.write("\n");
      out.write("         <div class=\"buttonDiv\">\n");
      out.write("            <ul>\n");
      out.write("                <li><a href=\"mainpage.jsp\">主页</a></li>\n");
      out.write("                <li><a href=\"auction.html\">拍卖</a></li>\n");
      out.write("                <li><a class=\"active\" href=\"cls_upload.jsp\">鉴定</a></li>\n");
      out.write("                <li><a href=\"mall.jsp\">商城</a></li>\n");
      out.write("                <li style=\"float:left\"><a href=\"expert_ask.jsp\">问答</a></li>\n");
      out.write("            </ul>\n");
      out.write("        </div>\n");
      out.write("    </body>\n");
      out.write("</html>\n");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
