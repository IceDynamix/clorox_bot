from PIL import Image, ImageDraw, ImageFont
import requests
import io
import json
import numpy as np
import pyttanko as osu

########################################################
#                                                      #
#           Only for testing purposes                  #
#       no specific correlation between lines          #
#                                                      #
########################################################

# black = Image.new('RGBA', (900,500), color=(0, 0, 0, 0))
# with open('data.json') as file:
#     data = json.load(file)

# img = Image.new('RGBA', (900,1250), color=(0, 0, 0, 255))


# mod_list = ['NF', 'EZ', 'TD', 'HD', 'HR', 'SD', 'DT', '', 'HT', 'NC', 'FL', '', 'SO', '', 'PF']

# pt18_light = ImageFont.truetype('./LEMONMILK-Light.woff', 18)

# pt150_regular = ImageFont.truetype('./LEMONMILK-Regular.woff', 150)
# pt30_regular = ImageFont.truetype('./LEMONMILK-Regular.woff', 30)
# pt18_regular = ImageFont.truetype('./LEMONMILK-Regular.woff', 18)

# special = ImageFont.truetype('./DejaVuSans.ttf', 18)

# for i in range(5):
#     decal = 250*i

#     beatmap_cover = Image.open(requests.get('https://assets.ppy.sh/beatmaps/733559/covers/cover.jpg', stream=True).raw)
#     beatmap_cover = beatmap_cover.resize((900,250))
#     beatmap_cover = beatmap_cover.convert('RGBA')

#     img.paste(beatmap_cover, (-450,0+decal))

#     draw = ImageDraw.Draw(img)
#     draw.polygon(([200, 0+decal, 900, 0+decal, 900, 250+decal, 160, 250+decal]), fill=(47, 49, 54))
#     draw.line([(200, 0+decal), (160, 250+decal)], fill=(102, 104, 110), width=3)
#     draw.rectangle(((0,0+decal), (898,250+decal)), fill=None, outline=(64, 67, 73), width=2)

#     #--------------------   HEADER   --------------------#
#     draw.text((220,10+decal), 'chikatto chika chika', fill=(255, 255, 255), font=pt30_regular)
#     draw.text((220,42+decal), '[reform\'s expert]', fill=(142, 142, 142), font=pt18_light)

#     #-------------------- LEFT INFO --------------------#
#     draw.rectangle([(220,80+decal),(272,103+decal)], fill=(57, 111, 244))
#     draw.text((248,85+decal), '300', fill=(47, 49, 54), font=pt18_regular, anchor='mt')
#     draw.text((283,85+decal), '69', fill=(255, 255, 255), font=pt18_light, anchor='lt')

#     draw.rectangle([(220,108+decal),(272,131+decal)], fill=(72, 248, 80))
#     draw.text((248,113+decal), '100', fill=(47, 49, 54), font=pt18_regular, anchor='mt')
#     draw.text((283,113+decal), '11', fill=(255, 255, 255), font=pt18_light, anchor='lt')

#     draw.rectangle([(220,136+decal),(272,159+decal)], fill=(245, 225, 90))
#     draw.text((248,141+decal), '50', fill=(47, 49, 54), font=pt18_regular, anchor='mt')
#     draw.text((283,141+decal), '0', fill=(255, 255, 255), font=pt18_light, anchor='lt')

#     draw.rectangle([(220,164+decal),(272,187+decal)], fill=(242, 56, 56))
#     draw.text((248,168+decal), 'miss', fill=(47, 49, 54), font=pt18_regular, anchor='mt')
#     draw.text((283,168+decal), '11', fill=(255, 255, 255), font=pt18_light, anchor='lt')

#     #-------------------- LEFT INFO --------------------#
#     draw.text((490,85+decal), 'difficulty:', fill=(255, 255, 255), font=pt18_light, anchor='rt')
#     draw.text((500,85+decal), '7.63', fill=(142, 142, 142), font=pt18_light, anchor='lt')
#     draw.text((550,85+decal), '★', fill=(142, 142, 142), font=special, anchor='lt')

#     draw.text((490,113+decal), 'combo:', fill=(255, 255, 255), font=pt18_light, anchor='rt')
#     draw.text((510,113+decal), '412/413', fill=(142, 142, 142), font=pt18_light, anchor='lt')
#     draw.text((400,118+decal), 'x', fill=(142, 142, 142), font=special, anchor='lt')

#     draw.text((490,141+decal), 'pp:', fill=(255, 255, 255), font=pt18_light, anchor='rt')
#     draw.text((500,141+decal), '427.16', fill=(142, 142, 142), font=pt18_light, anchor='lt')

#     draw.text((490,168+decal), 'accuracy:', fill=(255, 255, 255), font=pt18_light, anchor='rt')
#     draw.text((500,168+decal), '79.85%', fill=(142, 142, 142), font=pt18_light, anchor='lt')

#     #--------------------   RANK   --------------------#
#     draw.text((775,125+decal), 'S', fill=(170, 183, 204), font=pt150_regular, anchor='mm')

#     #--------------------   MODS   --------------------#
#     mod_code = 72
#     mod_code = list(bin(mod_code)[2:]) 
#     mod_code.reverse()

#     if len(mod_code)== 1 and mod_code[0] == '0': 
#         mods = [Image.fromarray(np.array(data['NM'], dtype=np.uint8))]
#     else: 
#         mods = [Image.fromarray(np.array(data[mod_list[x]], dtype=np.uint8)) for x in range(len(mod_code)) if mod_code[x] == '1']

#     if ('SD' in mods) and ('PF' in mods): mods.remove('SD')
#     if ('DT' in mods) and ('NC' in mods): mods.remove('DT')

#     mod_bg = Image.new('RGBA', (len(mods)*49,36), color=(47, 49, 54, 255))
#     a = Image.new('RGBA', (len(mods)*49,36), color=(47, 49, 54, 255))

#     [a.paste(mods[x].resize((49,36)), (49*x,0)) for x in range(len(mods))]

#     a = Image.alpha_composite(mod_bg, a)

#     img.paste(a, (220, 200+decal))

# img.show()

# black_draw = ImageDraw.Draw(black)
# black_draw.rectangle(((0,0), (900,500)), fill=(0, 0, 0, 127))

# img.paste(beatmap_cover, (0,0))
# img = Image.alpha_composite(img, black)


# # img.paste(flag, (16,14))

# #--------------------   HEADER   --------------------#
# draw.text((28,18), 'debug dance', fill=(255, 255, 255), font=pt35_light)
# draw.text((30,55), 'lapix', fill=(255, 255, 255), font=pt20_light)
# draw.text((875,28), '[whaaat]', fill=(255, 255, 255), font=pt30_light, anchor='rt')
# draw.text((850,70), '7.30', fill=(255, 255, 255), font=pt25_light, anchor='rt')
# draw.text((875,70), '★', fill=(255, 255, 255), font=special, anchor='rt')
# draw.text((840,112), '3.54', fill=(255, 255, 255), font=pt25_light, anchor='rt')
# draw.text((875,112), 'pp', fill=(255, 255, 255), font=pt25_light, anchor='rt')

# #--------------------   SCORES LEFT   --------------------#
# draw.text((28,150), '1 1 1 3 5 4 6 9', fill=(255, 255, 255), font=pt50_regular)

# draw.rectangle([(30,220),(135,260)], fill=(57, 111, 244))
# draw.text((85,227), '300', fill=(47, 49, 54), font=pt35_regular, anchor='mt')
# draw.text((155,227), '69', fill=(255, 255, 255), font=pt35_light, anchor='lt')

# draw.rectangle([(30,268),(135,308)], fill=(72, 248, 80))
# draw.text((85,275), '100', fill=(47, 49, 54), font=pt35_regular, anchor='mt')
# draw.text((155,275), '11', fill=(255, 255, 255), font=pt35_light, anchor='lt')

# draw.rectangle([(30,316),(135,356)], fill=(245, 225, 90))
# draw.text((85,323), '50', fill=(47, 49, 54), font=pt35_regular, anchor='mt')
# draw.text((155,323), '0', fill=(255, 255, 255), font=pt35_light, anchor='lt')

# draw.rectangle([(30,364),(135,404)], fill=(242, 56, 56))
# draw.text((85,371), 'miss', fill=(47, 49, 54), font=pt35_regular, anchor='mt')
# draw.text((155,371), '11', fill=(255, 255, 255), font=pt35_light, anchor='lt')

# #--------------------   SCORES RIGHT   --------------------#
# draw.text((500,227), 'accuracy:', fill=(255, 255, 255), font=pt35_light, anchor='rt')
# draw.text((510,227), '79.85%', fill=(142, 142, 142), font=pt35_light, anchor='lt')

# draw.text((500,295), 'combo:', fill=(255, 255, 255), font=pt35_light, anchor='rt')
# draw.text((520,295), '1138/1138', fill=(142, 142, 142), font=pt35_light, anchor='lt')
# draw.text((505,310), 'x', fill=(142, 142, 142), font=special, anchor='lt')

# draw.text((800,250), 'f', fill=(242, 56, 56), font=pt200_regular, anchor='mt')

# draw.text((450,450), 'completion: 11.43%', fill=(255, 255, 255), font=pt35_light, anchor='mt')

# mod_code = int(resp.json()[0]['enabled_mods'])
# mod_code = list(bin(mod_code)[2:]) 
# mod_code.reverse()

# if len(mod_code)== 1 and mod_code[0] == '0': 
#     mods = [Image.fromarray(np.array(data['NM'], dtype=np.uint8))]
# else: 
#     mods = [Image.fromarray(np.array(data[mod_list[x]], dtype=np.uint8)) for x in range(len(mod_code)) if mod_code[x] == '1']

# if ('SD' in mods) and ('PF' in mods): mods.remove('SD')
# if ('DT' in mods) and ('NC' in mods): mods.remove('DT')

# mod_bg = Image.new('RGBA', (len(mods)*71,50), color=(47, 49, 54, 255))
# a = Image.new('RGBA', (len(mods)*71,50), color=(47, 49, 54, 255))

# [a.paste(mods[x].resize((71,50)), (71*x,0)) for x in range(len(mods))]

# a = Image.alpha_composite(mod_bg, a)

# if len(mods) == 7:
#     img.paste(a, (218, 355))
# else:
#     img.paste(a, (290, 355))

# img = Image.new('RGB', (400,200), color=(47, 49, 54))
# avatar = Image.open(requests.get(f'http://s.ppy.sh/a/{response.json()[0]["user_id"]}', stream=True).raw)
# flag = Image.open(requests.get(f'https://osu.ppy.sh/images/flags/{response.json()[0]["country"]}.png', stream=True).raw)
# title_font = ImageFont.truetype('./LEMONMILK-Regular.woff', 13)
# default_font = ImageFont.truetype('./LEMONMILK-Light.woff', 13)
# rank_font = ImageFont.truetype('./LEMONMILK-Regular.woff', 31)

# avatar = avatar.resize((200,200))
# flag = flag.resize((21,15))

# img.paste(avatar, (200,0))

# draw = ImageDraw.Draw(img)
# draw.polygon([0, 0, 240, 0, 310, 200, 0, 200], fill=(47, 49, 54))

# img.paste(flag, (16,14))

# draw.text((42,12), f'{response.json()[0]["username"]} profile', fill=(255, 255, 255), font=title_font)

# draw.text((16,44), 'rank:', fill=(255, 255, 255), font=default_font)
# draw.text((65,44), f'#{response.json()[0]["pp_rank"]} ({response.json()[0]["country"]}#{response.json()[0]["pp_country_rank"]})', fill=(240, 90, 90), font=default_font)

# draw.text((16,64), 'level:', fill=(255, 255, 255), font=default_font)
# level = response.json()[0]["level"]
# draw.text((69,64), f'{int(float(level))} ({round((float(level)- int(float(level)))*100, 2)}%)', fill=(240, 90, 90), font=default_font)

# draw.text((16,84), 'net pp:', fill=(255, 255, 255), font=default_font)
# draw.text((75,84), f'{response.json()[0]["pp_raw"]}', fill=(240, 90, 90), font=default_font)

# draw.text((16,104), 'hit accuracy:', fill=(255, 255, 255), font=default_font)
# draw.text((129,104), f'{round(float(response.json()[0]["accuracy"]), 2)}%', fill=(240, 90, 90), font=default_font)

# draw.text((16,124), 'playcount:', fill=(255, 255, 255), font=default_font)
# draw.text((112,124), f'{response.json()[0]["playcount"]}', fill=(240, 90, 90), font=default_font)

# draw.text((40,148), 'SS', fill=(162, 162, 162), font=rank_font, anchor='mt')
# draw.text((120,148), 'S', fill=(245, 225, 90), font=rank_font, anchor='mt')
# draw.text((200,148), 'A', fill=(76, 208, 54), font=rank_font, anchor='mt')

# draw.text((40,178), f'{int(response.json()[0]["count_rank_ss"]) + int(response.json()[0]["count_rank_ssh"])}', fill=(255, 255, 255), font=default_font, anchor='mt')
# draw.text((120,178), f'{int(response.json()[0]["count_rank_s"]) + int(response.json()[0]["count_rank_sh"])}', fill=(255, 255, 255), font=default_font, anchor='mt')
# draw.text((200,178), f'{int(response.json()[0]["count_rank_a"])}', fill=(255, 255, 255), font=default_font, anchor='mt')


# img.show()

# nomod = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_no-mod.d04b9d35.png', stream=True).raw).convert('RGBA'))

# halftime = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_half.3e707fd4.png', stream=True).raw).convert('RGBA'))
# easy = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_easy.076c7e8c.png', stream=True).raw).convert('RGBA'))
# nofail = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_no-fail.ca1a6374.png', stream=True).raw).convert('RGBA'))

# doubletime = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_double-time.348a64d3.png', stream=True).raw).convert('RGBA'))
# nightcore = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_nightcore.240c22f2.png', stream=True).raw).convert('RGBA'))
# hardrock = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_hard-rock.52c35a3a.png', stream=True).raw).convert('RGBA'))
# hidden = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_hidden.cfc32448.png', stream=True).raw).convert('RGBA'))
# suddendeath = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_sudden-death.d0df65c7.png', stream=True).raw).convert('RGBA'))
# perfect = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_perfect.460b6e49.png', stream=True).raw).convert('RGBA'))
# flashlight = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_flashlight.be8ff220.png', stream=True).raw).convert('RGBA'))
# fadein = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_fader.b863efe4.png', stream=True).raw).convert('RGBA'))

# spunout = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_spun-out.989be71e.png', stream=True).raw).convert('RGBA'))
# touchdevice = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_touchdevice.e5fa4271.png', stream=True).raw).convert('RGBA'))
# mirror = np.array(Image.open(requests.get('https://osu.ppy.sh/assets/images/mod_mirror.f733b7e1.png', stream=True).raw).convert('RGBA'))

# mod_dict = {
#     'NM': nomod.tolist(), 
#     'HT': halftime.tolist(),
#     'EZ': easy.tolist(), 
#     'NF': nofail.tolist(),
#     'HR': hardrock.tolist(),
#     'DT': doubletime.tolist(),
#     'NC': nightcore.tolist(),
#     'HD': hidden.tolist(),
#     'SD': suddendeath.tolist(), 
#     'PF': perfect.tolist(), 
#     'FL': flashlight.tolist(),
#     'FI': fadein.tolist(),
#     'SO': spunout.tolist(),
#     'TD': touchdevice.tolist(),
#     'MR': mirror.tolist(),
# }

# with open('data.json', 'w') as file:
#     mod_dict = json.dumps(mod_dict)
#     file.write(mod_dict)