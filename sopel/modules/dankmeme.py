# -*- coding: utf-8 -*/
from sopel import module
from random import randint
import time

@module.rule('.*lenny.*')
def lenny(bot, trigger):
    bot.say('( ͡° ͜ʖ ͡°)')

@module.rule('.*shrug.*')
def shrug(bot, trigger):
    bot.say('¯\_(ツ)_/¯')

@module.rule('.*dealwithit.*')
def dealwithit(bot, trigger):
    bot.say('☞   ͜ʖ  ☞')

@module.rule('.*dwi.*')
def dwi(bot, trigger):
    bot.say('(⌐■_■)')

@module.rule('.*kawai.*')
def kawai(bot, trigger):
    bot.say('ʢ◉ᴥ◉ʡ')

#I like it when it comes up on overwtach and other things
@module.rule('.*wat.*')
def wat(bot, trigger):
    bot.say('( ͡°_ ͡°)')

@module.rule('.*waat.*')
def waat(bot, trigger):
    bot.say('staaap!')

@module.rule('.*gnéé.*')
def gne(bot, trigger):
    bot.say('ヽ(。_°)ノ')

@module.rule('.*ftt.*')
def ftt(bot, trigger):
    bot.say('(╯°□°）╯︵ ┻━┻')

@module.rule('.*RA+GE.*')
def rage(bot,trigger):
    bot.say(' ┻━┻︵ \(°□°)/ ︵ ┻━┻')

@module.rule('.*idkaidwtk.*')
def no(bot,trigger):
    bot.say(' I don\'t know and I don\'t want to know ╭∩╮')

@module.rule('.*doot.*')
def doot(bot,trigger):
    bot.say(' doot doot les rageux ╭∩╮（︶︿︶）╭∩╮ ')

@module.rule('.*poot.*')
def poot(bot,trigger):
    bot.say(' poot poot les rageux ┌∩┐(‿|‿)┌∩┐ ')

@module.rule('.*uwotm8.*')
def wtf(bot,trigger):
    bot.say('( ≖‿≖) ʷᵗᶠ ᵈᶦᵈ ʸᵒᵘ ˢᵃʸ ʸᵒᵘ ᶫᶦᵗᵗᶫᵉ ˢʰᶦᵗ')

@module.rule('\*coin\*')
def coin(bot,trigger):
    bot.say('( °)<')

@module.commands('fusion')
def fusion(bot, trigger):
    bot.say('(☞ﾟ∀ﾟ)☞    ☜(ﾟ∀ﾟ☜)')
    bot.say('☜(ﾟ∀ﾟ☜)  (☞ﾟ∀ﾟ)☞ ')
    bot.say('FU')
    bot.say('(☞ﾟ∀ﾟ)☞☜(ﾟ∀ﾟ☜)')
    bot.say('SION')
    time.sleep(2)
    bot.say('. . .')
    time.sleep(2)
    i = 0
    s = '☜('
    b = '☞ﾟ∀ﾟ☞ﾟ∀ﾟ☜'
    ''.join(random.sample(b, len(b)))
    bot.say(s + ')ᶰʸᵉᶫᶫᵒʷ')
