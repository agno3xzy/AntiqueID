/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.classification.file;

/**
 *
 * @author agno3
 */
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
 
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
 
import org.apache.commons.fileupload.FileItem;
import org.apache.commons.fileupload.disk.DiskFileItemFactory;
import org.apache.commons.fileupload.servlet.ServletFileUpload;


@WebServlet("/UploadServlet")
public class UploadServlet extends HttpServlet {
    private static final long serialVersionUID = 1L;
     
    // 上传文件存储目录
    private static final String UPLOAD_DIRECTORY = "upload";
 
    // 上传配置
    private static final int MEMORY_THRESHOLD   = 1024 * 1024 * 3;  // 3MB
    private static final int MAX_FILE_SIZE      = 1024 * 1024 * 40; // 40MB
    private static final int MAX_REQUEST_SIZE   = 1024 * 1024 * 50; // 50MB
    private Integer RECOMMEND_TYPE = 1;
    
    /**
     * 上传数据及保存文件
     */
    protected void doPost(HttpServletRequest request,
        HttpServletResponse response) throws ServletException, IOException {
        System.out.println("进入了doPost");
        // 检测是否为多媒体上传
        if (!ServletFileUpload.isMultipartContent(request)) {
            // 如果不是则停止
            PrintWriter writer = response.getWriter();
            writer.println("Error: 表单必须包含 enctype=multipart/form-data");
            writer.flush();
            return;
        }
 
        // 配置上传参数
        DiskFileItemFactory factory = new DiskFileItemFactory();
        // 设置内存临界值 - 超过后将产生临时文件并存储于临时目录中
        factory.setSizeThreshold(MEMORY_THRESHOLD);
        // 设置临时存储目录
        factory.setRepository(new File(System.getProperty("java.io.tmpdir")));
 
        ServletFileUpload upload = new ServletFileUpload(factory);
         
        // 设置最大文件上传值
        upload.setFileSizeMax(MAX_FILE_SIZE);
         
        // 设置最大请求值 (包含文件和表单数据)
        upload.setSizeMax(MAX_REQUEST_SIZE);
        
        // 中文处理
        upload.setHeaderEncoding("UTF-8"); 

        // 构造临时路径来存储上传的文件
        // 这个路径相对当前应用的目录
        String uploadPath ="C:\\Users\\agno3\\Documents\\NetBeansProjects\\AntiqueID\\web\\" + UPLOAD_DIRECTORY;
        System.out.println("uploadPath: " + uploadPath);
         
        // 如果目录不存在则创建
        File uploadDir = new File(uploadPath);
        if (!uploadDir.exists()) {
            uploadDir.mkdir();
        }
 
        try {
            // 解析请求的内容提取文件数据
            @SuppressWarnings("unchecked")
            List<FileItem> formItems = upload.parseRequest(request);
 
            if (formItems != null && formItems.size() > 0) {
                // 迭代表单数据
                for (FileItem item : formItems) {
                    // 处理不在表单中的字段
                    if (!item.isFormField()) {
                        System.out.println("进入上传部分");
                        String fileName = new File(item.getName()).getName();
                        System.out.println(fileName);
                        if( !fileName.contains("jpg") && !fileName.contains("jpeg") &&
                            !fileName.contains("png") && !fileName.contains("bmp") && 
                            !fileName.contains("JPG") && !fileName.contains("JPEG") &&
                            !fileName.contains("PNG") && !fileName.contains("BMP") ){
                            request.setAttribute("message", "请上传图片文件以进行鉴别~");
                            getServletContext().getRequestDispatcher("/cls_upload.jsp").forward(
                                request, response);
                        }
                        String filePath = uploadPath + File.separator + fileName;
                        System.out.println(filePath);
                        // 保存文件到硬盘
                        File storeFile = new File(filePath);
                        item.write(storeFile);
                        
                        filePath = filePath.replaceAll("\\\\", "#");
                        System.out.println(filePath);
                        System.out.println("filePath: " + filePath);
                        request.setAttribute("message","文件上传成功!");
                        request.setAttribute("fileName",fileName);
                        request.setAttribute("filePath",filePath);
                    }
                }
            }
        } catch (Exception ex) {
            request.setAttribute("message",
                    "错误信息: " + ex.getMessage());
        }

        getServletContext().getRequestDispatcher("/cls_choose_category.jsp").forward(
            request, response);
         
    }
}