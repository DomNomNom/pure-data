from lxml.html import parse
import re

commaInt = re.compile(r'[0-9,]+') # ['38,380'] from '\n38,380\nViewers\n'

doc = parse('http://www.twitch.tv/').getroot()
print 'parsed'

games = []

for link in doc.cssselect('.game.clearfix'):
    gameTitle = link.cssselect('.title')[0].text_content().strip()


    # print '%s: %s' % (link.text_content(), link.get('href'))
    viewersText = link.cssselect('.info')[0].text_content()
    viewers = int(commaInt.findall(viewersText)[0].replace(',', '')) # get 38380 from '\n38,380\nViewers\n'

    games.append((viewers, gameTitle))

    # print repr(viewersText)

for game in games:
    print game

print 'done'