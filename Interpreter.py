from lib2to3.pgen2.grammar import line


def hw3(input, output):
	fInput = open(input,'r')
	f = open(output,'w')
	stack = []
	for line in fInput:
		if line[0].isalpha():
			parsePrimitive(line, stack, f)
		elif line[0] == ':':
			parseBooleanOrError(line, stack)
	fInput.close()



#def parsePrimitive(line, stack, f):
#	if line.startswith('add'):
#		doAdd(stack)
#	elif line.startswith('sub'):
#		doSub(stack)
#	elif line.startswith('mul'):
#		doMul(stack)
#	elif line.startswith('div'):
#		doDiv(stack)
#	elif line.startswith('rem'):
#		doRem(stack)
#	elif line.startswith('pop'):
#		doPop(stack)
#	elif line.startswith('push'):
#		doPush(stack, line)
#	elif line.startswith('swap'):
#		doSwap(stack)
#	elif line.startswith('neg'):
#		doNeg(stack)
#	elif line.startswith('quit'):
#		doQuit(stack, f)
#   print('hello')

def parsePrimitive(line, stack, f):
    if line.startswith('add'):
        doAdd(stack)
    elif line.startswith('sub'):
        doSub(stack)
    elif line.startswith('mul'):
        doMul(stack)
    elif line.startswith('div'):
        doDiv(stack)
    elif line.startswith('rem'):
        doRem(stack)
    elif line.startswith('pop'):
        doPop(stack)
    elif line.startswith('push'):
        doPush(stack,line)
    elif line.startswith('swap'):
        doSwap(stack)
    elif line.startswith('neg'):
        doNeg(stack)
    elif line.startswith('quit'):
        doQuit(stack, f)
    elif line.startswith('and'):
        doAnd(stack)
    elif line.startswith('or'):
        doOr(stack)

def doOr(stack):


def doAnd(stack):
    if len(stack) < 2:
        return stack.insert(0,':error:')
    elif stack[0][0] == ':' and stack[0][1] != 'e' and stack [1][0] == ':' and stack[1][1] != 'e':
        if stack[0] == ':true:' and stack[1] == ':true:':
            stack.pop(0)
            stack.pop(0)
            return stack.insert(0, ':true:')
        elif stack[0] == ':true:' and stack[1] == ':false:':
            stack.pop(0)
            stack.pop(0)
            return stack.insert(0, ':false:')
        elif stack[0] == ':false:' and stack[1] == ':true:':
            stack.pop(0)
            stack.pop(0)
            return stack.insert(0, ':false:')
        elif stack[0] == ':false:' and stack[1] == 'false':
            stack.pop(0)
            stack.pop(0)
            return stack.insert(0, ':false:')
        else:
            return stack.insert(0, ':error:')
    else:
        return stack.insert(0, ':error:')

def doAdd(stack):
	if len(stack) < 2:
		return stack.insert(0, ':error:')
	elif stack[0][0] == ':' or stack[1][0] == ':':
		return stack.insert(0, ':error:')
	else:
		x = int(stack[1])
		y = int(stack[0])
		stack.pop(0)
		stack.pop(0)
		newTop = x+y
		return stack.insert(0, str(newTop))


def doSub(stack):
	if len(stack) < 2:
		return stack.insert(0, ':error:')
	elif stack[0][0] == ':' or stack[1][0] == ':':
		return stack.insert(0, ':error:')
	else:
		x = int(stack[1])
		y = int(stack[0])
		stack.pop(0)
		stack.pop(0)
		newTop = x-y
		return stack.insert(0, str(newTop))


def doMul(stack):
	if len(stack) < 2:
		return stack.insert(0, ':error:')
	elif stack[0][0] == ':' or stack[1][0] == ':':
		return stack.insert(0, ':error:')
	else:
		x = int(stack[1])
		y = int(stack[0])
		stack.pop(0)
		stack.pop(0)
		newTop = x*y
		return stack.insert(0, str(newTop))


def doDiv(stack):
	if len(stack) < 2:
		return stack.insert(0, ':error:')
	elif stack[0][0] == ':' or stack[1][0] == ':':
		return stack.insert(0, ':error:')
	else:
		x = int(stack[1])
		y = int(stack[0])
		if y == 0:
			return stack.insert(0, ':error:')
		else:
			stack.pop(0)
			stack.pop(0)
			newTop = x//y
			return stack.insert(0, str(newTop))



def doRem(stack):
	if len(stack) < 2:
		return stack.insert(0, ':error:')
	elif stack[0][0] == ':' or stack[1][0] == ':':
		return stack.insert(0, ':error:')
	else:
		x = int(stack[1])
		y = int(stack[0])
		if y == 0:
			return stack.insert(0, ':error:')
		else:
			stack.pop(0)
			stack.pop(0)
			newTop = x % y
			return stack.insert(0, str(newTop))


def doPop(stack):
	if len(stack) < 1:
		return stack.insert(0, ':error:')
	else:
		return stack.pop(0)


def doPush(stack, line):
	getList = line.split()
	if getList[1][0] == '-':
		if getList[1][1:] == '0':
			return stack.insert(0,'0')
		elif getList[1][1:].isdigit():
			return stack.insert(0, getList[1])
		else:
			return stack.insert(0, ':error:')
	elif getList[1].isdigit():
		return stack.insert(0, getList[1])
	else:
        if '.' not in getList[1]:
    		return stack.insert(0, getList[1])
        else:
            return stack.insert(0,':error:')

def doSwap(stack):
	if len(stack) < 2:
		return stack.insert(0, ':error:')
	else:
		x = stack[1]
		y = stack[0]
		stack.pop(0)
		stack.pop(0)
		stack.insert(0, y)
		return stack.insert(0, x)



def doNeg(stack):
	if len(stack) < 1:
		return stack.insert(0, ':error:')
	elif stack[0][0] == ':':
		return stack.insert(0, ':error:')
	else:
		x = int(stack[0])
		stack.pop(0)
		newTop = -1*x
		return stack.insert(0, str(newTop))


def doQuit(stack, f):
	for ele in stack:
		f.write(ele + '\n')
	f.close()




def parseBooleanOrError(line, stack):
	if line[1] == 'e':
		return stack.insert(0,':error:')
	elif line[1] == 't':
		return stack.insert(0,':true:')
	else:
		return stack.insert(0,':false:')