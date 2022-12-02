## Ran on AWS

import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '$')
client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity = discord.Game("$help"))
    print('Bot is ready')

@client.command(aliases = ['h', 'H', 'Help'])
async def help(ctx):
    user = ctx.author.id
    help = discord.Embed(title = 'Help', colour = 0xff0000)

    help.add_field(name = "Lecturers", value = "$lecturers - Lists the lecturers and their emails", inline = False)
    help.add_field(name = "Assistants", value = "$assistants - Lists the teaching assistants and their emails", inline = False)
    help.add_field(name = "Timetable", value = "$timetable - Shows this semesters timetable", inline = False)
    help.add_field(name = "Student Representitives", value = "$studentrep - Lists the stage 1 student representitives", inline = False)
    help.add_field(name = "Coursework", value = "$coursework - Shows what coursework is due and when", inline = False)
    help.add_field(name = "Term Dates", value = "$termdates - Shows when each semester starts and ends as well as other important dates", inline = False)
    help.add_field(name = "Degree Class Percentages", value = "$percentages - Shows what percentages are needed for each degree class", inline = False)
    help.add_field(name = "Zoom Links", value = "$zoom - Lists all the zoom codes and passwords for each module", inline = False)
    # help.add_field(name = "", value = "", inline = False)

    await ctx.author.send(embed = help)
    await ctx.send(f'<@{user}> Commands sent!!')


@client.command(aliases = ['Timetable', 't', 'T'])
async def timetable(ctx):
    timetable = discord.Embed(title = "Timetable", colour = 0xff0000)
    timetable.add_field(name = "Monday", value = "09:00\tCharles Optional Video Watch along\n\n10:00\tIN1006 System Architecture\nLecturer = George Spanoudakis", inline = False)
    timetable.add_field(name = "Tuesday", value = "09:00\tCharles Optional Video Watch along\n\n10:00\tIN1007 Programming in Java\nLecturer = Laure Daviaud", inline = False)
    timetable.add_field(name = "Wednesday", value = "\u200b\n", inline = False)
    timetable.add_field(name = "Thursday", value = "09:00\tCharles Optional Video Watch along\n\n10:00\tIN1004 Mathematics for Computing\nLecturer = Jacob Howe", inline = False)
    timetable.add_field(name = "Friday", value = "09:00\tCharles Optional Video Watch along\n\n10:00\tIN1010 Databases and Web Development\nLecturer = Christopher Smart", inline = False)

    await ctx.send(embed=timetable)

@client.command(aliases = ['Lecturers', 'l', 'L'])
async def lecturers(ctx):
    lecturers = discord.Embed(title = "Lecturers", colour = 0xff0000)
    lecturers.add_field(name = "Jo Wood", value = "Email: J.D.Wood@city.ac.uk", inline = False)
    lecturers.add_field(name = "Jacob Howe", value = "J.M.Howe@city.ac.uk", inline = False)
    lecturers.add_field(name = "Radu Jianu", value = "Radu.Jianu@city.ac.uk", inline = False)
    lecturers.add_field(name = "Christopher Smart", value = "C.Smart@city.ac.uk", inline = False)
    lecturers.add_field(name = "George Spanoudakis", value = "G.E.Spanoudakis@city.ac.uk", inline = False)
    lecturers.add_field(name = "Laure Daviaud", value = "Laure.Daviaud@city.ac.uk", inline = False)
    # lecturers.add_field(name = "", value = "", inline = False)

    await ctx.send(embed=lecturers)

@client.command(aliases = ['Assistants', 'a', 'A'])
async def assistants(ctx):
    assistants = discord.Embed(title = "Teaching Assistants", colour = 0xff0000)
    assistants.add_field(name = "Charles Watson", value = "Charles.Watson.1@city.ac.uk", inline = False)
    assistants.add_field(name = "Olga Herrero", value = "Olga.Herrero.1@city.ac.uk", inline = False)
    assistants.add_field(name = "Aravin Naren", value = "Aravin.Naren.1@city.ac.uk", inline = False)
    assistants.add_field(name = "Kamal Pal", value = "K.pal@city.ac.uk", inline = False)
    assistants.add_field(name = "Aspen Fernandes", value = "Aspen.Fernandes@city.ac.uk", inline = False)
    assistants.add_field(name = "Hana Rauf", value = "Hana.Rauf@city.ac.uk", inline = False)
    assistants.add_field(name = "Ilyas Aden", value = "Ilyas.aden@city.ac.uk", inline = False)
    assistants.add_field(name = "Marius Zicius", value = "Marius.Zicius.2@city.ac.uk", inline = False)
    assistants.add_field(name = "Asli Mohammed", value = "Asli.Mohammed@city.ac.uk", inline = False)
    # assistants.add_field(name = "", value = "", inline = False)

    await ctx.send(embed=assistants)

@client.command(aliases = ['rep', 'reps', 'r', 'R', 'Rep', 'Reps', 'Studentrep', 'studentreps', 'Studentreps'])
async def studentrep(ctx):
    reps = discord.Embed(title = "Student Representitives", colour = 0xff0000)
    reps.add_field(name = "Placeholder Name", value = "Email: name1@city.ac.uk\nDiscord: nickname#1603", inline = False)
    reps.add_field(name = "Placeholder Name", value = "Email: name2@city.ac.uk\nDiscord: nickname#0480", inline = False)
    reps.add_field(name = "Placeholder Name", value = "Email: name3@city.ac.uk\nDiscord: nickname#2465", inline = False)
    reps.add_field(name = "Placeholder Name", value = "Email: name4@city.ac.uk\nDiscord: nickname#6967", inline = False)
    reps.add_field(name = "Placeholder Name", value = "Email: name5@city.ac.uk\nDiscord: nickname#8499", inline = False)
    reps.add_field(name = "Placeholder Name", value = "Email: name6@city.ac.uk\nDiscord: nickname#4338", inline = False)

    # reps.add_field(name = "", value = "", inline = False)

    await ctx.send(embed=reps)

## Coursework dates

@client.command(aliases = ['c', 'cw', 'C', 'CW', 'Coursework'])
async def coursework(ctx):
    coursework = discord.Embed(title = "Coursework Deadlines", colour = 0xff0000)
    coursework.set_image(url = 'https://media.discordapp.net/attachments/758334962797248532/760487756634783804/unknown.png')

    await ctx.send(embed = coursework)

@client.command(aliases = ['td', 'TD', 'Td', 'termdates', 'Termdates', 'TermDates'])
async def termDates(ctx):
    termDates = discord.Embed(title = "Term Dates", colour = 0xff0000)
    termDates.set_image(url = 'https://media.discordapp.net/attachments/760120840397783060/767414872584486952/unknown.png')

    await ctx.send(embed = termDates)

## Add degree percentages
@client.command(aliases = ['p', 'P', 'Percentages'])
async def percentages(ctx):
    percentages = discord.Embed(title = "", colour = 0xff0000)
    percentages.add_field(name = "First", value = "70 - 100%", inline = False)
    percentages.add_field(name = "Upper Second Class 2:1", value = "60 - 69%", inline = False)
    percentages.add_field(name = "Lower Second Class 2:2", value = "50 - 59%", inline = False)
    percentages.add_field(name = "Third", value = "40 - 49%", inline = False)
    percentages.add_field(name = "Fail", value = "< 40%", inline = False)

    await ctx.send(embed = percentages)

## Add zoom links for each module // group
@client.command(aliases = ['Zoom', 'z', ' Z', 'link', 'links', 'Link', 'Links'])
async def zoom(ctx):
    links = discord.Embed(title = "Zoom links", colour = 0xff0000)

    links.add_field(name = "IN1004 Mathematics for Computing",\
    value = "__Lecture__\nCode: 878 5587 6394\nPassword: IN1004plen\
    \n\n__Groups__\nA - 868 3994 4767\nPassword - IN1004gpa\
    \n\nB - 878 5144 3503\nPassword - IN1004\
    \n\nC - 824 4549 9511\nPassword - IN1004gpC\
    \n\nD - 850 4670 5762\nPassword - IN1004gpD\
    \n\nE - 816 3567 6848\nPassword - IN1004gpE\
    \n\nF - 863 0167 5758\nPassword - IN1004\
    \n\nG - 818 7609 6490\nPassword - IN1004\
    \n\nH - 896 1150 9459\nPassword - IN1004gpH", inline = True)

    links.add_field(name = "IN1006 System Architecture",
    value = "__Lecture__\nCode: 821 3965 8904\nPassword - IN1006\
    \n\n__Groups__\nA - 832 4099 3762\nPassword - IN1006\
    \n\nB - 850 2594 1032\nPassword - IN1006\
    \n\nC - 876 9472 1974\nPassword - IN1006\
    \n\nD - 874 3706 5056\nPassword - IN1006\
    \n\nE - 810 6330 6190\nPassword - IN1006\
    \n\nF - 868 5046 3675\nPassword - IN1006\
    \n\nG - 894 3780 8441\nPassword - IN1006\
    \n\nH - 868 7241 6366\nPassword - IN1006", inline = True)

    links.add_field(name = "\u200b", value = "\u200b")

    links.add_field(name = "IN1007 Programming in Java",\
    value = "__Lecture__\nCode: 967 5663 9280\nPassword: JAVA2020\
    \n\n__Groups__\nA - 899 0482 1438\nPassword - IN1007\
    \n\nB - 832 4111 4125\nPassword - IN1007\
    \n\nC - 848 2593 4087\nPassword - IN1007\
    \n\nD - 818 1897 2134\nPassword - IN1007\
    \n\nE - 986 8909 8596\nPassword - JAVALab\
    \n\nF - 835 5668 3761\nPassword - JAVALab\
    \n\nG - 838 3185 6054\nPassword - JAVALab\
    \n\nH - 850 2137 0503\nPassword - JAVALab\
    \n\nI - 849 2195 4138\nPassword - JAVALab", inline = True)

    links.add_field(name = "IN1010 Databases and \nWeb Development",\
    value = "__Lecture__\nCode: 836 3007 6341\nPassword: IN1010\
    \n\n__Groups__\nA - 89690842763\nPassword - IN1010\
    \n\nB - 835 4681 7429\nPassword - IN1010\
    \n\nC - 848 6387 1240\nPassword - IN1010\
    \n\nD - 870 5966 1101\nPassword - IN1010\
    \n\nE - 832 8120 1793\nPassword - IN1010\
    \n\nF - 896 9084 0264\nPassword - IN1010\
    \n\nG - 897 3482 3547\nPassword - IN1010\
    \n\nH - 895 0235 8620\nPassword - IN1010", inline = True)

    links.add_field(name = "\u200b", value = "\u200b")

    links.add_field(name = "Charles' Watch Along Session",\
    value = "Code: 868 6515 4807\nPassword: videos")

    await ctx.send(embed = links)



client.run('discordKey')
