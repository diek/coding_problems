size = int(input())

room_numbers = list(map(int, input().split()))
captain_room = [room for room in room_numbers if room_numbers.count(room) == 1]
print(captain_room[0])
