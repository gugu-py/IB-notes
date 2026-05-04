### IB Computer Science HL – **Topic 6: Resource Management**


---

#### 6.1.1 Resources that need to be managed

**Main groups**

| Storage                                                     | Processing                                                             | I/O                                                                       |
| ----------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| • Cache & RAM (primary) • Secondary storage • Disk capacity | • CPU speed (clock rate) • # of cores • Specialised chips (GPU, sound) | • Bandwidth • Screen resolution • Network connectivity • Peripherals 外围设备 |

---

#### 6.1.2 Evaluating resources in different computer systems

- **Supercomputers** – maximise raw computation for simulations. Emphasis on massive parallel CPU/GPU, less on user I/O.
    
- **Mainframes** – always-on, high I/O throughput for transactions; redundant RAM, storage & bandwidth.
    
- **Servers** – balance network bandwidth, storage and RAM to serve many clients concurrently.
    
- **PCs / laptops / chromebooks** – general purpose; specs vary with use-case (e.g. gamers add GPU & RAM).
    
- **Mobile devices (smartphones, tablets)** – convergent tech; limited by size & battery but now powerful CPUs/GPUs.
    
- **Specialised devices (DSLRs, GoPros, PDAs)** – optimised for narrow tasks; minimal extra resources.
    

---

#### 6.1.3 Typical resource limitations & their effects

| Resource           | Too little leads to…                   |
| ------------------ | -------------------------------------- |
| CPU speed / cores  | Long execution times; poor parallelism |
| RAM                | Thrashing: constant paging to disk     |
| Disk space         | Unable to install / store data         |
| Swap / paging file | Virtual memory can’t expand            |
| Bandwidth          | IO waits dominate, low throughput      |
| GPU absence        | CPU bound for graphics                 |

---

#### Core operating-system strategies (HL extension)

- **Multi-tasking** – scheduler shares CPU via: time-slicing, prioritisation, round-robin, FIFO.
    
- **Multi-processing** – extra cores or dedicated GPUs add power but add scheduling complexity.
    
- **Polling vs Interrupts** – polling wastes CPU; interrupts save time but too many = overhead. Default: use interrupts for most devices.
    
- **Blocking & Swapping** – when process waits on I/O, OS swaps it out, freeing RAM.
    



---

#### Memory-management concepts

paging:
- memory management method that uses secondary memory to increase the amount of primary memory;
- transfers data blocks of the same size (“pages”);
- from secondary storage to main storage when they are required;
- and returns them to secondary storage when they are not;

| Term               | What it means                                                                                  | Why it matters                                                      |
| ------------------ | ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **==Paging==**     | Split RAM into equal pages; processes can occupy non-contiguous pages                          | Reduces _external_ fragmentation but causes internal fragmentation. |
| **Virtual Memory** | Presents each process with a contiguous address space starting at 0; MMU maps to real RAM/disk | More processes can run than fit in RAM – classic abstraction.       |
| **Fragmentation**  | _External_ – gaps between blocks; _Internal_ – unused space inside pages                       | Defragment disks (not needed on SSDs).                              |

---

#### Multi-user & dedicated OS environments

- **Single-user single-task** (old Palm OS) → one program, one user.
    
- **Single-user multi-tasking** (macOS, Windows) → one user, many processes.
    
- **Multi-user** (Windows Server, Unix servers) → OS protects each user’s data & processes.
    
- **Dedicated / real-time OS** – optimised for niche hardware or fast, deterministic response (e.g. QNX for medical devices).
    
==role of OS in terms of resource management==:
- OS is an interface between user and hardware. It plays a role of allocating resources to tasks and users, keeping track of the current user, mediate resource conflicts.

---

#### Virtualisation examples

- Virtual memory & virtual storage letters hide hardware complexity.
    
- JVM abstracts OS differences: “write once, run anywhere”.
    

---

#### Exam snapshot

- IB allocates **~9 teaching hours** → ≈ 7 marks in Paper 1 (but past papers sometimes give fewer). Focus on definitions + clear examples.
    

---

**Tip for revision:**  
Practise the IB command terms:

- _Identify_ = name a resource.
    
- _Evaluate_ = discuss pros/cons in context.
    
- _Discuss_ = balanced argument (e.g. interrupts vs polling).  
    Link every answer back to how effective resource use ↑ overall system performance.

![[UWC/CS/_resources/Pasted image 20240912132342.png]]

![[UWC/CS/_resources/Pasted image 20240912132720.png]]

![[UWC/CS/_resources/Pasted image 20240912133832.png]]

![[UWC/CS/_resources/Pasted image 20240912135157.png]]

![[UWC/CS/_resources/Pasted image 20240912135324.png]]

![[UWC/CS/_resources/Pasted image 20240912135936.png]]

![[UWC/CS/_resources/Pasted image 20240912141536.png]]

![[UWC/CS/_resources/Pasted image 20240912141547.png]]

# Patch

virtual machine:
1. a program
2. that imitates an OS environment
3. in another OS
4. to abstractify hardware details

Interrupt definition: a **signal** sent to the processor to **suspend current task** (and work on the interrupting one)

