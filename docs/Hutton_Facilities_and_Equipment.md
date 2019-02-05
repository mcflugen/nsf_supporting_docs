# Facilities and Equipment

## University of Colorado

The University of Colorado Boulder is a comprehensive Research 1 public university with a long 
(>50 year) tradition of interdisciplinary research. CU Boulder enjoys formal research relationships 
with nearby national research laboratories, including NIST, NOAA, NCAR/UCAR, USGS, and 
NREL, as well as numerous industry partners.

### Meeting Space

The Institute of Arctic and Alpine Research (INSTAAR) is the anchor of the new Sustainability, 
Energy and Environment Community (SEEC) campus in the University of Colorado Boulder
Research Park. The SEEC campus provides a major conference facility, including an
auditorium, ten conference rooms, six classrooms, and a cafe. All conference rooms, classrooms,
and the auditorium are equipped with projectors and projector screens. The entire
SEEC campus has wireless internet access.

### Main Auditorium

The main auditorium (C120) dimensions are 44' x 53'. If combined with the side rooms C120A/B 
and C120 C/D), the dimensions are 79' x 50'. In the main auditorium, SEEC has a total of 300 chairs 
for use in the rooms. The main auditorium can fit approximately 250 chairs. The side rooms can 
individually seat 30 to 60 depending on format. C120A/B is 17' x 50' when combined. C120A is 
17' x 25', C120B is 17' x 25'. C120C/D is 18' x 49' when combined. C120C is 18' x 24' and C120D is 
18' x 25'. The rooms are separated by soundproof, movable walls and can be divided in five, four, 
three, two or one separate spaces. Maximum room occupancy limits are C120 (412), C120A (81), 
C120B (64), C120C (82), C120D (65), for a total of 704.

The auditorium has a ceiling-mounted Epson G7905UNL 7,000-lumen projector and 137-inch 
tensioned motorized screen with HDMI, VGA, and Mini DisplayPort connections. A Vaddio
RoboSHOT 30x HD PTZ rear camera and Vaddio RoboSHOT 12x HD PTZ front camera provide 
web-based video conferencing.  For voice ampliÞcation, the room is equipped with two Shure 
WL185-lavalier microphones and two Shure SM58 handheld microphones. The auditorium comes 
with two floor microphone stands and two table top microphone stands. Wall-mounted JBL line 
array speakers are positioned on the front wall for program audio, while ceiling-mounted
speakers provide voice reinforcement. There is an ADA-compliant height-adjustable motorized lectern. 

The side rooms each have a ceiling-mounted Epson 2255U 5,000-lumen projector and 137 
inch tensioned motorized screen with HDMI and VGA connections. The content display can be 
duplicated across screens.  Recording is provided by software-based applications running on a
laptop connected to the system.

## Computing

### Blanca HPC Cluster

CSDMS currently owns four compute nodes in a modular high-performance computing cluster 
(HPCC), blanca, that is hosted in a larger compute facility operated by the University of Colorado 
Research Computing group. Each CSDMS compute node on blanca consists of:

-	2x 14-core 2.4 GHz Intel Broadwell processors
-	128 GB RAM at 2400 MHz
-	1x1 TB 7,200 RPM hard drive
-	10 gigabit/s Ethernet

The CSDMS nodes are intended to be used as a testing and learning facility. They are free 
to use (no allocation needed) for CSDMS members. Additional nodes on blanca can be used by 
CSDMS members when not in use by their owners. Blanca is supported by Uninterruptible Power 
Supply (UPS) in the event of a power failure and data (other than stored in the 'scratch' directory) 
is backed up.

**Summit HPC Cluster:**

CSDMS members that are in need of additional compute time, with models that have matured 
from a prototyping and testing phase, can make use of the HPCC summit, also operated by CU's 
Research Computing group. Summit has been operational since February 2017. Summit is a
heterogeneous supercomputing cluster based primarily on the Intel Xeon Haswell CPU, with additional 
NVidia Tesla K80 and high-memory nodes. All nodes sit on a first-generation Intel Omni-Path 
Architecture interconnect, which also provides access to an IBM GPFS Parallel scratch file system. 
Summit consist of:

**General Compute nodes**

-	380 nodes
-	CPU: Intel Xeon E5-2680 v3 @ 2.50GHz (2 CPUs/node, 24 cores/node)
-	Memory: 2,133 MT/s, Dual Rank, x4 Data Width RDIMM, (8x16GB, 128GB/node)
-	Local storage: 200 GB SSD (1/node)

**GPU compute nodes**

-	10 nodes
-	CPU: Intel Xeon E5-2680 v3 @ 2.50GHz (2 CPUs/node, 24 cores/node)
-	Memory: 2,133 MT/s, Dual Rank, x4 Data Width RDIMM (8x16GB, 128GB/node)
-	Local storage: Local storage
-	GPU accelerator: Nvidia Tesla K80 (2/node)

**High-memory compute nodes**

-	5 nodes
-	CPU: Intel Xeon CPU E7-4830 v3 @ 2.10GHz (4 CPUs/node, 48 cores/node)
-	Memory: 2,133 MT/s, Dual Rank, x4 Data Width RDIMM (64x32GB, 2TB/node)
-	Local storage: 1TB 7.2K RPM, 6Gbps Near Line SAS 2.5" Hard Drive (12/node)

**Phi nodes**

-	20 Nodes
-	CPU: Intel Xeon Phi "Knights Landing" processor (1/node)
-	Memory: 128 GiB/node
-	Local storage: 200 GB SSD Data storage on summit is only for short-term, and people can 
make use of the 1.2 PB Scratch storage space that is available.

### Data Storage

Researchers using the computational resources at CU Boulder, either blanca or summit, have a 
home directory with 2 GB of storage and a project directory with 250 GB of storage. Tape and
Hierarchical Storage Management (HSM) are additional storage options that are available for archive 
data.

### PetaLibrary

The two main categories of services offered to members of the PetaLibrary are Active storage 
for data that need to be accessed frequently, and Archive storage for data that are
accessed infrequently. Active data is always stored on disk and is accessible to researchers on compute resources 
managed by Research Computing. Archive storage consists of a two-level HSM solution, with 
disk storage for data that are more likely to be accessed, and tape storage for data that are less 
likely to be accessed. The cost is $100/TB/year for disk and $20/TB/year for tape.

## Server Security

Physical access to the computing resources is restricted. The Facilities' electronic locking system is managed 
by CU Access Services. The user list is controlled and kept up-to-date. The server OS is RedHat 
Enterprise with up-to-date patches. For remote logins, clear-text protocols (i.e. FTP, Telnet) are 
blocked; SSH connections apply. Login from peripheral PCs and Macs is via SSH and requires 
username and password. The University of Colorado campus firewall is part of a
comprehensive and broad-based Office of Information Technology security program to protect campus users 
and its servers from malicious online attacks.
