def revise(assignment, csp, var1, var2, constraint):
	inferences = set([])
	"""Question 5"""
	"""YOUR CODE HERE"""
	# if not consistent(assignment, csp, var1, value):
	# 	return None
	
	if constraint.affects(var1) and constraint.affects(var2):

		var1_val = assignment.varDomains[var1]
		var2_val = assignment.varDomains[var2]

		for v2 in var2_val:
			inferences.add((var2, v2))
			# print inferences
			for v1 in var1_val:
				if constraint.isSatisfied(v1, v2):
					if (var2, v2) in inferences:
						inferences.remove((var2, v2))
		
		# print inferences

		# Remove inconsistent values in var2
		for i in inferences:
			if i[0] == var2:
				assignment.varDomains[i[0]].remove(i[1])
				# print assignment
			# See if var2 is empty
			if len(assignment.varDomains[i[0]]) == 0:
				# print otherVar
				for i in inferences:
					assignment.varDomains[i[0]].add(i[1])
				
				return None

	return inferences