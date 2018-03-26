/*
 * Disk()
 * Version 0.00.01 (Totally safe to compile and use!)
 * <Copyright info here>
 *
 */

package Graham;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.zip.GZIPOutputStream;
import java.security.MessageDigest;

public class Disk {
    
    private String srcPath;
    private String destPath;
    private String srcDisk;
    private String destDisk;
    
    Disk() {
        
    }
    
    Disk(String path, String src) {
        this.srcPath = path;
        this.srcDisk = src;
    }
    
    public static void diskCopy(String srcPath, String srcDisk, String destPath,  String destDisk) throws IOException {
        // File Stream
//        InputStream is = null;
//        OutputStream os = null;
//        try {
//            is = new FileInputStream(srcPath + srcDisk);
//            os = new FileOutputStream(destPath + destDisk);
//            byte[] buffer = new byte[1024];
//            int length;
//            while ((length = is.read(buffer)) > 0 ) {
//                os.write(buffer, 0, length);
//            }
//        } finally {
//            is.close();
//            os.close();
//        }

        // Files.copy() class
        Path src = Paths.get(srcPath + srcDisk);
        Path dst = Paths.get(destPath + destDisk);
        Files.copy(src, dst, StandardCopyOption.REPLACE_EXISTING);
        
    }
    
    public static void diskCompress(String file, String gzipFile) {
        try {
            FileInputStream fis = new FileInputStream(file);
            FileOutputStream fos = new FileOutputStream(gzipFile);
            GZIPOutputStream gzipOS = new GZIPOutputStream(fos);
            byte[] buffer = new byte[1024];
            int len;
            while((len=fis.read(buffer)) != -1){
                gzipOS.write(buffer, 0, len);
            }
            //close resources
            gzipOS.close();
            fos.close();
            fis.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
        
    }
    
    
    

}
