/*
 * Graham()
 * Version 0.00.01 (Totally safe to compile and use!)
 * 28 Feb 2018
 * <Copyright info here>
 *
*/

package Graham;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;
import java.util.ArrayList;

public class Graham {

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
        new Graham();
    }
    
   public Graham() {
        Properties prop = new Properties();
	InputStream input = null;
        ArrayList<VirtualMachine> virtM = new ArrayList<VirtualMachine>();
        
        try {
            
            input = new FileInputStream("/etc/graham.conf");

            // Load a properties file
            prop.load(input);

            // Get the property value and print it out

            // Process Volume Group Pool location
            System.out.print("VG Pool: ");
            System.out.println(prop.getProperty("pool"));
            String pool = prop.getProperty("pool");

            // Process VM Names 
            //System.out.print("VMs: ");
            String[] vm = prop.getProperty("vm").split(",");
            for (int i = 0; i < vm.length; i++) {
                //System.out.print(db[i]);
            }

            // Process Virtual Disks
            System.out.println("Disks: ");
            String[] disk = prop.getProperty("disk").split(";");
            for (int i = 0; i < disk.length; i++) {
                //System.out.println(disk[i]);
                String[] disks = disk[i].split(",");
                for (int j = 0; j < disks.length; j++) {
                    //System.out.println(disks[j]);
                }
            }

            System.out.println("------------");

            // Create object for each VM
            for (int i = 0; i < vm.length; i++) {
                for (int j = 0; j < disk.length; j++) {
                    //System.out.println("VM: " + vm[i] + "| Disks: " + disk[i]);
                    String[] disks = disk[i].split(",");
                    virtM.add(new VirtualMachine(vm[i], pool, disks));
                    break;
                }
            }
            
                        // All in one line...
            /* 
            System.out.println("VMs....");
            String[] vm = prop.getProperty("VirtualMachine").split(";");
            for (int i = 0; i < vm.length; i++) {
                String[] vmDisk = vm[i].split(",");
                System.out.println(vmDisk[i]);
                System.out.println("------------");
                for (int j = 1; j < vmDisk.length; j++) {
                    System.out.println(vmDisk[j]);
                }
            }
                */

            // Test
//                for (int i = 0; i < virtM.size(); i++) {
//                    System.out.println(virtM.get(i).getName());
//                    System.out.println("--------");
//                    String[] diskArray = virtM.get(i).getDisks();
//                    for (int j = 0; j < diskArray.length; j++) {
//                        System.out.println(diskArray[j]);
//                    }
//                }



            

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

        for (int i = 0; i < virtM.size(); i++) {
            System.out.println("Backing up " + virtM.get(i).getName() + "...");
            String[] diskArray = virtM.get(i).getDisks();
            for (int j = 0; j < diskArray.length; j++) {
                // Create some variables
                String pool = virtM.get(i).getPool();
                String disk = diskArray[j];
                // Create snapshot object instance
                Snapshot Snapper = new Snapshot(pool, disk);

                // Create Snapshot
                Snapper.create();

                // Copy Disk

                // Checksum

                // Remove snapshot
                Snapper.remove();

                // Call mailer/logger

            }
        }        
    }
    
}
