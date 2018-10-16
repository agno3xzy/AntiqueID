package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import java.util.*;
import java.lang.System;
import java.io.*;
import java.time.*;
import javax.servlet.*;

public final class cls_005fchoose_005fcategory_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.apache.jasper.runtime.TagHandlerPool _jspx_tagPool_sql_update_var_dataSource;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspInit() {
    _jspx_tagPool_sql_update_var_dataSource = org.apache.jasper.runtime.TagHandlerPool.getTagHandlerPool(getServletConfig());
  }

  public void _jspDestroy() {
    _jspx_tagPool_sql_update_var_dataSource.release();
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

      out.write('\n');
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("\n");

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


      out.write('\n');
      //  sql:update
      org.apache.taglibs.standard.tag.rt.sql.UpdateTag _jspx_th_sql_update_0 = (org.apache.taglibs.standard.tag.rt.sql.UpdateTag) _jspx_tagPool_sql_update_var_dataSource.get(org.apache.taglibs.standard.tag.rt.sql.UpdateTag.class);
      _jspx_th_sql_update_0.setPageContext(_jspx_page_context);
      _jspx_th_sql_update_0.setParent(null);
      _jspx_th_sql_update_0.setVar("insertFilePath");
      _jspx_th_sql_update_0.setDataSource(new String("jdbc/antiqueid"));
      int[] _jspx_push_body_count_sql_update_0 = new int[] { 0 };
      try {
        int _jspx_eval_sql_update_0 = _jspx_th_sql_update_0.doStartTag();
        if (_jspx_eval_sql_update_0 != javax.servlet.jsp.tagext.Tag.SKIP_BODY) {
          if (_jspx_eval_sql_update_0 != javax.servlet.jsp.tagext.Tag.EVAL_BODY_INCLUDE) {
            out = _jspx_page_context.pushBody();
            _jspx_push_body_count_sql_update_0[0]++;
            _jspx_th_sql_update_0.setBodyContent((javax.servlet.jsp.tagext.BodyContent) out);
            _jspx_th_sql_update_0.doInitBody();
          }
          do {
            out.write("\n");
            out.write("    INSERT INTO classification (class_id, class_img, class_recommend_type, user_user_id) \n");
            out.write("    VALUES (\"");
out.print(date);
            out.write("\", \"");
 out.print(filePath); 
            out.write("\", ");
 out.print(recommendType); 
            out.write(", \"");
out.print(useridString);
            out.write("\");\n");
            int evalDoAfterBody = _jspx_th_sql_update_0.doAfterBody();
            if (evalDoAfterBody != javax.servlet.jsp.tagext.BodyTag.EVAL_BODY_AGAIN)
              break;
          } while (true);
          if (_jspx_eval_sql_update_0 != javax.servlet.jsp.tagext.Tag.EVAL_BODY_INCLUDE)
            out = _jspx_page_context.popBody();
            _jspx_push_body_count_sql_update_0[0]--;
        }
        if (_jspx_th_sql_update_0.doEndTag() == javax.servlet.jsp.tagext.Tag.SKIP_PAGE) {
          return;
        }
      } catch (Throwable _jspx_exception) {
        while (_jspx_push_body_count_sql_update_0[0]-- > 0)
          out = _jspx_page_context.popBody();
        _jspx_th_sql_update_0.doCatch(_jspx_exception);
      } finally {
        _jspx_th_sql_update_0.doFinally();
        _jspx_tagPool_sql_update_var_dataSource.reuse(_jspx_th_sql_update_0);
      }
      out.write("\n");
      out.write("\n");
      out.write("<html>\n");
      out.write("    <head>\n");
      out.write("        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n");
      out.write("        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=utf-8\" />\n");
      out.write("        <meta name=\"format-detection\" content=\"telephone=no\">\n");
      out.write("        <meta name=\"msapplication-tap-highlight\" content=\"no\">\n");
      out.write("        <meta name=\"viewport\" content=\"user-scalable=no, initial-scale=1, maximum-scale=1, minimum-scale=1, width=device-width\">\n");
      out.write("        <link rel=\"stylesheet\" type=\"text/css\" href=\"css/bottom_navigation.css\">\n");
      out.write("        <link rel=\"stylesheet\" type=\"text/css\" href=\"css/cls_choose_category.css\">\n");
      out.write("        <link rel=\"stylesheet\" type=\"text/css\" href=\"css/welcome.css\">        \n");
      out.write("        <title>Choose the type</title>\n");
      out.write("    </head>\n");
      out.write("    <body style=\"overflow-y: scroll\">     \n");
      out.write("        <div class=\"cotn_principal\">\n");
      out.write("            <div class=\"cont_centrar\">\n");
      out.write("                <h1 class=\"ttl\" style=\"color:white\">选择鉴定类别</br>");
      out.print(request.getAttribute("fileName"));
      out.write("</h1>\n");
      out.write("                <div class=\"photoleft\">\n");
      out.write("\n");
      out.write("                    <img src=\"img/img_my.jpg\" style=\"width:100%\">\n");
      out.write("                    <a href=\"cls_result.jsp?recommendType=1&clsID=");
out.print(date);
      out.write("\">\n");
      out.write("                        <button>鉴定马俑");
out.print(recommendText[1]);
      out.write("</button></a>\n");
      out.write("                </div>\n");
      out.write("\n");
      out.write("                <div class=\"photoleft\">\n");
      out.write("                    <img src=\"img/img_rx.jpg\" style=\"width:100%\">\n");
      out.write("                    <a href=\"cls_result.jsp?recommendType=2&clsID=");
out.print(date);
      out.write("\">\n");
      out.write("                        <button>鉴定人像");
out.print(recommendText[2]);
      out.write("</button></a>\n");
      out.write("                </div>\n");
      out.write("\n");
      out.write("                <div class=\"photoleft\">\n");
      out.write("                    <img src=\"img/img_wp.jpg\" style=\"width:100%\">\n");
      out.write("                    <a href=\"cls_result.jsp?recommendType=3&clsID=");
out.print(date);
      out.write("\">\n");
      out.write("                        <button>鉴定碗盆");
out.print(recommendText[3]);
      out.write("</button></a>\n");
      out.write("                </div>\n");
      out.write("\n");
      out.write("                <div class=\"photoleft\">\n");
      out.write("                    <img src=\"img/img_sx.jpg\" style=\"width:99%\">\n");
      out.write("                    <a href=\"cls_result.jsp?recommendType=4&clsID=");
out.print(date);
      out.write("\">\n");
      out.write("                        <button>鉴定兽像");
out.print(recommendText[4]);
      out.write("</button></a>\n");
      out.write("                </div>\n");
      out.write("            </div>\n");
      out.write("        </div>\n");
      out.write("        <div class=\"buttonDiv\">\n");
      out.write("            <ul>\n");
      out.write("                <li><a href=\"mainpage.jsp\">主页</a></li>\n");
      out.write("                <li><a href=\"auction.html\">拍卖</a></li>\n");
      out.write("                <li><a class=\"active\" href=\"cls_upload.jsp\">鉴定</a></li>\n");
      out.write("                <li><a href=\"mall.html\">商城</a></li>\n");
      out.write("                <li style=\"float:left\"><a href=\"expert_ask.jsp\">问答</a></li>\n");
      out.write("            </ul>\n");
      out.write("        </div>\n");
      out.write("\n");
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
