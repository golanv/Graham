/*
 * Disk()
 * Version 0.00.01 (Totally safe to compile and use!)
 * <Copyright info here>
 *
 */

package Graham;

import java.io.IOException;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.zip.GZIPOutputStream;
//import java.security.MessageDigest;
import java.util.zip.Checksum;

//import javax.xml.bind.DatatypeConverter;
import java.io.File;

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
    
    public static void diskCopy(String src, String dst) throws IOException {
        // Files.copy() class
        Path srcDisk = Paths.get(src);
        Path dstDisk = Paths.get(dst);
        Files.copy(srcDisk, dstDisk, StandardCopyOption.REPLACE_EXISTING);
        
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
    
    public static void diskCheckSum(String src, String dst) throws Exception {
        File srcDisk = new File(src);
        File dstDisk = new File(dst);
        
        if (!Hash.toHex(Hash.SHA256.checksum(srcDisk)).equals(Hash.toHex(Hash.SHA256.checksum(dstDisk)))) {
            System.out.println("ERROR BRO!");
        } else {
            System.out.println("Checksum was awesome");
        }

    }   

}
