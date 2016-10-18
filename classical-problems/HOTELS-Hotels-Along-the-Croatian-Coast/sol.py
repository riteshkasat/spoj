hotels, money = map(int, raw_input().strip().split())
costarray = map(int, raw_input().strip().split())
i=0;j=0; end = hotels

maxi = 0
current = 0
while(j<hotels):
	if current + costarray[j]<=money:
		current = current + costarray[j]
		maxi = max(maxi, current)
		j+=1

	else:
		current = current - costarray[i]
		i+=1
print maxi
