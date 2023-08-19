import sys

meetingCount = int(sys.stdin.readline().rstrip())
meetingList = []

for _ in range(meetingCount):
    meetingInfo = sys.stdin.readline().rstrip().split()
    meetingList.append((int(meetingInfo[0]), int(meetingInfo[1])))

meetingList.sort(key=lambda x: (x[1], x[0]))
result = [meetingList[0]]
for i in range(1,   meetingCount):
    if meetingList[i][0] < result[-1][1]:  # 시작 시간이 종료 시간보다 빠르면 pass
        continue
    result.append(meetingList[i])

print(len(result))
