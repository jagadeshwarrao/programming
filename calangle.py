def calculateAngle(hh,mm):

	hAngle = double((hh%12+mm/60)*30)
	mAngle = double(mm*6)
	angle = double((mAngle-hAngle))
	angle = min(angle, 360 - angle)
	return angle
