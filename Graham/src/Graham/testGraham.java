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
import java.util.ArrayList;
import java.util.logging.Level;
import java.util.logging.Logger;

public class testGraham {

    public static void main(String[] args) {
        
        // Read config file which should contain (this should be its own class):
        // VM name
        // Disk name
        // Disk path
        
        // Create LVM Snapshot
        
        // Copy snapshot to disk image
        
        // Backup Verification
        
        // Mailer or logger
        
        // If Verification succeeds, remove snapshot
        new testGraham();
    }
    
   public testGraham() {
        Properties prop = new Properties();
	InputStream input = null;
        ArrayList<VirtualMachine> virtM = new ArrayList<>();
        //String destination = null;
        //String destPath = "/backup/";
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
            //System.out.println("Backing up " + virtM.get(i).getName() + "...");
            //String[] diskArray = virtM.get(i).getDisks();
            //for (int j = 0; j < diskArray.length; j++) {
                // Create some variables
                //String pool = virtM.get(i).getPool();
                //String disk = diskArray[j];
                String disk = disks[i];
                // Create snapshot object instance
                Snapshot Snapper = new Snapshot(pool, disk);
                
                String snap = Snapper.getSnapshot();
                

                // Create Snapshot
                Snapper.create();
                System.out.println("Dest Path:" + destPath);
                Snapper.testVars();
                try {
                    Thread.sleep(10000);
                } catch (InterruptedException ex) {
                    Logger.getLogger(Graham.class.getName()).log(Level.SEVERE, null, ex);
                }

                try {
                    // Copy Disk
                    //Disk ds = new Disk();
                    
                    // THIS IS DUMB
                    Disk.diskCopy(pool, snap, destPath, snap);                    
                    
                } catch (IOException ex) {
                    Logger.getLogger(Graham.class.getName()).log(Level.SEVERE, null, ex);
                }
                
                // Checksum
                    
                // Remove snapshot
                Snapper.remove();
                
                // Compress output
                String file = destPath + snap;
                String gzipFile = destPath + snap + ".gz";
                Disk.diskCompress(file, gzipFile);

                // Call mailer/logger

            //}
        }        
    }
    
}
