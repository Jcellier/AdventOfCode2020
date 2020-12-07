import sys, pprint, math

# input file as cmdline arg
with open("day5.txt", 'r') as f:
    seats = f.read().strip().split('\n')

def bsearch(ticket, i, lower, upper):
    if ticket[i] in ['F', 'L']:
        upper -= math.ceil((upper-lower)/2)
    else:
        lower += math.ceil((upper-lower)/2)
    if upper == lower:
        return upper
    return bsearch(ticket, i+1, lower, upper)

taken_seats = sorted([(x * 8) + y for x,y in [(bsearch(seat[0:7], 0, 0, 127), bsearch(seat[7:10], 0, 0, 7)) for seat in seats]])

print('Max:', max(taken_seats))
for i in range(len(taken_seats)):
    if taken_seats[i]+1 != taken_seats[i+1]:
        print('Missing:', taken_seats[i] + 1)
        break