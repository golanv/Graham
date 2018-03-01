/*
 * VirtualMachine()
 * Version 0.00.01 (Totally safe to compile and use!)
 * 28 Feb 2018
 * <Copyright info here>
 *
*/

package Graham;

public class VirtualMachine {
    private String name;
    private String pool;
    private String[] disks;
    
    // Constructors
    
    public VirtualMachine() {
        
    }
    
    public VirtualMachine(String name, String pool, String[] disks) {
        this.name = name;
        this.pool = pool;
        this.disks = disks;
    }
    
    // Accessors
    
    public String getName() {
        return name;
    }
    
    public String getPool() {
        return pool;
    }
    
    public String[] getDisks() {
        return disks;
    }
    
    // Mutators

}
