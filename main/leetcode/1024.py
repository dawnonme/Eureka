class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()
        ans = 0
        cur_end = 0
        tmp = 0
        for start, end in clips:
            if start > tmp or tmp >= T:
                break
            elif start > cur_end:
                ans += 1
                cur_end = tmp
                if cur_end == T:
                    return ans
            tmp = max(tmp, end)
        return ans + 1 if tmp >= T else -1

    # O(nlogn) time
    def video_stitching(self, clips, T):
        # Sort clips by start time
        clips.sort(key=lambda x: x[0])
        t_video = 0  # Seconds of continious video we have so far
        cnt = 0
        i = 0
        while i < len(clips):
            t_end_next = -float(
                'inf')  # initialize end time of next overlapping clip
            # While next clip overlaps with the video we have so far,
            # keep updating t_end_next
            while i < len(clips) and t_video >= clips[i][0]:
                t_end_next = max(t_end_next, clips[i][1])
                i += 1
            # if no next clips overlap with the video-so-far, the task is impossible
            if t_end_next == -float('inf'):
                return -1
            else:
                # else update number of seconds of continious video we have so far, and
                # increment the count
                t_video = t_end_next
                cnt += 1
                if t_video >= T:
                    return cnt
        return -1