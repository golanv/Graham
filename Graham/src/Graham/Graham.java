package Graham;

import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class Graham {

    public static void main(String[] args) {
        
        Properties prop = new Properties();
	InputStream input = null;
        
        try {

		input = new FileInputStream("graham.conf");

		// load a properties file
		prop.load(input);

		// get the property value and print it out
                System.out.print("VG Pool: ");
                System.out.println(prop.getProperty("pool"));

                System.out.print("VMs: ");
                String[] db = prop.getProperty("vm").split(",");
                for (int i = 0; i < db.length; i++) {
                    System.out.print(db[i] + ", ");
                    
                }

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
        
        // Read config file which should contain (this should be its own class):
            // VM name
            // Disk name
            // Disk path
        
        // Create LVM Snapshot
        
        // Copy snapshot to disk image
        
        // Backup Verification
        
        // If Verification succeeds, remove snapshot
    }
    
}
