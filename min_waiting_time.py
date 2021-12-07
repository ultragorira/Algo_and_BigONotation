def minimumWaitingTime(queries):
	queries.sort()
	total_wait = 0
	for id, item in enumerate(queries):
		queries_left = len(queries) - (id + 1)
		total_wait += item * queries_left
	return total_wait

print(minimumWaitingTime([3, 2, 1, 2, 6]))