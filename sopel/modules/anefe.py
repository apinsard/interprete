# -*- coding: utf-8 -*/
from sopel import module

@module.rule('.*en effet.*')
def anefe(bot, trigger):
  bot.say('anéfé')
