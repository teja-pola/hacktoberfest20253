# LeetCode 126. Word Ladder II (find all shortest transformation sequences)
# BFS to build parent graph (level-by-level), then DFS/backtrack to build paths.
# Time: O(N * L^2) roughly where N is dict size and L is word length. Space: O(N * L)

from collections import defaultdict, deque

def findLadders(beginWord, endWord, wordList):
    word_set = set(wordList)
    if endWord not in word_set:
        return []

    # BFS variables
    level = {beginWord}
    parents = defaultdict(set)  # child -> set(parents)
    while level and endWord not in parents:
        next_level = defaultdict(set)
        for word in level:
            word_set.discard(word)
        for word in level:
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    if c == word[i]:
                        continue
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in word_set:
                        next_level[new_word].add(word)
        level = next_level.keys()
        for child, parents_set in next_level.items():
            parents[child].update(parents_set)

    # backtracking from endWord to beginWord using parents
    res = []
    def dfs(word, path):
        if word == beginWord:
            res.append(path[::-1])
            return
        for p in parents[word]:
            dfs(p, path + [p])

    if endWord in parents:
        dfs(endWord, [endWord])
    return res

# quick test
if __name__ == "__main__":
    begin = "hit"
    end = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(findLadders(begin, end, wordList))
    # expected: [
    #  ["hit","hot","dot","dog","cog"],
    #  ["hit","hot","lot","log","cog"]
    # ]
