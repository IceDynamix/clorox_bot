from PIL import Image, ImageDraw, ImageFont
import json
import numpy as np
import pyttanko as osu
import osu_api

image_data = 'mod_image_data.json'

mod_list = ['NF', 'EZ', 'TD', 'HD', 'HR', 'SD', 'DT', '', 'HT', 'NC', 'FL', '',
            'SO', '', 'PF', '', '', '', '', '', 'FI', '', '', '', '', '', '', '', '', '', 'MR']

rank_colors = {
    'F': (242, 56, 56),
    'D': (242, 56, 56),
    'C': (119, 57, 189),
    'B': (57, 111, 244),
    'A': (72, 248, 80),
    'S': (245, 225, 90),
    'X': (255, 223, 6),
    'SH': (170, 183, 204),
    'XH': (170, 183, 204)
}

lemon_milk_light = './fonts/LEMONMILK-Light.woff'
lemon_milk_regular = './fonts/LEMONMILK-Regular.woff'
special_characters_font = './fonts/DejaVuSans.ttf'


pt35_light = ImageFont.truetype(lemon_milk_light, 35)
pt30_light = ImageFont.truetype(lemon_milk_light, 30)
pt25_light = ImageFont.truetype(lemon_milk_light, 25)
pt20_light = ImageFont.truetype(lemon_milk_light, 20)
pt18_light = ImageFont.truetype(lemon_milk_light, 18)

pt200_regular = ImageFont.truetype(lemon_milk_regular, 200)
pt150_regular = ImageFont.truetype(lemon_milk_regular, 150)
pt50_regular = ImageFont.truetype(lemon_milk_regular, 50)
pt35_regular = ImageFont.truetype(lemon_milk_regular, 35)
pt30_regular = ImageFont.truetype(lemon_milk_regular, 30)
pt18_regular = ImageFont.truetype(lemon_milk_regular, 18)

pt25_special = ImageFont.truetype(special_characters_font, 25)
pt18_special = ImageFont.truetype(special_characters_font, 18)

with open(image_data) as file:
    mods_image_data = json.load(file)


def display_play(beatmap_data: object,
                 play_data: object,
                 cover_image: Image = Image.new('RGBA', (900, 500), color=(0, 0, 0, 0))):

    img = Image.new('RGBA', (900, 500), color=(0, 0, 0, 255))
    black = Image.new('RGBA', (900, 500), color=(0, 0, 0, 0))

    total_count = int(beatmap_data["count_normal"]) + \
        int(beatmap_data["count_slider"]) + \
        int(beatmap_data["count_spinner"])

    accuracy = int(play_data["count300"]) + \
        int(play_data["count100"])*(1/3) + \
        int(play_data["count50"])*(1/6)

    count_sum = int(play_data["count300"]) + \
        int(play_data["count100"]) + \
        int(play_data["count50"]) + \
        int(play_data["countmiss"])

    accuracy /= count_sum

    completion = count_sum/total_count

    cover_image = cover_image.resize((900, 250))
    cover_image = cover_image.convert('RGBA')

    black_draw = ImageDraw.Draw(black)
    black_draw.rectangle(((0, 0), (900, 500)), fill=(0, 0, 0, 127))

    img.paste(cover_image, (0, 0))
    img = Image.alpha_composite(img, black)

    draw = ImageDraw.Draw(img)
    draw.polygon(([0, 100, 900, 200, 900, 500, 0, 500]), fill=(47, 49, 54))
    draw.line([(0, 100), (900, 200)], fill=(102, 104, 110), width=6)

    # --------------------   HEADER   --------------------#
    if len(beatmap_data["version"]) >= 15:
        version = beatmap_data["version"][:15] + '...'
    else:
        version = beatmap_data["version"]

    if len(beatmap_data["title"]) >= 22:
        title = beatmap_data["title"][:22] + '...'
    else:
        title = beatmap_data["title"]

    draw.text((28, 18), f'{title}', fill=(255, 255, 255), font=pt35_light)
    draw.text((30, 55), f'{beatmap_data["creator"]}', fill=(
        255, 255, 255), font=pt20_light)
    draw.text((875, 28), f'[{version}]', fill=(
        255, 255, 255), font=pt30_light, anchor='rt')
    draw.text((875, 70), '★', fill=(255, 255, 255),
              font=pt25_special, anchor='rt')

    # --------------------   SCORES LEFT   --------------------#
    draw.text((28, 150), f'{" ".join(play_data["score"])}', fill=(
        255, 255, 255), font=pt50_regular)

    draw.rectangle([(30, 220), (135, 260)], fill=(57, 111, 244))
    draw.text((85, 227), '300', fill=(47, 49, 54),
              font=pt35_regular, anchor='mt')
    draw.text((155, 227), f'{play_data["count300"]}', fill=(
        255, 255, 255), font=pt35_light, anchor='lt')

    draw.rectangle([(30, 268), (135, 308)], fill=(72, 248, 80))
    draw.text((85, 275), '100', fill=(47, 49, 54),
              font=pt35_regular, anchor='mt')
    draw.text((155, 275), f'{play_data["count100"]}', fill=(
        255, 255, 255), font=pt35_light, anchor='lt')

    draw.rectangle([(30, 316), (135, 356)], fill=(245, 225, 90))
    draw.text((85, 323), '50', fill=(47, 49, 54),
              font=pt35_regular, anchor='mt')
    draw.text((155, 323), f'{play_data["count50"]}', fill=(
        255, 255, 255), font=pt35_light, anchor='lt')

    draw.rectangle([(30, 364), (135, 404)], fill=(242, 56, 56))
    draw.text((85, 371), 'miss', fill=(47, 49, 54),
              font=pt35_regular, anchor='mt')
    draw.text((155, 371), f'{play_data["countmiss"]}', fill=(
        255, 255, 255), font=pt35_light, anchor='lt')

    # --------------------   SCORES RIGHT   --------------------#
    draw.text((500, 227), 'accuracy:', fill=(
        255, 255, 255), font=pt35_light, anchor='rt')
    draw.text((510, 227), f'{accuracy:.2%}',
              fill=(142, 142, 142), font=pt35_light, anchor='lt')

    draw.text((500, 275), 'combo:', fill=(
        255, 255, 255), font=pt35_light, anchor='rt')
    draw.text((520, 275), f'{play_data["maxcombo"]}/{beatmap_data["max_combo"]}', fill=(
        142, 142, 142), font=pt35_light, anchor='lt')
    draw.text((505, 290), 'x', fill=(142, 142, 142),
              font=pt25_special, anchor='lt')

    # silver grades
    if 'H' in play_data["rank"]:
        rank = play_data["rank"][:-1]
    else:
        rank = play_data["rank"]

    if 'X' in play_data["rank"]:
        rank = 'SS'

    draw.text(
        (800, 250), f'{rank}', fill=rank_colors[play_data["rank"]], font=pt200_regular, anchor='mt')

    # play was failed/quit
    if count_sum != total_count:
        draw.text((30, 458), '.', fill=(255, 255, 255),
                  font=pt50_regular, anchor='lt')
        draw.text((50, 450), f'completion: {round(completion*100, 2)}%',
                  fill=(142, 142, 142), font=pt25_light, anchor='lt')

    draw.text((870, 458), f'{play_data["date"]}', fill=(
        142, 142, 142), font=pt25_light, anchor='rt')

    mods = get_mods_from_play(play_data)

    draw.text((850, 70), f'{round(float(beatmap_data["difficultyrating"]),2)}', fill=(
        255, 255, 255), font=pt25_light, anchor='rt')

    if "pp" in play_data:
        pp = play_data["pp"]
    else:
        pp = calculate_pp(beatmap_data, play_data, completion) or "NaN"

    fc_pp = calculate_fc_pp(beatmap_data, play_data) or "NaN"

    draw.text((500, 323), 'pp:', fill=(255, 255, 255),
              font=pt35_light, anchor='rt')
    draw.text((510, 323), f'{pp:.2f}', fill=(
        142, 142, 142), font=pt35_light, anchor='lt')

    draw.text((875, 112), 'pp', fill=(255, 255, 255),
              font=pt25_light, anchor='rt')
    draw.text((840, 112), f'{fc_pp:.2f}', fill=(
        255, 255, 255), font=pt25_light, anchor='rt')

    # mods are pasted with a blackground if this isnt done
    mod_bg = Image.new('RGBA', (len(mods)*71, 50), color=(47, 49, 54, 255))
    mod_composite = Image.new(
        'RGBA', (len(mods)*71, 50), color=(47, 49, 54, 255))

    mod_images = get_mod_images_from_mods(mods)

    for mod in range(len(mods)):
        mod_composite.paste(mod_images[mod].resize((71, 50)), (71*mod, 0))

    mod_composite = Image.alpha_composite(mod_bg, mod_composite)

    if len(mods) == 7:
        img.paste(mod_composite, (218, 355))
    else:
        img.paste(mod_composite, (290, 355))

    return img


def display_plays(beatmap_data_list,
                  play_data_list,
                  cover_image_list):

    repetitions = len(beatmap_data_list)
    if len(play_data_list) != repetitions or \
            len(cover_image_list) != repetitions:
        return None

    img = Image.new('RGBA', (900, 250*repetitions), color=(0, 0, 0, 255))

    for i in range(repetitions):
        offset = 250*i

        beatmap_data = beatmap_data_list[i]
        play_data = play_data_list[i]

        beatmap_cover = cover_image_list[i].resize(
            (900, 250)).convert('RGBA')

        img.paste(beatmap_cover, (0, offset))

        draw = ImageDraw.Draw(img)
        draw.polygon(([200, offset, 900, offset, 900, 250 +
                       offset, 160, 250+offset]), fill=(47, 49, 54))
        draw.line([(200, offset), (160, 250+offset)],
                  fill=(102, 104, 110), width=3)
        draw.rectangle(((0, offset), (898, 250+offset)),
                       fill=None, outline=(64, 67, 73), width=2)

        #--------------------   HEADER   --------------------#
        draw.text((220, 10+offset),
                  f'{beatmap_data["title"]}', fill=(255, 255, 255), font=pt30_regular)
        draw.text((220, 42+offset), f'[{beatmap_data["version"]}]',
                  fill=(142, 142, 142), font=pt18_light)

        #-------------------- LEFT INFO --------------------#
        draw.rectangle([(220, 80+offset), (272, 103+offset)],
                       fill=(57, 111, 244))
        draw.text((248, 85+offset), '300', fill=(47, 49, 54),
                  font=pt18_regular, anchor='mt')
        draw.text((283, 85+offset), f'{play_data["count300"]}', fill=(
            255, 255, 255), font=pt18_light, anchor='lt')

        draw.rectangle([(220, 108+offset), (272, 131+offset)],
                       fill=(72, 248, 80))
        draw.text((248, 113+offset), '100', fill=(47, 49, 54),
                  font=pt18_regular, anchor='mt')
        draw.text((283, 113+offset), f'{play_data["count100"]}', fill=(
            255, 255, 255), font=pt18_light, anchor='lt')

        draw.rectangle([(220, 136+offset), (272, 159+offset)],
                       fill=(245, 225, 90))
        draw.text((248, 141+offset), '50', fill=(47, 49, 54),
                  font=pt18_regular, anchor='mt')
        draw.text((283, 141+offset), f'{play_data["count50"]}', fill=(
            255, 255, 255), font=pt18_light, anchor='lt')

        draw.rectangle([(220, 164+offset), (272, 187+offset)],
                       fill=(242, 56, 56))
        draw.text((248, 168+offset), 'miss', fill=(47, 49, 54),
                  font=pt18_regular, anchor='mt')
        draw.text((283, 168+offset), f'{play_data["countmiss"]}', fill=(
            255, 255, 255), font=pt18_light, anchor='lt')

        #-------------------- LEFT INFO --------------------#

        total_count = int(beatmap_data["count_normal"]) + \
            int(beatmap_data["count_slider"]) + \
            int(beatmap_data["count_spinner"])

        accuracy = int(play_data["count300"]) + \
            int(play_data["count100"])*(1/3) + \
            int(play_data["count50"])*(1/6)

        count_sum = int(play_data["count300"]) + \
            int(play_data["count100"]) + \
            int(play_data["count50"]) + \
            int(play_data["countmiss"])

        accuracy /= count_sum

        completion = count_sum/total_count

        draw.text((490, 85+offset), 'difficulty:',
                  fill=(255, 255, 255), font=pt18_light, anchor='rt')
        draw.text((550, 85+offset), '★', fill=(142, 142, 142),
                  font=pt18_special, anchor='lt')

        draw.text((490, 113+offset), 'combo:', fill=(255, 255, 255),
                  font=pt18_light, anchor='rt')
        draw.text((510, 113+offset), f'{play_data["maxcombo"]}/{beatmap_data["max_combo"]}', fill=(
            142, 142, 142), font=pt18_light, anchor='lt')
        draw.text((500, 118+offset), 'x', fill=(142, 142, 142),
                  font=pt18_special, anchor='lt')

        if "pp" in play_data:
            pp = play_data["pp"]
        else:
            pp = calculate_pp(beatmap_data, play_data, completion) or "NaN"

        draw.text((490, 141+offset), 'pp:', fill=(255, 255, 255),
                  font=pt18_light, anchor='rt')
        draw.text((500, 141+offset), f'{pp}', fill=(
            142, 142, 142), font=pt18_light, anchor='lt')

        draw.text((490, 168+offset), 'accuracy:',
                  fill=(255, 255, 255), font=pt18_light, anchor='rt')
        draw.text((500, 168+offset), f'{(accuracy/count_sum*100):.2f}%',
                  fill=(142, 142, 142), font=pt18_light, anchor='lt')

        #--------------------   RANK   --------------------#
        if 'H' in play_data["rank"]:
            rank = play_data["rank"][:-1]
        else:
            rank = play_data["rank"]

        if 'X' in play_data["rank"]:
            rank = 'SS'

        draw.text((775, 125+offset),
                  f'{rank}', fill=rank_colors[play_data["rank"]], font=pt150_regular, anchor='mm')

        # --------------------   MODS   --------------------#

        mods = get_mods_from_play(play_data)
        mod_images = get_mod_images_from_mods(mods)

        # if any(item in ['EZ', 'HR', 'DT', 'NC', 'HT'] for item in mod_request):
        #     mod_request = sum([mod_values[x] for x in mod_request if x in [
        #                       'EZ', 'HR', 'DT', 'NC', 'HT']])
        #     try:
        #         beatmap_info = requests.get(
        #             f'{api_link}get_beatmaps?k={api_key}&b={beatmap_id}&mods={mod_request}&m={mode}')
        #         beatmap_data
        #     except IndexError:
        #         beatmap_info = requests.get(
        #             f'{api_link}get_beatmaps?k={api_key}&b={beatmap_id}&mods={mod_request}&m={mode}&a=1')

        draw.text((500, 85+offset), f'{float(beatmap_data["difficultyrating"]):.2f}', fill=(
            142, 142, 142), font=pt18_light, anchor='lt')

        mod_bg = Image.new('RGBA', (len(mods)*49, 36), color=(47, 49, 54, 255))
        mod_composite = Image.new(
            'RGBA', (len(mods)*49, 36), color=(47, 49, 54, 255))

        for mod in range(len(mods)):
            mod_composite.paste(mod_images[mod].resize((49, 36)), (49*mod, 0))

        mod_composite = Image.alpha_composite(mod_bg, mod_composite)

        img.paste(mod_composite, (220, 200+offset))

    return img


def display_profile(response):
    img = Image.new('RGB', (400, 200), color=(47, 49, 54))
    avatar = Image.open(requests.get(
        f'http://s.ppy.sh/a/{response.json()[0]["user_id"]}', stream=True).raw)
    flag = Image.open(requests.get(
        f'https://osu.ppy.sh/images/flags/{response.json()[0]["country"]}.png', stream=True).raw)
    title_font = ImageFont.truetype(lemon_milk_regular, 13)
    default_font = ImageFont.truetype(lemon_milk_light, 13)
    rank_font = ImageFont.truetype(lemon_milk_regular, 31)

    avatar = avatar.resize((200, 200))
    flag = flag.resize((21, 15))

    img.paste(avatar, (200, 0))

    draw = ImageDraw.Draw(img)
    draw.polygon([0, 0, 240, 0, 310, 200, 0, 200], fill=(47, 49, 54))
    draw.line([(240, 0), (310, 200)], fill=(102, 104, 110), width=3)

    img.paste(flag, (16, 14))

    draw.text((42, 12), f'{response.json()[0]["username"]} profile', fill=(
        255, 255, 255), font=title_font)

    draw.text((16, 44), 'rank:', fill=(255, 255, 255), font=default_font)
    draw.text((65, 44), f'#{response.json()[0]["pp_rank"]} ({response.json()[0]["country"]}#{response.json()[0]["pp_country_rank"]})', fill=(
        240, 90, 90), font=default_font)

    draw.text((16, 64), 'level:', fill=(255, 255, 255), font=default_font)
    level = response.json()[0]["level"]
    draw.text((69, 64), f'{int(float(level))} ({(( float(level)- int(float(level)) )*100):.2f}%)',
              fill=(240, 90, 90), font=default_font)

    draw.text((16, 84), 'net pp:', fill=(255, 255, 255), font=default_font)
    draw.text((75, 84), f'{response.json()[0]["pp_raw"]}', fill=(
        240, 90, 90), font=default_font)

    draw.text((16, 104), 'hit accuracy:', fill=(
        255, 255, 255), font=default_font)
    draw.text((129, 104), f'{float(response.json()[0]["accuracy"]):.2f}%', fill=(
        240, 90, 90), font=default_font)

    draw.text((16, 124), 'playcount:', fill=(255, 255, 255), font=default_font)
    draw.text((112, 124), f'{response.json()[0]["playcount"]}', fill=(
        240, 90, 90), font=default_font)

    draw.text((40, 148), 'SS', fill=(162, 162, 162),
              font=rank_font, anchor='mt')
    draw.text((120, 148), 'S', fill=(245, 225, 90),
              font=rank_font, anchor='mt')
    draw.text((200, 148), 'A', fill=(76, 208, 54), font=rank_font, anchor='mt')

    draw.text((40, 178), f'{int(response.json()[0]["count_rank_ss"]) + int(response.json()[0]["count_rank_ssh"])}', fill=(
        255, 255, 255), font=default_font, anchor='mt')
    draw.text((120, 178), f'{int(response.json()[0]["count_rank_s"]) + int(response.json()[0]["count_rank_sh"])}', fill=(
        255, 255, 255), font=default_font, anchor='mt')
    draw.text((200, 178), f'{int(response.json()[0]["count_rank_a"])}', fill=(
        255, 255, 255), font=default_font, anchor='mt')

    return img


def get_mods_from_play(play_data):
    mod_code = int(play_data['enabled_mods'])
    mod_code = list(bin(mod_code)[2:])
    mod_code.reverse()

    # nomod
    if mod_code == '0':
        mods = ['NM']
    else:
        mods = [mod_list[x]
                for x in range(len(mod_code)) if mod_code[x] == '1']

    if ('SD' in mods) and ('PF' in mods):
        mods.remove('SD')
    if ('DT' in mods) and ('NC' in mods):
        mods.remove('DT')

    return mods


def get_mod_images_from_mods(mods):
    mod_images = [Image.fromarray(
        np.array(mods_image_data[mod], dtype=np.uint8)) for mod in mods]
    return mod_images


def calculate_pp(beatmap_data, play_data, completion):
    return osu.ppv2(aim_stars=float(beatmap_data["diff_aim"]),
                    speed_stars=float(beatmap_data["diff_speed"]),
                    max_combo=int(beatmap_data["max_combo"])*completion,
                    nsliders=int(beatmap_data["count_slider"])*completion,
                    ncircles=int(beatmap_data["count_normal"])*completion,
                    nobjects=int(beatmap_data["count_spinner"])*completion,
                    base_ar=float(beatmap_data["diff_approach"]),
                    base_od=float(beatmap_data["diff_overall"]),
                    mode=int(beatmap_data["mode"]),
                    mods=int(play_data["enabled_mods"]),
                    combo=int(play_data["maxcombo"]),
                    n300=int(play_data["count300"]),
                    n100=int(play_data["count100"]),
                    n50=int(play_data["count50"]),
                    nmiss=int(play_data["countmiss"]),
                    score_version=1)[0]


def calculate_fc_pp(beatmap_data, play_data):
    return osu.ppv2(aim_stars=float(beatmap_data["diff_aim"]),
                    speed_stars=float(beatmap_data["diff_speed"]),
                    max_combo=int(beatmap_data["max_combo"]),
                    nsliders=int(beatmap_data["count_slider"]),
                    ncircles=int(beatmap_data["count_normal"]),
                    nobjects=int(beatmap_data["count_spinner"]),
                    base_ar=float(beatmap_data["diff_approach"]),
                    base_od=float(beatmap_data["diff_overall"]),
                    mode=int(beatmap_data["mode"]),
                    mods=int(play_data["enabled_mods"]),
                    combo=int(play_data["maxcombo"]),
                    n300=int(play_data["count300"]) +
                    int(play_data["countmiss"]),
                    n100=int(play_data["count100"]),
                    n50=int(play_data["count50"]),
                    nmiss=0,
                    score_version=1)[0]


if __name__ == "__main__":
    beatmap_data = {
        "beatmapset_id": "336099",
        "beatmap_id": "743896",
        "approved": "1",
        "total_length": "151",
        "hit_length": "145",
        "version": "Lunatic",
        "file_md5": "d08d7f2faed17dd0b0d1a3fa20e439e2",
        "diff_size": "4",
        "diff_overall": "9",
        "diff_approach": "9.4",
        "diff_drain": "6.6",
        "mode": "0",
        "count_normal": "538",
        "count_slider": "200",
        "count_spinner": "1",
        "submit_date": "2015-07-19 12:26:20",
        "approved_date": "2015-08-24 17:00:14",
        "last_update": "2015-08-17 15:29:12",
        "artist": "LeaF",
        "artist_unicode": "LeaF",
        "title": "Wizdomiot",
        "title_unicode": "Wizdomiot",
        "creator": "Asahina Momoko",
        "creator_id": "3650145",
        "bpm": "200",
        "source": "BMS",
        "tags": "東方project touhou zun 東方地霊殿 ～ subterranean animism 東方音弾遊戯7 optie 緑眼のジェラシー 水橋 パルスィ green eyed jealousy mizuhashi parsee mokori m_o_k_o_r_i rational punishment featured artist",
        "genre_id": "2",
        "language_id": "5",
        "favourite_count": "707",
        "rating": "9.58895",
        "storyboard": "0",
        "video": "1",
        "download_unavailable": "0",
        "audio_unavailable": "0",
        "playcount": "620946",
        "passcount": "55585",
        "packs": "A62,S426",
        "max_combo": "1164",
        "diff_aim": "2.83409",
        "diff_speed": "3.05964",
        "difficultyrating": "6.00651"
    }

    play_data = {
        "beatmap_id": "743896",
        "score": "186741",
        "maxcombo": "92",
        "count50": "18",
        "count100": "81",
        "count300": "147",
        "countmiss": "28",
        "countkatu": "24",
        "countgeki": "10",
        "perfect": "0",
        "enabled_mods": "9",
        "user_id": "7630046",
        "date": "2021-01-31 21:43:50",
        "rank": "F"
    }

    cover = Image.open(osu_api.get_beatmap_cover_data(336099))

    img = display_plays([beatmap_data], [play_data], [cover])
    img.show()
