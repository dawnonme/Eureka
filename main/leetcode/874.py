class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        dire_move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dire, pos = 0, [0, 0]
        obs_set = set(tuple(ob) for ob in obstacles)
        res = 0
        for cmd in commands:
            if cmd == -2:
                dire = (dire - 1) % 4
            elif cmd == -1:
                dire = (dire + 1) % 4
            else:
                move = dire_move[dire]
                coor = 0 if dire % 2 == 1 else 1
                move = move[coor]
                for i in range(1, cmd + 1):
                    pos[coor] += 1 * move
                    if tuple(pos) in obs_set:
                        pos[coor] -= 1 * move
                        break
                res = max(res, pos[0] ** 2 + pos[1] ** 2)
        return res
