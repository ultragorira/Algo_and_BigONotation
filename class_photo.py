#O(nlog N) because we sort and then loop through, Time O(1) Space

def classPhotos(redShirtHeights, blueShirtHeights):
	
	redShirtHeights.sort(reverse=True)
	blueShirtHeights.sort(reverse=True)
		
	shirt_back_row = "BLUE" if blueShirtHeights[0] > redShirtHeights[0] else "RED"
	
	for idx in range(len(blueShirtHeights)):
		blue_shirt = blueShirtHeights[idx]
		red_shirt = redShirtHeights[idx]
		
		if shirt_back_row == "BLUE":
			if blue_shirt <= red_shirt:
				return False
			
		else:
			if red_shirt <= blue_shirt:
				return False
	
	return True



classPhotos([2, 4, 7, 5, 1],[3, 5, 6, 8, 2])