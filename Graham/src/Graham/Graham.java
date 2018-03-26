/*
 * Graham()
 * Version 0.00.01 (Totally safe to compile and use!)
 * <Copyright info here>
 *
 */

package Graham;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;
//import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Graham {

    public static void main(String[] args) {
        Properties prop = new Properties();
	InputStream input = null;
        String destPath = null;
        String[] disks = null;
        String pool = null;
        
        try {
            
            input = new FileInputStream("/etc/graham.conf");

            // Load a properties file
            prop.load(input);

            // Get the property value and print it out
            
            // Get backup location
            destPath = prop.getProperty("destination");

            // Process Volume Group Pool location
            System.out.print("VG Pool: ");
            System.out.println(prop.getProperty("pool"));
            pool = prop.getProperty("pool");

            // Process Virtual Disks
            System.out.println("Disks: ");
            disks = prop.getProperty("disk").split(",");
            for (int i = 0; i < disks.length; i++) {
                System.out.println(disks[i]);
            }


            System.out.println("------------");

	} catch (IOException ex) {
		ex.printStackTrace();
	} finally {
            if (input != null) {
                try {
                        input.close();
                } catch (IOException e) {
                        e.printStackTrace();
                }
            }
	}

        for (int i = 0; i < disks.length; i++) {
            String disk = disks[i];
            
            // Create snapshot object instance
            Snapshot Snapper = new Snapshot(pool, disk);
            String snap = Snapper.getSnapshot();
            
            String srcSnap = pool + snap;
            String dstSnap = destPath + snap;

            // Create Snapshot
            Snapper.create();
            System.out.println("Dest Path:" + destPath);
            Snapper.testVars();
            try {
                Thread.sleep(10000);
            } catch (InterruptedException ex) {
                Logger.getLogger(Graham.class.getName()).log(Level.SEVERE, null, ex);
            }

            // Copy disk
            try {
                Disk.diskCopy(srcSnap, dstSnap);
            } catch (IOException ex) {
                Logger.getLogger(Graham.class.getName()).log(Level.SEVERE, null, ex);
            }

            try {
                // Checksum
                Disk.diskCheckSum(srcSnap, dstSnap);
            } catch (Exception ex) {
                Logger.getLogger(Graham.class.getName()).log(Level.SEVERE, null, ex);
            }

            // Remove snapshot
            Snapper.remove();

            // Compress output
            //String file = destPath + snap;
            String gzipFile = destPath + snap + ".gz";
            Disk.diskCompress(dstSnap, gzipFile);
        }        
        
        // Read config file which should contain (this should be its own class):
        // VM name
        // Disk name
        // Disk path
        
        // Create LVM Snapshot
        
        // Copy snapshot to disk image
        
        // Backup Verification
        
        // Mailer or logger
        
        // If Verification succeeds, remove snapshot
    }

}
