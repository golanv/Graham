/*
 * Snapshot()
 * Version 0.00.01 (Totally safe to compile and use!)
 * 1 March 2018
 * <Copyright info here>
 *
*/

package Graham;

import java.io.IOException;
import java.util.logging.Level;
import java.util.logging.Logger;

public class Snapshot {
    
    private String snapshot;
    private String disk;
    private String pool;
    
    // Constructors 
    
    public Snapshot() {
        
    }
    
    public Snapshot(String pool, String disk) {
        this.pool = pool;
        this.disk = disk;
        this.snapshot = disk + "_snapshot";
    }
    
    
    public void testVars() {
        System.out.println("Pool: " + pool);
        System.out.println("Disk: " + disk);
        System.out.println("Snapshot: " + snapshot);
        //System.out.println("lvcreate -L1G -s -n " + pool + snapshot + " " + pool + disk);
    }
    
    public void create() {
        String[] cSnap = {"lvcreate", "-L1G", "-s", "-n", pool + snapshot, pool + disk};
        // Create snapshot
        try {
            Runtime.getRuntime().exec(cSnap);
        } catch (IOException ex) {
            Logger.getLogger(Snapshot.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    public void remove() {
        String[] rSnap = {"lvremove", pool + snapshot};
        // Remove snapshot
        try {
            Runtime.getRuntime().exec(rSnap);
        } catch (IOException ex) {
            Logger.getLogger(Snapshot.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
    
    // Accessors
    
    // Mutators

}
