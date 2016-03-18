# Data Management Plan

## Types of data 

The proposed work will not generate new data directly that would require
archiving, but will enable scientists to carry out complex modeling exercises
on a large array of Earth system data. The developed system will rely heavily
on a variety of data collected from different sources (government agencies,
data centers, research institutions, etc.). The University of Colorado team,
which is in charge of most of the data management aspect of the proposed work,
maintains a sizable archive of a wide range of geophysical, remote sensing and
climate data at the CSDMS computing facilities. The archive contains both the
data itself and detailed metadata from the original data providers or links to
documentation. Most of the data in our archive are available publicly and
freely from the original data sources. In some cases, the original data
providers reserve data distribution rights, limiting the proposing team's
ability to pass the collected data to third parties.

The modeling exercises enabled by the proposed new modeling platform will
result in an explosion of model outputs that our system will be able to archive
along with their provenance information. A key element of the proposed work is
an integrated data management component that handles data from external sources
in the same manner as it treats the data produced from modeling experiments.
This uniform handling will enable users to reuse data from previous experiments
as input for new analyses. While archiving all the model outputs over time will
be impractical, the integrated modeling platform will allow the comprehensive
documentation of the modeling executions offering new levels of
reproducibility.

Survey, interview, and observation data will be collected in order to evaluate
the system. The data will mainly be used to provide feedback to the developers
in how to better serve the user community and will be of little value for
reuse.

## Data and metadata standards

Our proposed system will utilize standard tools and rely heavily on data
standards gaining widespread adoption. A dominant part of the data used in the
modeling tools that our system will support are gridded fields of climate
variables and geophysical data. The most widely accepted format to store such
data is NetCDF (that is the primary choice for Earth System modelers). We will
follow the CF v1.x conventions (and UGRID 0.9 for unstructured meshes), both
for the internal NetCDF data structures, and as the means to embed metadata
into the individual data files. The managing of topological gridded networks
will require some extensions of the CF convention that we will submit to the CF
Metadata Trac maintained at the Lawrence Livermore National Lab (CF
Conventions, 2014). For the naming of data variables, we will use the CSDMS
Standard Name conventions, which will soon provide a crosswalk to the CF
Standard Names. For the virtual globe component of this system, we will employ
KML (an OGC standard), CZML (an open format, based on JSON, that’s used in the
Cesium virtual globe environment) and GeoJSON (a standard quickly gaining in
popularity) for storing model metadata, as well as annotating and visualizing
model outputs.

We will rely heavily on accessing data through Web services, such as the CSDMS
Web Modelling Tools (compose and execute models, query model metadata, and
retrieve model output data), OpenDAP/THREDDS or WaterOneFlow developed by
CUAHSI as part of their Hydrological Information System and the OpenGIS
Consortium Web Features and Web Coverage Services (WFS, WCS) enabling Visual
Globe interfaces. Our primary motivation in adapting particular metadata and
data standards is to build a system that not only complies with established
practices of collaborating institutions within the US, but also supports
interoperability with international partners participating in the construction
of the Global Earth Observing System of Systems (GEOSS).

## Policies for access and sharing and provisions for appropriate protection/privacy

The general data sharing policy of the participating institutions is driven by
openness. None of the proposing institutions impose restrictions on accessing
or distributing data amongst each other or outside the project team unless the
license agreement with the original data providers limits how their data can be
redistributed. To the extent that these license agreements permit, the
proposing team will make both the data from external sources and the analysis
results accessible to outside researchers at no cost through the same data
services the will serve the proposed modeling environment internally. The
proposing team is committed to release modeling results that might attract wide
interests after proper quality control and without any additional grace period.

We anticipate that the data handled in our system will not contain sensitive
information that would require the protection of privacy or national security.
We follow closely the policy changes of our data providers and revise our data
policies according to those changes. For instance, the National Inventory of
Dams developed by the Army Corps of Engineers was originally released to the
scientific community without restrictions and distributed widely from multiple
sources (EPA, USGS).

Survey, interview, and observation data will be maintained in adherence
with the restrictions advised by the applicable Institutional Review Board(s).
Where possible these data will be made available, with documentation, to
members of the user community.
