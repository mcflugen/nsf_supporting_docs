# Facilities and Equipment #

## University of Colorado ##

A comprehensive Research 1 public university, CU Boulder campus has a long
(>50 year) tradition of interdisciplinary research and enjoys formal research
relationships with nearby national research laboratories including NIST, NOAA,
NCAR/UCAR, USGS, and NREL, as well as numerous industry partners.

## Computing

The CSDMS High Performance Computing Cluster (HPCC) beach.colorado.edu is an
8 TFlops Altix XE 1300 SGI cluster (with a total of 704 cores) that consists
of:

- 64 Altix XE320 compute nodes (8 cores; 3 GHz Harpertown processors; 16 GB
  memory)
- 24 Altix XE320 high memory compute nodes (8 cores; 3 GHz Harpertown
  processors; 32 GB memory; 250 GB temporary storage)
- Altix XE250 login node (8 cores; 3 GHz Harpertown processors; 32 GB memory;
  2 TB storage)
- Altix XE250 NFS server (8 cores; 3 GHz Harpertown processors; 16 GB memory;
  250 GB temporary storage)

Computes nodes are connected with both and fully non-blocking quad-data rate
InfiniBand fabric (measured unidirectional bandwidth of 12 Gb/s; bidirectional
bandwidth of 21 Gb/s), as well as gigabit Ethernet.

All nodes are able to access 72 TB (40 TB usable) of RAID storage through NFS.

Beach provides GNU and Intel compilers, a suite of various MPI compilers
(mvapich, mpich, openmpi) that have been optimized for the cluster’s
configuration. Users are also provided with versions of Matlab, IDL, Python,
as well as visualization software.

The main power management is an APC UPS with 30 minutes of uptime at 50%
load. The Beach login node and storage are backed-up by a separate SGI
installed UPS system. Beach is supported by the CU ITS Managed Services
(UnixOps) under contract to CSDMS.

A new supercomputer, funded by NSF under Grant No. AC-1532236, is currently
under procurement. The exact details of the system are not yet determined but
the peak performance will be about 500 TFLOPS. The system will have 10 GPU
nodes containing two NVIDIA K80 GPUs, 5 high-memory nodes with about 1 TB
of main memory and in a second deployment 20 Xeon Phi ("Knight’s Landing")
nodes for development.

## Data Storage

Researchers using the computational resources at CU Boulder will have a home
directory with 2GB and a project space consisting of 250 GB of storage.
Additional storage is provided as part of a storage condominium at a cost of
$100 per TB for single copy storage. Tape and HSM are additional storage
options that are available for archive data.

**PetaLibrary**

The two main categories of services are offered to members of the
PetaLibrary are Active storage for data that needs to be accessed frequently
and Archive storage for data that is accessed infrequently. Active data is
always stored on disk and is accessible to researchers on compute resources
managed by RC. Archive storage consists of a two level hierarchical storage
management (HSM) solution, with disk storage for data that is more likely to
be accessed and tape for data that is less likely to be accessed frequently.
The cost for the research is $100/TB/year for disk and $20/TB/year for tape.

## Web Server

A web server through the Community Surface Dynamics Modeling System
(CSDMS, NSF funded) and the Dartmouth Flood Observatory (DFO, mainly NASA
funded) (Letter of collaboration Syvitski). These two programs purchased a

The CSDMS web server is a PowerEdge R730 Dell Server. The Dell Server contains:

-  8 x 16GB RAM memory capacity
-  2 Intel Xeon E5-2630 v3 2.4GHz, 20M Cache, 8.00GT/s QPI, Turbo, HT, 8
   core/16T (85W) processors
-  8 x 4TB hard drives configured as a RAID 6 to minimize data loss in the
   event of a hard drive failure.

Critical data are backed-up daily through a backup server supported
by the CSDMS program. A backup server, monthly maintenance costs (for both
the web and backup servers) and a seven-year hardware warranty is covered by
CSDMS.

## Peripherals

B&W and Color LaserJet printers, Color Scanners, and a HP Design Jet 5000PS
60” plotter.

## ECI & CSDMS Security

Physical access is restricted out of formal hours, holidays and weekends.
The Facilities electronic locking system is managed by CU Access Services.
The user list is controlled and kept up-to-date.  The OS is RedHat Enterprise
with up-to-date patches. For remote login, clear-text protocols (i.e. FTP,
Telnet) are blocked; SSH connections apply. Login from peripheral PCs and Macs
is via SSH and requires username and password. The ECI benefits from
technical advices and alerts given across the campus network by the central
Colorado University ITS contractor. The ECI is within the CU domain protected
by a firewall. 

## Office space

*Office space*: INSTAAR has access to several conference rooms (that can hold
20 to 60 people). Office space for Postdoctoral position and graduate student
are provided by INSTAAR. Typically, a Postdoctoral fellow could share his
office with one other researcher. Graduate students are typically sharing
offices with 1 or 2 other students.
