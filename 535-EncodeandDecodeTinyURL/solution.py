import random

class Codec:
    data = {}
    reverse_data = {}

    def randomStr(self):
        result = ''
        for x in range(8):
            cap = random.randint(0, 1)
            tmp = random.randint(0, 25)
            if cap:
                tmp = chr(tmp + 65)
            else:
                tmp = chr(tmp + 97)
            result = result + tmp
        return result

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.reverse_data:
            return self.reverse_data[longUrl]
        else:
            tmp = "http://tinyurl.com/" + self.randomStr()
            self.data[tmp] = longUrl
            self.reverse_data[longUrl] = tmp
            return tmp

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if shortUrl in self.data:
            return self.data[shortUrl]
        return shortUrl
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
a = Codec()
print a.randomStr()