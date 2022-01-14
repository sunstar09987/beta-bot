import discord, datetime, asyncio, random, status, guild
import member, pytz

client = discord.Client

token = "OTI5NjM5NDQzMDgwNTY4ODMy.YdqQMw.8jgbba4zPhXFCYHSV2tph9dDPrw"       
client = discord.Client()

@client.event
async def on_member_join(member):
    await member.send(f'안녕하세요 {member}님, 환영합니다!')

@client.event
async def on_ready():
    print(f"joiend {client.user}.")
    print('봇이 성공적으로 동작합니다.')
    print("==========================")
    game = discord.Game("리그오브레전드")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "테스트": # 메세지 감지
        await message.channel.send ("{} | {}, Hello".format(message.author, message.author.mention))
        await message.author.send ("{} | {}, User, Hello".format(message.author, message.author.mention))


    

@client.event
async def on_message(message):
    if message.content.startswith('$greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))

        

    #if message.content == "임베드": # 메세지 감지
        embed = discord.Embed(title="명령어 목록", description="테스트 부제목")

        embed.add_field(name="ㅎㅇ", value="ㅎㅇ", inline=False)
        embed.add_field(name="너 봇임?", value="라인 이름에 해당하는 값", inline=False)

        embed.add_field(name="임베드 라인 3 - inline = true로 책정", value="라인 이름에 해당하는 값", inline=True)
        embed.add_field(name="임베드 라인 4 - inline = true로 책정", value="라인 이름에 해당하는 값", inline=True)

        embed.set_footer(text="Bot Made by. Beta Bot!#4390", icon_url="https://cdn.discordapp.com/attachments/929652398966841404/930073202703630366/u.jpg")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/929652398966841404/930073202703630366/u.jpg")
        await message.channel.send (embed=embed)
    
    if message.content == "ㅎㅇ":  
        await message.channel.send(f"{message.author.name}님, ㅎㅇ!")

        
    if message.content == "/서버규칙":
        await message.channel.send(f"""게임과 수다를 떠는곳의 서버 규칙!
1. 선 넘는 욕설 금지 :negative_squared_cross_mark:
2. 노래 스킵할거면 물어보고 스킵 :zany_face:
3. 상처가 되는 말 하지 않기 :negative_squared_cross_mark:
4. 관리자 , 부관리자 말은 꼭 들어주세요 :sweat_smile:
5. 노래 틀거면 노래-제목 에다가 노래 검색하고 틀어주세요 :notes:
6. 성적인 이야기 패드립 성드립 치는 사람 경고 조치 없이 강퇴 입니다 
7. 관리자 달라 떼쓰지 말아주세요 :smiling_face_with_tear:
8. 자기 보다 어른 누나 형 언니 오빠 이면 예의를 지켜주세요 :revolving_hearts:
9. 필요하거나 하고 싶은게 있으면 관리자 부관리자에게 말해주세요 가능 한건 해드릴게요 :kissing_smiling_eyes: 
10. 서버 관리자 ( 은하수 조성빈 하나 준호 현석 ) 부관리자 ( 샤인 님 영준 님  ) 
11. 친목질 금지:white_check_mark:
나의 작은 아기 고양이 규칙 지켜주세요 """)

    if message.content == "넌 누가 만듦?":
        await message.channel.send(f"전 wkdwltjd14님이 만들어 주심!")

    if message.content == "도와줘":
        await message.channel.send(f"네, 무엇을 도와드릴 까요?,")
         
    if message.content == "봇아":
        await message.channel.send(f"왜앵")

    if message.content == "뭐해":
         await message.channel.send(f"아무것도 않해")

    if message.content.startswith(f"/채널메시지"):
        ch = client.get_channel(int(message.content[7:25]))
        await ch.send(message.content[26:])

    if message.content == "잘자~":
        await message.channel.send(f"good night~~~!")

    if message.content == '내정보':
        user = message.author
        date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
        await message.channel.send(f"{message.author.mention}의 가입일 : {date.year}/{date.month}/{date.day}")
        await message.channel.send(f"{message.author.mention}의 이름: {user.name} / 아이디: {user.id} / 닉네임: {user.display_name}")
        await message.channel.send(message.author.avatar_url)

    if message.content =="랜덤숫자":
        await message.channel.send(random.randint(1, 10))

    if message.content == "10초타이머":
        await asyncio.sleep(10)
        await message.channel.send(f"{message.author.mention}, 10초가 지났어요!")

    if message.content.startswith ("/공지"):
        await message.channel.purge(limit=1)
        i = (message.author.guild_permissions.administrator)
        if i is True:
            notice = message.content[4:]
            channel = client.get_channel(930662566244515901)
            embed = discord.Embed(title="**공지사항 봇 테스트가 정상적으로 완료되었습니다.*", description="\n자동공지!\n\n{}\n\n공지사항 문의가능".format(notice),timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0x00ff00)
            embed.set_footer(text="Bot Made by. wkdlwtjd14 #4422 | 담당 관리자 : {}".format(message.author), icon_url="https://cdn.discordapp.com/attachments/930662566244515901/931381502535684096/road-220058.jpg")
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/930662566244515901/931381502535684096/road-220058.jpg")
            await channel.send ("", embed=embed)
            await message.author.send("""*-------------------------------------------------------------------------------------------
[ BOT 자동 알림 ]* | 정상적으로 공지가 채널에 작성이 완료되었습니다 : )\n\n[ 기본 작성 설정 채널 ] : {}\n[ 공지 발신자 ] : {}\n\n[ 내용 ]\n{}""".format(channel, message.author, notice))
                                           
        if i is False:
            await message.channel.send("{}, 당신은 관리자가 아닙니다".format(message.author.mention))


    if message.content.startswith ("/청소"):
        i = (message.author.guild_permissions.administrator)
        if i is True:
            amount = message.content[4:]
            await message.channel.purge(limit=1)
            await message.channel.purge(limit=int(amount))

            embed = discord.Embed(title="메시지 삭제 알림", description="최근 디스코드 채팅 {}개가\n관리자 {}님의 요청으로 인해 정상 삭제 조치 되었습니다".format(amount, message.author), color=0x000000)
            embed.set_footer(text="Bot Made by. wkdlwtjd14 #4422", icon_url="https://discordapp.com/channels/691615852620939274/703908401381376000/711859989177958410")
            await message.channel.send(embed=embed)
        
        if i is False:
            await message.channel.purge(limit=1)
            await message.channel.send("{}, 당신은 명령어를 사용할 수 있는 권한이 없습니다".format(message.author.mention))

        


    if message.content.startswith ("/관리자인증 "):
        if message.author.guild_permissions.administrator:
            await message.delete()
            user = message.mentions[0]

            embed = discord.Embed(title="인증 시스템", description="인증이 정상적으로 완료 되었습니다 !",timestamp=datetime.datetime.now(pytz.timezone('UTC')), color=0xff0000)
            embed.add_field(name="인증 대상자", value=f"{user.name} ( {user.mention} )", inline=False)
            embed.add_field(name="담당 관리자", value=f"{message.author} ( {message.author.mention} )", inline=False)
            embed.set_footer(text="Bot Made by. wkdlwtjd14 #4422")
            await message.author.send (embed=embed)
            role = discord.utils.get(message.guild.roles, name = "관리자")
            await user.add_roles(role)

        else:
            await message.delete()
            await message.channel.send(embed=discord.Embed(title="권한 부족", description = message.author.mention + "님은 권한이 없습니다", color = 0xff0000))
   




@client.event
async def on_member_join(member):
    channel = client.get_channel(930662557507801158)#수다떨자채널
    await channel.send("반갑습니다! 방문하신 것을 환영해요.")

client.run("OTI5NjM5NDQzMDgwNTY4ODMy.YdqQMw.8jgbba4zPhXFCYHSV2tph9dDPrw")
