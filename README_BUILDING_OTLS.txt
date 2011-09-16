
How to build OTLs
=================

(work-in-progress)

Scripts are now provided for converting between 'compacted' OTLs and
their extracted equivalent (which are small directory structures, almost everything
within represented as ASCII files).


Why
---

Because the compacted OTL files are both non-ASCII and compressed, therefore
even the smallest internal changes are opaque to the version control app (git).


Scripts
-------


./otl_extract.sh

	Looks for all compacted .otl files and extract their contents
	as appropriately named sub-folders.


./otl_delete_extracted.sh

	Deletes all extracted contents, but doesn't touch the compacted .otl files.


./otl_delete_built.sh

	Deletes all compacted .otl files, but keeps all extracted contents.


./otl_build.sh

	Builds compacted .otl files from previously extracted contents.



Workflow
--------

This is yet to be envisioned. :)





