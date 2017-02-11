def float2str(val, precision=1, length=7):
	if val < 0:
		flstr = ("{:." + str(precision) + "f}").format(val) 
	else:
		flstr = (" {:." + str(precision) + "f}").format(val)
	while len(flstr) < length:
		flstr += " "
	return flstr

def int2str(val, length=5):
	if val < 0:
		instr = str(val)
	else:
		instr = " " + str(val)
	while len(instr) < length:
		instr += " "
	return instr	