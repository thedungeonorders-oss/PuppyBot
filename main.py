"""
PuppyBot 🐾
===========
Owner & Puppy interaction bot with custom GIFs.

Environment variables:
  PUPPY_BOT_TOKEN      Discord bot token
  OWNER_DISCORD_ID     Owner's Discord user ID
  PUPPY_DISCORD_ID     Puppy's Discord user ID
  GITHUB_RAW_BASE      Raw GitHub URL to gifs folder
                       e.g. https://raw.githubusercontent.com/yourname/puppybot/main/gifs
"""

import discord
from discord import app_commands
import os

# ── Config ────────────────────────────────────────────────

TOKEN    = os.getenv('PUPPY_BOT_TOKEN')
OWNER_ID = int(os.getenv('OWNER_DISCORD_ID', '0'))
PUPPY_ID = int(os.getenv('PUPPY_DISCORD_ID', '0'))
BASE     = os.getenv('GITHUB_RAW_BASE', '').rstrip('/')

def gif(filename: str) -> str:
    return f'{BASE}/{filename}.gif' if BASE else ''

GIFS = {
    'Give_Puppy_Headpats':       gif('Give_Puppy_Headpats'),
    'Cuddles':                   gif('Cuddles'),
    'Kiss_Puppy_on_Forehead':    gif('Kiss_Puppy_on_Forehead'),
    'Lift_Puppy_Like_Simba':     gif('Lift_Puppy_Like_Simba'),
    'Give_Puppy_Treats':         gif('Give_Puppy_Treats'),
    'Cuddled_Sleep':             gif('Cuddled_Sleep'),
    'Rocks_Puppy':               gif('Rocks_Puppy'),
    'Order_Puppy_To_Fetch':      gif('Order_Puppy_To_Fetch'),
    'Order_Puppy_To_Roll':       gif('Order_Puppy_To_Roll'),
    'Order_Puppy_To_Send_Money': gif('Order_Puppy_To_Send_Money'),
    'Cage_Puppy':                gif('Cage_Puppy'),
    'Uncage_Puppy':              gif('Uncage_Puppy'),
    'Gag_Puppy':                 gif('Gag_Puppy'),
    'Puppy_Fetches':             gif('Puppy_Fetches'),
    'Puppy_Rolls':               gif('Puppy_Rolls'),
    'Puppy_Eats_Treats':         gif('Puppy_Eats_Treats'),
    'Puppy_Sends_Money':         gif('Puppy_Sends_Money'),
    'Good_Boy':                  gif('Good_Boy'),
    'Mommy_Mommy':               gif('Mommy_Mommy'),
}

PINK = 0xFFB6C1

# ── Bot setup ─────────────────────────────────────────────

intents = discord.Intents.default()
client  = discord.Client(intents=intents)
tree    = app_commands.CommandTree(client)

# ── Helpers ───────────────────────────────────────────────

def _mention(guild: discord.Guild, user_id: int) -> str:
    m = guild.get_member(user_id) if guild else None
    return m.mention if m else f'<@{user_id}>'

def owner(i: discord.Interaction) -> str:
    return _mention(i.guild, OWNER_ID)

def puppy(i: discord.Interaction) -> str:
    return _mention(i.guild, PUPPY_ID)

def make_embed(text: str, key: str) -> discord.Embed:
    e   = discord.Embed(description=text, color=PINK)
    url = GIFS.get(key, '')
    if url:
        e.set_image(url=url)
    return e

def clean_amount(amount: str) -> str:
    return amount.lstrip('$').strip()

async def owner_only(i: discord.Interaction) -> bool:
    if i.user.id != OWNER_ID:
        await i.response.send_message('🚫 Only Owner can use this!', ephemeral=True)
        return False
    return True

async def puppy_only(i: discord.Interaction) -> bool:
    if i.user.id != PUPPY_ID:
        await i.response.send_message('🚫 Only Puppy can use this!', ephemeral=True)
        return False
    return True

# ── OWNER — Reward ────────────────────────────────────────

@tree.command(name='owner-give-puppy-headpats', description='Give puppy gentle headpats 🐾')
async def cmd_headpat(i: discord.Interaction):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        f"Aww! Who's a good puppy? 👑 {owner(i)} gave {puppy(i)} gentle headpats 🐾✨",
        'Give_Puppy_Headpats'))

@tree.command(name='owner-cuddles', description='Cuddle puppy close 💕')
async def cmd_cuddles(i: discord.Interaction):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        f'💕 {owner(i)} cuddles {puppy(i)} close 🥰',
        'Cuddles'))

@tree.command(name='owner-kiss-puppy-on-forehead', description='Kiss puppy on the forehead 💋')
async def cmd_kiss(i: discord.Interaction):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        f'💋 {owner(i)} kissed {puppy(i)} softly on the forehead. Such a good baby puppy.',
        'Kiss_Puppy_on_Forehead'))

@tree.command(name='owner-lift-puppy-like-simba', description='Lift puppy up like Simba 🦁')
async def cmd_simba(i: discord.Interaction):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        f'🦁 {owner(i)} lifts {puppy(i)} up proudly like Simba ✨',
        'Lift_Puppy_Like_Simba'))

@tree.command(name='owner-give-puppy-treats', description='Give puppy a treat 🦴')
async def cmd_treat(i: discord.Interaction):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        f'🦴 {owner(i)} gives {puppy(i)} a treat! Good puppy!',
        'Give_Puppy_Treats'))

@tree.command(name='owner-cuddled-sleep', description='Cuddle up to sleep with puppy 💤')
async def cmd_sleep(i: discord.Interaction):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        f'💤 {owner(i)} and {puppy(i)} are cuddled up fast asleep 🌙',
        'Cuddled_Sleep'))

@tree.command(name='owner-rocks-puppy', description='Rock puppy to sleep 💤')
async def cmd_rocks(i: discord.Interaction):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        'Mommy Minnie rocks her baby puppy to sleep. Such a good baby.',
        'Rocks_Puppy'))


@tree.command(name='owner-good-boy', description='Tell puppy they are a good boy 🌟')
async def cmd_good_boy(i: discord.Interaction):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        f'🌟 {owner(i)} says: Good boy, {puppy(i)}! 🐾✨',
        'Good_Boy'))

# ── OWNER — Play ──────────────────────────────────────────

@tree.command(name='owner-order-puppy-to-fetch', description='Throw the ball for puppy 🎾')
async def cmd_fetch(i: discord.Interaction):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        f'🎾 {owner(i)} throws the ball. Go fetch, {puppy(i)}!',
        'Order_Puppy_To_Fetch'))

@tree.command(name='owner-order-puppy-to-roll', description='Tell puppy to roll over 🌀')
async def cmd_roll(i: discord.Interaction):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        f'🐾 {owner(i)} says: Roll over, {puppy(i)}!',
        'Order_Puppy_To_Roll'))

# ── OWNER — Findom ────────────────────────────────────────

@tree.command(name='owner-order-puppy-to-send-money', description='Make puppy send tribute 💸')
@app_commands.describe(amount='Amount in dollars e.g. 20')
async def cmd_send(i: discord.Interaction, amount: str):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        f'💸 {puppy(i)}, send {owner(i)} **${clean_amount(amount)}** now! 👑',
        'Order_Puppy_To_Send_Money'))

# ── OWNER — Femdom ────────────────────────────────────────

@tree.command(name='owner-cage-puppy', description='Cage the puppy 🔒')
async def cmd_cage(i: discord.Interaction):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        f'🔒 {owner(i)} has caged {puppy(i)}. Bad Puppy!',
        'Cage_Puppy'))

@tree.command(name='owner-uncage-puppy', description='Release puppy from the cage 🔓')
async def cmd_uncage(i: discord.Interaction):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        f'🔓 {owner(i)} has released {puppy(i)} from the cage 🐾',
        'Uncage_Puppy'))

@tree.command(name='owner-gag-puppy', description='Strap down puppy ⛓️')
async def cmd_gag(i: discord.Interaction):
    if not await owner_only(i): return
    await i.response.send_message(embed=make_embed(
        f'⛓️ {owner(i)} has strapped down {puppy(i)} 🔇 Shut up!',
        'Gag_Puppy'))

# ── PUPPY — Reward ────────────────────────────────────────

@tree.command(name='puppy-cuddles', description='Cuddle back against Owner 💕')
async def cmd_pcuddle(i: discord.Interaction):
    if not await puppy_only(i): return
    await i.response.send_message(embed=make_embed(
        f'🐾 {puppy(i)} cuddles up close to {owner(i)} 💕',
        'Cuddles'))


@tree.command(name='puppy-mommy-mommy', description='Puppy calls out for Mommy Minnie 🥺')
async def cmd_mommy(i: discord.Interaction):
    if not await puppy_only(i): return
    await i.response.send_message(embed=make_embed(
        f'🐾 {puppy(i)} says... Mommy Minnie! Mommy Minnie! 🥺',
        'Mommy_Mommy'))

# ── PUPPY — Play ──────────────────────────────────────────

@tree.command(name='puppy-fetches', description='Puppy fetches the ball 🎾')
async def cmd_pfetch(i: discord.Interaction):
    if not await puppy_only(i): return
    await i.response.send_message(embed=make_embed(
        f"🎾 {puppy(i)} fetches the ball and drops it at {owner(i)}'s feet! Such a good boy.",
        'Puppy_Fetches'))

@tree.command(name='puppy-rolls', description='Puppy rolls over 🌀')
async def cmd_proll(i: discord.Interaction):
    if not await puppy_only(i): return
    await i.response.send_message(embed=make_embed(
        f'🌀 {puppy(i)} rolls over! 🐾',
        'Puppy_Rolls'))

@tree.command(name='puppy-eats-treats', description='Puppy eats the treat 🦴')
async def cmd_peat(i: discord.Interaction):
    if not await puppy_only(i): return
    await i.response.send_message(embed=make_embed(
        f'🦴 {puppy(i)} happily munches on the treat 😋✨',
        'Puppy_Eats_Treats'))

@tree.command(name='puppy-cuddled-sleep', description='Puppy curls up to sleep next to Owner 💤')
async def cmd_psleep(i: discord.Interaction):
    if not await puppy_only(i): return
    await i.response.send_message(embed=make_embed(
        f'💤 {puppy(i)} curls up and falls asleep next to {owner(i)} 🌙',
        'Cuddled_Sleep'))

# ── PUPPY — Findom ────────────────────────────────────────

@tree.command(name='puppy-sends-money', description='Puppy tributes Owner 💸')
@app_commands.describe(amount='Amount in dollars e.g. 20')
async def cmd_psend(i: discord.Interaction, amount: str):
    if not await puppy_only(i): return
    await i.response.send_message(embed=make_embed(
        f'💸 {puppy(i)} tributes {owner(i)} **${clean_amount(amount)}** 👑✨',
        'Puppy_Sends_Money'))

# ── Guide ─────────────────────────────────────────────────

@tree.command(name='guide', description='Show available commands 📖')
async def cmd_guide(i: discord.Interaction):
    is_o = i.user.id == OWNER_ID
    is_p = i.user.id == PUPPY_ID

    if not is_o and not is_p:
        await i.response.send_message('🚫 This bot is private!', ephemeral=True)
        return

    if is_o:
        e = discord.Embed(title='👑 Owner Commands', color=PINK)
        e.add_field(name='🎀 Reward', value=(
            '`/owner-give-puppy-headpats` — Give puppy gentle headpats\n'
            '`/owner-cuddles` — Cuddle puppy close\n'
            '`/owner-kiss-puppy-on-forehead` — Kiss puppy on the forehead\n'
            '`/owner-lift-puppy-like-simba` — Lift puppy like Simba\n'
            '`/owner-give-puppy-treats` — Give puppy a treat\n'
            '`/owner-cuddled-sleep` — Cuddle up to sleep together\n'
            '`/owner-rocks-puppy` — Rock puppy to sleep\n'
            '`/owner-good-boy` — Tell puppy they are a good boy'
        ), inline=False)
        e.add_field(name='🎾 Play', value=(
            '`/owner-order-puppy-to-fetch` — Throw the ball for puppy\n'
            '`/owner-order-puppy-to-roll` — Tell puppy to roll over'
        ), inline=False)
        e.add_field(name='💸 Findom', value=(
            '`/order-puppy-to-send-money <amount>` — Make puppy send tribute'
        ), inline=False)
        e.add_field(name='⛓️ Femdom', value=(
            '`/owner-cage-puppy` — Cage the puppy\n'
            '`/owner-uncage-puppy` — Release puppy from the cage\n'
            '`/owner-gag-puppy` — Strap down puppy'
        ), inline=False)

    else:
        e = discord.Embed(title='🐾 Puppy Commands', color=PINK)
        e.add_field(name='🎀 Reward', value=(
            '`/puppy-cuddles` — Cuddle back against Owner\n'
            '`/puppy-mommy-mommy` — Call out for Mommy Minnie'
        ), inline=False)
        e.add_field(name='🎾 Play', value=(
            '`/puppy-fetches` — Fetch the ball for Owner\n'
            '`/puppy-rolls` — Roll over\n'
            '`/puppy-eats-treats` — Eat your treat\n'
            '`/puppy-cuddled-sleep` — Curl up to sleep next to Owner'
        ), inline=False)
        e.add_field(name='💸 Findom', value=(
            '`/puppy-sends-money <amount>` — Tribute Owner'
        ), inline=False)

    await i.response.send_message(embed=e, ephemeral=True)

# ── Startup ───────────────────────────────────────────────

@client.event
async def on_ready():
    await tree.sync()
    missing = [k for k, v in GIFS.items() if not v]
    print('=' * 50)
    print(f'✅ PuppyBot online! — {client.user}')
    print(f'👑 Owner ID  : {OWNER_ID}')
    print(f'🐾 Puppy ID  : {PUPPY_ID}')
    print(f'🖼️  GIFs      : {len(GIFS) - len(missing)}/{len(GIFS)} loaded')
    if missing:
        print(f'⚠️  Missing   : {", ".join(missing)}')
    print('=' * 50)

client.run(TOKEN)
