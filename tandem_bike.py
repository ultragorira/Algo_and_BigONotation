def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
	redShirtSpeeds.sort()
	blueShirtSpeeds.sort()
	speed = 0
	
	while len(redShirtSpeeds) > 0:
		if fastest:
			if redShirtSpeeds[-1] >= blueShirtSpeeds[-1]:
				speed += max(redShirtSpeeds[-1], blueShirtSpeeds[0])
				removeItem(redShirtSpeeds, blueShirtSpeeds, -1, 0)
			else:
				speed += max(blueShirtSpeeds[-1], redShirtSpeeds[0])
				removeItem(redShirtSpeeds, blueShirtSpeeds, 0, -1)
		else:
			for i in reversed(redShirtSpeeds):
				speed += max(redShirtSpeeds[0], blueShirtSpeeds[0])
				removeItem(redShirtSpeeds, blueShirtSpeeds, 0,0)


	return speed

def removeItem(redShirtSpeeds, blueShirtSpeeds, idx1, idx2):

	del redShirtSpeeds[idx1]
	del blueShirtSpeeds[idx2]

print(tandemBicycle([3, 6, 7, 2, 1], [5, 5, 3, 9, 2], True))
print(tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], False))
