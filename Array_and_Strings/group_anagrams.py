def groupAnagrams(strs):
        anagrams = {}
        for word in strs:
            print(word)
            key = " ".join(sorted(word))
            # print(key)
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(word)
            print(anagrams)
        return list(anagrams.values())

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) # -> [["bat"],["nat","tan"],["ate","eat","tea"]]