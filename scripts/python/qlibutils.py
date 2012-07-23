"""
		@file		qlibutils.py
		@author		xy
		@since		2012-07-23

		@brief		qLib-related utility functions.

"""

import hou
import re
import traceback




def set_namespace_aliases(prefix="qLib::", verbose=False):
	"""
	Defines (non-)namespaced aliases for operators with a particular namespace prefix.

	This is used for always creating the namespaced versions of assets, even if an
	older .hip file contains non-namespaced asset names.

	Mapping looks like:  <opname>  -->  <prefix>::<opname>

	The namespaced name intentionally doesn't contain any version postfix, so always

	@note
		This function should be called (preferably) on Houdini startup, e.g.

		import qlibutils
		qlibutils.set_namespace_aliases( ["qLib::", "myStuff::"] )

	"""
	if type(prefix) is list:
		for p in prefix: set_namespace_aliases(p)
		return

	assert "::" in prefix, "Include trailing '::' characters in prefix"

	cmds = []
	for file in hou.hda.loadedFiles():

		names = [ (d.nodeType().name(), d.nodeTypeCategory().name()) \
			for d in list(hou.hda.definitionsInFile(file)) \
			if prefix in d.nodeType().name() ]

		for n in names:

			try:
				# strip namespace prefix and version suffix
				old = re.sub("^[^:]+::", "", n[0])
				old = re.search("^[^:]+", old).group(0)	

				# strip version postfix from new (meaning "always use latest")
				new = re.sub("::[0-9.]+$", "", n[0])

				cmd = "opalias %s %s %s" % (n[1], new, old)

				if cmd not in cmds:
					if verbose: print cmd
					hou.hscript(cmd)
					cmds.append(cmd)
				else:
					print "# ALREADY ALIASED: %s (%s)" % (cmd, file)

			except:
				print "ERROR: %s" % traceback.format_exc()





