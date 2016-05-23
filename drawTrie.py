from suffixTrie import suffixTrie
from compressedSuffixTrie import compressedSuffixTrie
import pygame
from pygame.locals import *

def drawTrie(screen,node,x,y,interval,uncompressed):
    inc=40
    if node._label!=None or node._branches!={}:
        keys = [key for key in node._branches]
        if keys !=[] and node._branches[keys[0]]._label!=None:
            # x = x + inc*len(node._branches[keys[0]]._branches)
            ChildPos = drawTrie(screen, node._branches[keys[0]],x,y+inc,interval*0.7,uncompressed)
            pygame.draw.line(screen,(0,0,0),ChildPos,(x,y))
        if node._label==None:
            pass
        else: 
            if uncompressed:
                string = str(node._label[0])
            else:
                string=str(node._label)
            text=font.render(string,True,(0,0,0))
            screen.blit(text,(x,y))
        retval=(x,y)
        count=0
        for key in keys[1:]:
            if node._branches[key]._label!=None:
                count +=1
                ChildPos = drawTrie(screen, node._branches[key],\
                                    x+interval*count,y+inc,interval*0.7,uncompressed)
                pygame.draw.line(screen,(0,0,0),ChildPos,retval)
        return retval

def drawInsert(char):
    s = 'Input a string to insert: '+char
    text = font.render(s, True, (0,0,0))
    screen.blit(text,(10,10))

def find(string):
    trie=compressedSuffixTrie()
    trie.insert(string)
    result=findLongest(trie._root)
    return result

def findLongest(node):
    if node._label!=None:
        if node._label[-1]!='$':
            maxx=0
            string=''
            for i in node._branches.values():
                longest=findLongest(i)
                if len(longest)>maxx:
                    maxx=len(longest)
                    string=longest
            return node._label+string
        else:
            return ''
    else:
        maxx=0
        string=''
        for i in node._branches.values():
            longest=findLongest(i)
            if len(longest)>maxx:
                maxx=len(longest)
                string=longest
        return string
        # stringList=[]
        # for i in node._branches.values():
        #     stringList.append(findLongest(i))
        # return max(stringList)


def main(): 
    pygame.init()
    global width,height,dim
    (width,height) = (1500,700)
    dim = (width,height)
    global screen
    screen = pygame.display.set_mode(dim, 0, 32)
    screen.fill((255,255,255))
    pygame.display.set_caption('Trie')
    global font
    font = pygame.font.SysFont('Monospace', 15)
    
    screen.fill((255,255,255))
    running=True
    uncompressed=True
    char=''
    while running:
        screen.fill((255,255,255))
        if uncompressed:
            trie=suffixTrie()
        else:
            trie=compressedSuffixTrie()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                pygame.quit()
                exit()
            elif event.type==KEYDOWN:
                if event.key==K_TAB:
                    uncompressed=not uncompressed
                elif event.key==K_BACKSPACE:
                    char=char[:-1]
                else:
                    char+=chr(event.key)
        trie.insert(char)
        drawInsert(char)
        string=find(char)
        s1 = 'Longest Common Prefix:'+string
        text1 = font.render(s1, True, (0,0,0))
        screen.blit(text1,(10,20))        
        drawTrie(screen,trie._root,200,50,150,uncompressed)
        pygame.display.update()
    
main()
